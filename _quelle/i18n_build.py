#!/usr/bin/env python3
"""Erzeugt EN/FR/IT/ES-Versionen aus den deutschen Seiten in site/ und ergänzt hreflang, Sprachmenü, Sitemap."""
import os, re, json, glob, hashlib, datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

DOMAIN = "https://alpinhost.ch"
LANGS = ["en", "fr", "it", "es"]
ALL = ["de"] + LANGS
HTML_LANG = {"de": "de-CH", "en": "en", "fr": "fr-CH", "it": "it-CH", "es": "es"}
OG_LOC = {"de": "de_CH", "en": "en_GB", "fr": "fr_CH", "it": "it_CH", "es": "es_ES"}
LABEL = {"de": "Deutsch", "en": "English", "fr": "Français", "it": "Italiano", "es": "Español"}
TODAY = datetime.date.today().isoformat()

SLUG = {
 "/": {"en": "/en/", "fr": "/fr/", "it": "/it/", "es": "/es/"},
 "/airbnb-verwaltung-grindelwald/": {"en": "/en/airbnb-management-grindelwald/", "fr": "/fr/gestion-airbnb-grindelwald/", "it": "/it/gestione-airbnb-grindelwald/", "es": "/es/gestion-airbnb-grindelwald/"},
 "/airbnb-verwaltung-interlaken/": {"en": "/en/airbnb-management-interlaken/", "fr": "/fr/gestion-airbnb-interlaken/", "it": "/it/gestione-airbnb-interlaken/", "es": "/es/gestion-airbnb-interlaken/"},
 "/airbnb-verwaltung-lauterbrunnen-wengen-muerren/": {"en": "/en/airbnb-management-lauterbrunnen-wengen-muerren/", "fr": "/fr/gestion-airbnb-lauterbrunnen-wengen-muerren/", "it": "/it/gestione-airbnb-lauterbrunnen-wengen-muerren/", "es": "/es/gestion-airbnb-lauterbrunnen-wengen-muerren/"},
 "/airbnb-verwaltung-luzern/": {"en": "/en/airbnb-management-lucerne/", "fr": "/fr/gestion-airbnb-lucerne/", "it": "/it/gestione-airbnb-lucerna/", "es": "/es/gestion-airbnb-lucerna/"},
 "/airbnb-verwaltung-bern/": {"en": "/en/airbnb-management-bern/", "fr": "/fr/gestion-airbnb-berne/", "it": "/it/gestione-airbnb-berna/", "es": "/es/gestion-airbnb-berna/"},
 "/airbnb-verwaltung-schweiz/": {"en": "/en/airbnb-management-switzerland/", "fr": "/fr/gestion-airbnb-suisse/", "it": "/it/gestione-airbnb-svizzera/", "es": "/es/gestion-airbnb-suiza/"},
 "/impressum/": {"en": "/en/imprint/", "fr": "/fr/mentions-legales/", "it": "/it/note-legali/", "es": "/es/aviso-legal/"},
 "/datenschutz/": {"en": "/en/privacy/", "fr": "/fr/protection-des-donnees/", "it": "/it/privacy/", "es": "/es/privacidad/"},
}
INDEXABLE = [p for p in SLUG if p not in ("/impressum/", "/datenschutz/")]

def lang_path(p, lang):
    return p if lang == "de" else SLUG[p][lang]

# ---------- Übersetzungen laden
def load_tr():
    T = {}
    for f in sorted(glob.glob("i18n/tr*.txt")):
        for block in open(f, encoding="utf-8").read().split("\n\n"):
            d = {}
            for line in block.strip().split("\n"):
                if line[:4] in ("de: ", "en: ", "fr: ", "it: ", "es: "):
                    d[line[:2]] = line[4:]
            if "de" in d:
                missing = [l for l in LANGS if l not in d]
                assert not missing, (d["de"], missing)
                T[d["de"]] = {l: d[l] for l in LANGS}
    return T
T = load_tr()
def strip_tags(h): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h)).replace("&amp;", "&").strip()
T_STRIP = {strip_tags(k): {l: strip_tags(v[l]) for l in LANGS} for k, v in T.items()}

MISSING = {}
INLINE = {"a","b","strong","i","em","span","small","br","sup","sub","abbr","code","time","mark","u"}
SKIP = {"script","style","svg","noscript"}
def has_text(t): return bool(re.search(r"[A-Za-zÄÖÜäöüé]", t))
def norm(h): return re.sub(r"\s+", " ", h).strip()

def placeholders(html):
    vals = {"H": [], "S": []}
    def rep(m):
        k = "H" if m.group(1) == "href" else "S"
        vals[k].append(m.group(2)); return f'{m.group(1)}="{{{k}{len(vals[k])-1}}}"'
    return re.sub(r'(href|style)="([^"]*)"', rep, html), vals
def unplace(html, vals):
    for k in ("H", "S"):
        for i, v in enumerate(vals[k]): html = html.replace(f"{{{k}{i}}}", v)
    return html

KEEP = {"Alpinhost","Grindelwald","Interlaken","Engelberg","Andermatt","Zermatt","Verbier","Saas-Fee","Crans-Montana","Lausanne","Lugano","CHF 0","Wengen","Lauterbrunnen","info@alpinhost.ch","de","en","fr","it","es",
 "Interlaken · Unterseen · Matten · Wilderswil · Bönigen · Ringgenberg","Lauterbrunnen · Wengen · Mürren · Gimmelwald · Stechelberg · Isenfluh"}
def tr_text(s, lang, where):
    t = norm(s)
    if not has_text(t) or t in KEEP: return s
    if t in T:
        lead = s[:len(s)-len(s.lstrip())]; trail = s[len(s.rstrip()):]
        return lead + T[t][lang] + trail
    MISSING.setdefault(t, where); return s

def is_unit(el):
    for d in el.descendants:
        if isinstance(d, Tag) and d.name not in INLINE: return False
    return has_text(el.get_text())

def translate_children(el, lang, where):
    for c in list(el.children):
        if isinstance(c, Comment): continue
        if isinstance(c, NavigableString):
            if has_text(str(c)): c.replace_with(tr_text(str(c), lang, where))
        elif isinstance(c, Tag) and c.name not in SKIP:
            if is_unit(c) and c.name not in INLINE | {"html","body","head"}:
                key, vals = placeholders(norm(c.decode_contents()))
                if key in T:
                    new = unplace(T[key][lang], vals)
                    c.clear()
                    frag = BeautifulSoup(new, "html.parser")
                    for n in list(frag.contents): c.append(n)
                    continue
            translate_children(c, lang, where)

def tr_json(o, lang):
    if isinstance(o, dict):
        return {k: (tr_json(v, lang) if k not in ("@context","@type","@id","telephone","email","image","logo") else v) for k, v in o.items()}
    if isinstance(o, list): return [tr_json(v, lang) for v in o]
    if isinstance(o, str):
        if o.startswith(DOMAIN):
            p = urlparse(o).path
            return DOMAIN + lang_path(p, lang) if p in SLUG else o
        if o in ("de-CH",): return HTML_LANG[lang]
        t = norm(o)
        if t in T: return T[t][lang]
        if t in T_STRIP: return T_STRIP[t][lang]
        if has_text(t) and t not in KEEP and not re.fullmatch(r"[A-Z][\w\-. &]+", t): MISSING.setdefault(t, "json")
        return o
    return o

def switcher(page_path, lang):
    items = "".join(
        f'<a href="{lang_path(page_path, l)}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}"{" aria-current=\"true\"" if l == lang else ""}>{LABEL[l]}<span>{l.upper()}</span></a>'
        for l in ALL)
    aria = {"de": "Sprache wählen", "en": "Choose language", "fr": "Choisir la langue", "it": "Scegli la lingua", "es": "Elegir idioma"}[lang]
    return (f'<details class="langsw"><summary aria-label="{aria}">{lang.upper()}<svg viewBox="0 0 12 12" aria-hidden="true">'
            f'<path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></summary><div class="menu">{items}</div></details>')

def fix_head(s, page_path, lang, indexable):
    url = DOMAIN + lang_path(page_path, lang)
    s.html["lang"] = HTML_LANG[lang]
    for l in s.find_all("link", rel="alternate"): l.decompose()
    can = s.find("link", rel="canonical")
    if can: can["href"] = url
    ogu = s.find("meta", property="og:url")
    if ogu: ogu["content"] = url
    ogl = s.find("meta", property="og:locale")
    if ogl: ogl["content"] = OG_LOC[lang]
    if indexable and can:
        anchor = can
        for l in ALL + ["x-default"]:
            tag = s.new_tag("link", rel="alternate", hreflang=HTML_LANG.get(l, "x-default"), href=DOMAIN + lang_path(page_path, "de" if l == "x-default" else l))
            anchor.insert_after(tag); anchor.insert_after("\n"); anchor = tag

def rewrite_links(s, de_path, lang):
    base = DOMAIN + de_path
    def conv(u):
        if not u or u.startswith(("mailto:", "tel:", "https://wa.me", "javascript:", "data:")) or (u.startswith("http") and "alpinhost.ch" not in u): return u
        full = urlparse(urljoin(base, u))
        p = full.path
        if p in SLUG or p + "/" in SLUG:
            p = p if p in SLUG else p + "/"
            out = lang_path(p, lang)
        else:
            out = p
        return out + (("#" + full.fragment) if full.fragment else "")
    for el in s.find_all(href=True):
        if el.name == "link" and el.get("rel") in (["canonical"], ["alternate"]): continue
        if el.name == "a" or el.name == "link": el["href"] = conv(el["href"])
    for el in s.find_all(src=True): el["src"] = conv(el["src"])
    for el in s.find_all(srcset=True):
        el["srcset"] = ", ".join((conv(p.split()[0]) + " " + " ".join(p.split()[1:])).strip() for p in el["srcset"].split(","))

# ---------- JS pro Sprache
JS_TR = {
 "en": [("Wird gesendet …","Sending …"),("<b>Danke, Ihre Anfrage ist bei uns.</b> Wir melden uns am selben Werktag.","<b>Thank you, we have received your enquiry.</b> We will get back to you the same working day."),('btn.textContent="Gesendet"','btn.textContent="Sent"'),("Das Senden hat nicht geklappt. Bitte ","Sending did not work. Please "),(">per WhatsApp senden</a> oder an ",">send via WhatsApp</a> or write to "),("</a> schreiben.","</a>."),("Persönliche Schätzung","Personal estimate"),("Für Ihren Ort rechnen wir mit echten Vergleichswohnungen aus der Nachbarschaft, kostenlos. ","For your location we calculate with real comparable apartments nearby, free of charge. "),(">Wohnung prüfen lassen</a>",">Get a free assessment</a>"),
   ("<span>Auslastung ","<span>Occupancy "),("Gebuchte Nächte pro Jahr","Booked nights per year"),("Nachtpreis im Schnitt","Average nightly rate"),("Umsatz pro Jahr","Revenue per year"),("Plattformgebühr 15,5 %","Platform fee 15.5 %"),("<span>Provision ","<span>Commission "),("Bleibt bei Ihnen pro Jahr","You keep per year"),(" <small>pro Monat</small>"," <small>per month</small>"),
   ('"Basis: "+r.n','"Based on "+r.n'),(" aktive Airbnb-Inserate in "," active Airbnb listings in "),(", Ø Nachtpreis ",", avg. nightly rate "),(", Ø Auslastung ",", avg. occupancy "),('"Basis: Durchschnitt der Airbnb-Inserate in der Zentralschweiz, Ø Nachtpreis "','"Based on the average of Airbnb listings in Central Switzerland, avg. nightly rate "'),
   ('b.textContent="Kopiert"','b.textContent="Copied"'),('b.textContent="Kopieren"','b.textContent="Copy"'),('"Paket "+pkg+" wählen"','"Choose package "+pkg'),
   ("Bitte Name, Telefon und Ort der Wohnung ausfüllen.","Please fill in name, phone and apartment location."),("Ihre Anfrage ist vorbereitet. ","Your enquiry is ready. "),("In WhatsApp öffnen und senden","Open and send in WhatsApp"),(". Lieber anrufen? ",". Prefer to call? "),
   ("Anfrage Alpinhost\\n","Alpinhost enquiry (EN)\\n"),("\\nTelefon: ","\\nPhone: "),("\\nOrt: ","\\nLocation: "),("\\nZimmer: ","\\nRooms: "),("\\nPaket: ","\\nPackage: "),("\\nNachricht: ","\\nMessage: ")],
 "fr": [("Wird gesendet …","Envoi en cours …"),("<b>Danke, Ihre Anfrage ist bei uns.</b> Wir melden uns am selben Werktag.","<b>Merci, nous avons bien reçu votre demande.</b> Nous vous répondons le jour ouvrable même."),('btn.textContent="Gesendet"','btn.textContent="Envoyé"'),("Das Senden hat nicht geklappt. Bitte ","L’envoi n’a pas fonctionné. Veuillez "),(">per WhatsApp senden</a> oder an ",">envoyer par WhatsApp</a> ou écrire à "),("</a> schreiben.","</a>."),("Persönliche Schätzung","Estimation personnalisée"),("Für Ihren Ort rechnen wir mit echten Vergleichswohnungen aus der Nachbarschaft, kostenlos. ","Pour votre lieu, nous calculons gratuitement avec de vrais logements comparables du voisinage. "),(">Wohnung prüfen lassen</a>",">Faire évaluer mon logement</a>"),
   ("<span>Auslastung ","<span>Taux d'occupation "),("Gebuchte Nächte pro Jahr","Nuits réservées par an"),("Nachtpreis im Schnitt","Prix moyen par nuit"),("Umsatz pro Jahr","Chiffre d'affaires annuel"),("Plattformgebühr 15,5 %","Frais de plateforme 15,5 %"),("<span>Provision ","<span>Commission "),("Bleibt bei Ihnen pro Jahr","Il vous reste par an"),(" <small>pro Monat</small>"," <small>par mois</small>"),
   ('"Basis: "+r.n','"Base : "+r.n'),(" aktive Airbnb-Inserate in "," annonces Airbnb actives – "),(", Ø Nachtpreis ",", prix moyen par nuit "),(", Ø Auslastung ",", taux d'occupation moyen "),('"Basis: Durchschnitt der Airbnb-Inserate in der Zentralschweiz, Ø Nachtpreis "','"Base : moyenne des annonces Airbnb de Suisse centrale, prix moyen par nuit "'),
   ('b.textContent="Kopiert"','b.textContent="Copié"'),('b.textContent="Kopieren"','b.textContent="Copier"'),('"Paket "+pkg+" wählen"','"Choisir la formule "+pkg'),
   ("Bitte Name, Telefon und Ort der Wohnung ausfüllen.","Veuillez indiquer le nom, le téléphone et le lieu du logement."),("Ihre Anfrage ist vorbereitet. ","Votre demande est prête. "),("In WhatsApp öffnen und senden","Ouvrir et envoyer dans WhatsApp"),(". Lieber anrufen? ",". Vous préférez appeler ? "),
   ("Anfrage Alpinhost\\n","Alpinhost enquiry (FR)\\n"),("\\nTelefon: ","\\nPhone: "),("\\nOrt: ","\\nLocation: "),("\\nZimmer: ","\\nRooms: "),("\\nPaket: ","\\nPackage: "),("\\nNachricht: ","\\nMessage: ")],
 "it": [("Wird gesendet …","Invio in corso …"),("<b>Danke, Ihre Anfrage ist bei uns.</b> Wir melden uns am selben Werktag.","<b>Grazie, abbiamo ricevuto la Sua richiesta.</b> La ricontattiamo in giornata."),('btn.textContent="Gesendet"','btn.textContent="Inviato"'),("Das Senden hat nicht geklappt. Bitte ","L’invio non è riuscito. La preghiamo di "),(">per WhatsApp senden</a> oder an ",">inviare via WhatsApp</a> o di scrivere a "),("</a> schreiben.","</a>."),("Persönliche Schätzung","Stima personalizzata"),("Für Ihren Ort rechnen wir mit echten Vergleichswohnungen aus der Nachbarschaft, kostenlos. ","Per la Sua località calcoliamo gratuitamente con veri appartamenti comparabili della zona. "),(">Wohnung prüfen lassen</a>",">Far valutare l'appartamento</a>"),
   ("<span>Auslastung ","<span>Occupazione "),("Gebuchte Nächte pro Jahr","Notti prenotate all'anno"),("Nachtpreis im Schnitt","Prezzo medio per notte"),("Umsatz pro Jahr","Ricavi annui"),("Plattformgebühr 15,5 %","Commissione piattaforma 15,5 %"),("<span>Provision ","<span>Provvigione "),("Bleibt bei Ihnen pro Jahr","Le rimane all'anno"),(" <small>pro Monat</small>"," <small>al mese</small>"),
   ('"Basis: "+r.n','"Base: "+r.n'),(" aktive Airbnb-Inserate in "," annunci Airbnb attivi a "),(", Ø Nachtpreis ",", prezzo medio per notte "),(", Ø Auslastung ",", occupazione media "),('"Basis: Durchschnitt der Airbnb-Inserate in der Zentralschweiz, Ø Nachtpreis "','"Base: media degli annunci Airbnb nella Svizzera centrale, prezzo medio per notte "'),
   ('b.textContent="Kopiert"','b.textContent="Copiato"'),('b.textContent="Kopieren"','b.textContent="Copia"'),('"Paket "+pkg+" wählen"','"Scegli il pacchetto "+pkg'),
   ("Bitte Name, Telefon und Ort der Wohnung ausfüllen.","Inserisca nome, telefono e località dell'appartamento."),("Ihre Anfrage ist vorbereitet. ","La Sua richiesta è pronta. "),("In WhatsApp öffnen und senden","Apri e invia in WhatsApp"),(". Lieber anrufen? ",". Preferisce chiamare? "),
   ("Anfrage Alpinhost\\n","Alpinhost enquiry (IT)\\n"),("\\nTelefon: ","\\nPhone: "),("\\nOrt: ","\\nLocation: "),("\\nZimmer: ","\\nRooms: "),("\\nPaket: ","\\nPackage: "),("\\nNachricht: ","\\nMessage: ")],
 "es": [("Wird gesendet …","Enviando …"),("<b>Danke, Ihre Anfrage ist bei uns.</b> Wir melden uns am selben Werktag.","<b>Gracias, hemos recibido su consulta.</b> Le contestamos el mismo día laborable."),('btn.textContent="Gesendet"','btn.textContent="Enviado"'),("Das Senden hat nicht geklappt. Bitte ","El envío no ha funcionado. Por favor, "),(">per WhatsApp senden</a> oder an ",">envíe por WhatsApp</a> o escriba a "),("</a> schreiben.","</a>."),("Persönliche Schätzung","Estimación personalizada"),("Für Ihren Ort rechnen wir mit echten Vergleichswohnungen aus der Nachbarschaft, kostenlos. ","Para su ubicación calculamos gratis con apartamentos comparables reales de la zona. "),(">Wohnung prüfen lassen</a>",">Evaluar mi apartamento</a>"),
   ("<span>Auslastung ","<span>Ocupación "),("Gebuchte Nächte pro Jahr","Noches reservadas al año"),("Nachtpreis im Schnitt","Precio medio por noche"),("Umsatz pro Jahr","Ingresos al año"),("Plattformgebühr 15,5 %","Comisión de la plataforma 15,5 %"),("<span>Provision ","<span>Comisión "),("Bleibt bei Ihnen pro Jahr","Le queda al año"),(" <small>pro Monat</small>"," <small>al mes</small>"),
   ('"Basis: "+r.n','"Base: "+r.n'),(" aktive Airbnb-Inserate in "," anuncios activos de Airbnb en "),(", Ø Nachtpreis ",", precio medio por noche "),(", Ø Auslastung ",", ocupación media "),('"Basis: Durchschnitt der Airbnb-Inserate in der Zentralschweiz, Ø Nachtpreis "','"Base: media de los anuncios de Airbnb en Suiza central, precio medio por noche "'),
   ('b.textContent="Kopiert"','b.textContent="Copiado"'),('b.textContent="Kopieren"','b.textContent="Copiar"'),('"Paket "+pkg+" wählen"','"Elegir el paquete "+pkg'),
   ("Bitte Name, Telefon und Ort der Wohnung ausfüllen.","Indique nombre, teléfono y ubicación del apartamento."),("Ihre Anfrage ist vorbereitet. ","Su consulta está lista. "),("In WhatsApp öffnen und senden","Abrir y enviar en WhatsApp"),(". Lieber anrufen? ",". ¿Prefiere llamar? "),
   ("Anfrage Alpinhost\\n","Alpinhost enquiry (ES)\\n"),("\\nTelefon: ","\\nPhone: "),("\\nOrt: ","\\nLocation: "),("\\nZimmer: ","\\nRooms: "),("\\nPaket: ","\\nPackage: "),("\\nNachricht: ","\\nMessage: ")],
}
def build_js():
    js = open("site/assets/site.js", encoding="utf-8").read()
    vers = {}
    for lang in LANGS:
        j = js
        for a, b in sorted(JS_TR[lang], key=lambda x: -len(x[0])):
            assert a in j, (lang, a)
            j = j.replace(a, b.replace("'", "’"))
        j = re.sub(r'name:"([^"]+)"', lambda m: 'name:"%s"' % (T[m.group(1)][lang].replace('"', '”') if m.group(1) in T else m.group(1)), j)
        open(f"site/assets/site.{lang}.js", "w", encoding="utf-8").write(j)
        vers[lang] = hashlib.md5(j.encode()).hexdigest()[:8]
    return vers

# ---------- Seiten
PAGES = {"/": "index.html", "/impressum/": "impressum/index.html", "/datenschutz/": "datenschutz/index.html"}
for p in SLUG:
    if p.startswith("/airbnb-verwaltung-"): PAGES[p] = p.strip("/") + "/index.html"

def process(de_path, file, lang, jsv):
    html = open("site/" + file, encoding="utf-8").read()
    html = html.replace("<!--LANGSW-->", "")
    s = BeautifulSoup(html, "html.parser")
    indexable = de_path in INDEXABLE
    if lang != "de":
        for el in s.select("[data-de-only]"): el.decompose()
        translate_children(s.head, lang, de_path); translate_children(s.body, lang, de_path)
        for el in s.find_all(True):
            for a in ("alt","aria-label","title","placeholder","data-pkg"):
                if el.get(a) and has_text(el[a]):
                    t = norm(el[a])
                    if t in T: el[a] = T[t][lang]
                    else: MISSING.setdefault(t, "attr " + de_path)
        for m in s.find_all("meta"):
            if m.get("name") == "description" or m.get("property") in ("og:title", "og:description"):
                t = norm(m["content"])
                if t in T: m["content"] = T[t][lang]
                else: MISSING.setdefault(t, "meta " + de_path)
        for sc in s.find_all("script", type="application/ld+json"):
            sc.string = json.dumps(tr_json(json.loads(sc.string), lang), ensure_ascii=False)
        rewrite_links(s, de_path, lang)
        for sc in s.find_all("script", src=True):
            if "site.js" in sc["src"]: sc["src"] = f"/assets/site.{lang}.js?v={jsv[lang]}"
    btn = s.select_one("header.top .btn")
    btn.insert_before(BeautifulSoup(switcher(de_path, lang), "html.parser"))
    fix_head(s, de_path, lang, indexable)
    out = "<!doctype html>\n" + str(s).replace("<!DOCTYPE html>", "").replace("<!doctype html>", "").lstrip()
    target = "site" + lang_path(de_path, lang) + "index.html"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    jsv = build_js()
    for de_path, file in PAGES.items():
        for lang in LANGS: process(de_path, file, lang, jsv)
        process(de_path, file, "de", jsv)   # deutsche Seite zuletzt überschreiben (hreflang + Menü)
    # 404 ohne Platzhalter
    p404 = open("site/404.html", encoding="utf-8").read().replace("<!--LANGSW-->", "")
    open("site/404.html", "w", encoding="utf-8").write(p404)
    # Sitemap mit Alternates
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in INDEXABLE:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HTML_LANG[l]}" href="{DOMAIN}{lang_path(p, l)}"/>' for l in ALL) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{p}"/>'
        for l in ALL:
            sm.append(f'  <url><loc>{DOMAIN}{lang_path(p, l)}</loc><lastmod>{TODAY}</lastmod><priority>{"1.0" if p == "/" else "0.8"}</priority>{alts}</url>')
    for u in json.load(open("i18n/ratgeber_urls.json")):
        sm.append(f'  <url><loc>{DOMAIN}/{u}</loc><lastmod>{TODAY}</lastmod><priority>{"0.7" if u == "ratgeber/" else "0.6"}</priority></url>')
    sm.append("</urlset>")
    open("site/sitemap.xml", "w", encoding="utf-8").write("\n".join(sm) + "\n")
    # llms.txt ergänzen
    llms = open("site/llms.txt", encoding="utf-8").read()
    if "## Sprachen" not in llms:
        llms += "\n## Sprachen\n" + "".join(f"- {LABEL[l]}: {DOMAIN}{lang_path('/', l)}\n" for l in ALL)
        open("site/llms.txt", "w", encoding="utf-8").write(llms)
    print("missing", len(MISSING))
    for k, v in sorted(MISSING.items(), key=lambda x: x[1]): print(" ", v, "|", k)
