#!/usr/bin/env python3
"""Baut die statische Website alpinhost.ch aus src.html (Startseite) und Seitenvorlagen."""
import re, json, os, shutil, datetime

DOMAIN = "https://alpinhost.ch"
OUT = "site"
TODAY = datetime.date.today().isoformat()
PHONE = "+41 79 531 81 11"
WA = "41795318111"

src = open("src.html", encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
JS = re.search(r"<script>(.*?)</script>", src, re.S).group(1)

EXTRA_CSS = """
/* Hauptnavigation mit Unterreitern */
nav.main{align-items:center}
nav.main .mi{position:relative}
nav.main .mt{display:inline-flex;align-items:center;gap:5px;padding:10px 0}
nav.main .mt svg{width:11px;height:11px;transition:transform .15s}
nav.main .mi:hover .mt,nav.main .mi:focus-within .mt{color:var(--ink)}
nav.main .mi:hover .mt svg,nav.main .mi:focus-within .mt svg{transform:rotate(180deg)}
nav.main .sub{position:absolute;left:-16px;top:100%;padding-top:6px;visibility:hidden;opacity:0;transform:translateY(-4px);transition:opacity .12s,transform .12s,visibility 0s .12s;z-index:70}
nav.main .mi:hover .sub,nav.main .mi:focus-within .sub{visibility:visible;opacity:1;transform:none;transition:opacity .12s,transform .12s}
nav.main .mi.shut .sub{visibility:hidden;opacity:0}
nav.main .sub>div{background:var(--paper);border:1px solid var(--line);border-radius:12px;box-shadow:0 18px 44px rgba(15,34,48,.16);padding:8px;display:grid;min-width:230px;width:max-content;max-width:360px}
nav.main .sub a{padding:9px 12px;border-radius:8px;color:var(--ink);font-size:15px;line-height:1.3;font-weight:500}
nav.main .sub a:hover,nav.main .sub a:focus-visible{background:var(--mist,#EEF2F4);color:var(--lake)}
[id^="l-"],[id^="p-"],[id^="frage-"],.rg-cat[id]{scroll-margin-top:90px}

.top .wrap{flex-wrap:nowrap}
.crumbs{font-family:var(--mono);font-size:12.5px;color:var(--muted);padding-top:22px}
.crumbs a{color:var(--muted)}
.local-hero{padding-block:28px 10px}
.local-hero .hero-grid{align-items:start}
.local-hero h1{font-size:clamp(36px,5vw,60px);font-weight:800;letter-spacing:-.03em}
.prose{display:grid;gap:16px;max-width:68ch}
.prose p{color:var(--muted)}
.prose h2{font-size:clamp(26px,3vw,34px);margin-top:18px}
.prose ul{margin:0;padding-left:20px;color:var(--muted);display:grid;gap:6px}
.twocol{display:grid;grid-template-columns:1.3fr 1fr;gap:44px;align-items:start}
@media (max-width:900px){.twocol{grid-template-columns:1fr}}
.sidecard{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);padding:24px;display:grid;gap:12px;position:sticky;top:calc(env(safe-area-inset-top,0px) + 90px)}
.sidecard .price-mini{display:flex;justify-content:space-between;font-family:var(--mono);font-size:14px;border-bottom:1px solid var(--line);padding:8px 0}
.region a.more{font-weight:600;color:var(--lake);text-decoration:none;font-size:15px}
.region a.cover{display:block;text-decoration:none;color:inherit}
.region:hover h3{color:var(--lake)}
.places a{color:inherit}
.tt-wrap{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:24px;align-items:stretch}
.tt-wrap>div{min-width:0}
.tt-photo{border-radius:8px;overflow:hidden;position:relative;min-height:240px}
.tt-photo img{width:100%;height:100%;object-fit:cover;display:block;position:absolute;inset:0}
.tt-photo figcaption{position:absolute;left:10px;bottom:10px;font-family:var(--mono);font-size:11.5px;background:rgba(10,20,28,.62);color:#fff;padding:5px 9px;border-radius:6px}
@media (max-width:900px){.tt-wrap{grid-template-columns:1fr}.tt-photo{min-height:220px}}
.footlinks{display:grid;gap:4px}
.footlinks a{color:var(--muted);text-decoration:none}
.footlinks a:hover{color:var(--ink)}
.legal .prose{max-width:72ch}
.prose>*{min-width:0}
.prose h3{font-size:20px;margin-top:6px}
.prose a{color:var(--lake)}
.prose ol{margin:0;padding-left:22px;color:var(--muted);display:grid;gap:6px}
.art-head{padding-block:22px 0}
.art-head h1{font-size:clamp(32px,4.6vw,54px);font-weight:800;letter-spacing:-.03em;max-width:24ch;margin-top:14px}
.art-meta{font-family:var(--mono);font-size:12.5px;color:var(--muted);margin-top:16px}
.photo.art-hero{margin:26px 0 0;aspect-ratio:16/8;order:0}
@media (max-width:900px){.photo.art-hero{aspect-ratio:16/10}}
.art-credit{font-size:12.5px;color:var(--muted);margin-top:10px;max-width:90ch}
.art-credit a{color:inherit}
.keybox{background:var(--lake-soft);border-radius:var(--r);padding:20px 22px}
.keybox>b{display:block;font-family:var(--mono);font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--lake);margin-bottom:10px}
.keybox ul{color:var(--ink)}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r);background:var(--paper)}
.tbl table{border-collapse:collapse;width:100%;font-size:15px}
.tbl th,.tbl td{padding:10px 12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
.tbl th{font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:500}
.tbl .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.tbl tr:last-child td{border-bottom:0}
.swipe{display:none;font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
@media (max-width:620px){.swipe{display:block}.tbl.wide table{min-width:520px}.tbl th,.tbl td{padding:9px 10px}}
.note{font-size:14.5px;border-left:3px solid var(--glow);padding-left:14px}
.srcs{font-size:12.5px;line-height:1.6;color:var(--muted);padding-bottom:44px}
.srcs-h{font-family:var(--mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;margin:0}
.srcs ol{margin:6px 0 10px;padding-left:18px}
.srcs a{color:inherit;word-break:break-word}
.srcs p{margin:0}
footer .credits a{color:inherit;text-decoration:none}
footer .credits + .credits{border-top:0;padding-top:0;margin-top:-8px}
.occbar{width:90px;height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin-top:7px}
.occbar i{display:block;height:100%;background:var(--glow);border-radius:99px}
.rg-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
@media (max-width:1060px){.rg-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.rg-grid{grid-template-columns:1fr}}
.rg-cat{font-size:clamp(24px,3vw,32px);margin:44px 0 18px}
.rg-cat:first-child{margin-top:0}
.rg-card h3{font-size:19px;line-height:1.25}
.article .sidecard .btn{text-align:center;justify-content:center}
.langsw{position:relative;margin-left:0;flex:none}
@media (max-width:900px){.langsw{margin-left:auto}.top .btn{margin-left:0}}
@media (max-width:900px){.top .brand{margin-right:auto}}
.langsw summary{list-style:none;cursor:pointer;font-family:var(--mono);font-size:13px;font-weight:500;padding:8px 10px;border:1px solid var(--line);border-radius:8px;display:flex;align-items:center;gap:6px;color:var(--ink);background:var(--paper)}
.langsw summary::-webkit-details-marker{display:none}
.langsw summary svg{width:10px;height:10px}
.langsw[open] summary{border-color:var(--ink)}
.langsw .menu{position:absolute;right:0;top:calc(100% + 6px);background:var(--paper);border:1px solid var(--line);border-radius:10px;box-shadow:0 14px 40px rgba(15,34,48,.16);padding:6px;display:grid;min-width:150px;z-index:60}
.langsw .menu a{display:flex;justify-content:space-between;gap:14px;padding:9px 12px;border-radius:7px;text-decoration:none;color:var(--ink);font-size:15px}
.langsw .menu a span{font-family:var(--mono);font-size:12px;color:var(--muted)}
.langsw .menu a:hover,.langsw .menu a[aria-current]{background:var(--mist,#EEF2F4)}
@media (max-width:520px){.brand small{display:none}.top .wrap{gap:12px}}
@media (max-width:420px){.langsw summary{padding:7px 8px}}
@media (max-width:360px){.top .wrap{gap:8px}.top .btn{padding-inline:12px;font-size:14px}.brand{gap:8px}.brand .mark{width:32px;height:32px}.langsw summary{padding:6px 7px;font-size:12px}}
"""

def img(name, alt, w800=True, cls="", sizes="(max-width: 900px) 100vw, 50vw", root="", eager=False, wh=(1600, 1067)):
    s = f'{root}img/{name}-800.webp'
    big = f'{root}img/{name}-1600.webp'
    srcset = f'{s} 800w, {big} 1600w' if os.path.exists(os.path.join(OUT, "img", f"{name}-1600.webp")) else f'{s} 800w'
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="{s}" srcset="{srcset}" sizes="{sizes}" alt="{alt}" width="{wh[0]}" height="{wh[1]}" {load} decoding="async"{(" class=%s" % cls) if cls else ""}>'

REGIONS = {
 "grindelwald": dict(
   slug="airbnb-verwaltung-grindelwald", name="Grindelwald",
   title="Airbnb-Verwaltung Grindelwald | Wohnung vermieten | Alpinhost",
   desc="Wir vermieten und betreuen Ihre Ferienwohnung in Grindelwald auf Airbnb und Booking.com. Vor Ort im Dorf. 18 % oder 21 %, keine Einrichtungsgebühr.",
   h1="Airbnb-Verwaltung in Grindelwald",
   lead="Wir wohnen in Grindelwald und kümmern uns um Ihre Ferienwohnung, als wäre es unsere eigene: Inserat, Preise, Gäste, Reinigung und Abrechnung.",
   photo=("grindelwald-eiger", "Chalets im Dorf Grindelwald, dahinter der Eiger", (1600,1068)),
   photo2=("grindelwald-winter", "Tief verschneite Holzhütten bei Grindelwald im Winter", (1600,1200)),
   body=[
     ("Ein Dorf mit zwei Hochsaisons", "Grindelwald ist im Sommer und im Winter gefragt. Im Sommer kommen Wanderer, Familien und Gäste, die zum Jungfraujoch oder auf First wollen. Im Winter sind es Skifahrer, Schlittler und Gäste, die Schnee zum ersten Mal sehen. Dazwischen liegen ruhigere Wochen im Frühling und Spätherbst. Genau dort entscheidet die Preisstrategie, ob die Wohnung leer steht oder gebucht ist."),
     ("Gäste aus der ganzen Welt", "Viele Gäste in Grindelwald reisen aus Asien, Amerika und den Golfstaaten an. Sie schreiben auf Englisch, oft spät abends nach Schweizer Zeit, und haben Fragen zu Bahnen, Wetter und Gepäck. Wir antworten schnell und kennen die Antworten, weil wir selbst hier leben."),
     ("Vor Ort, wenn es zählt", "Ein Gast findet den Schlüssel nicht, die Heizung streikt oder im Winter liegt Schnee vor der Tür: In Grindelwald sind wir in kurzer Zeit selbst in der Wohnung. Reinigung und Kontrolle laufen über unser Team im Dorf."),
     ("Erlebnisse für Ihre Gäste", "Unsere Gäste in der Jungfrau Region bekommen Tipps und buchbare Erlebnisse über Grindelwald Experiences, vom Gleitschirmflug bis zum Schlitteln. Zufriedene Gäste schreiben bessere Bewertungen, und gute Bewertungen bringen höhere Preise."),
   ],
   places=["Grindelwald Dorf","Grund","Terrassenweg","Bussalp","Grindelwald-First","Wargistal"],
 ),
 "interlaken": dict(
   slug="airbnb-verwaltung-interlaken", name="Interlaken",
   title="Airbnb-Verwaltung Interlaken | Wohnung vermieten | Alpinhost",
   desc="Ferienwohnung in Interlaken, Wilderswil oder am Brienzersee professionell vermieten. Airbnb und Booking.com, Reinigung, Gäste. 18 % oder 21 %.",
   h1="Airbnb-Verwaltung in Interlaken",
   lead="Interlaken ist das Tor zur Jungfrau Region. Wir vermieten Ihre Wohnung an die Gäste, die von hier aus die Berge entdecken, und kümmern uns um alles dazwischen.",
   photo=("interlaken-harder-kulm", "Blick vom Harder Kulm auf Interlaken, den Thunersee und die Berge", (1600,1067)),
   photo2=None,
   body=[
     ("Ganzjährig gefragt", "Interlaken lebt von Gästen, die nur wenige Nächte bleiben und weiterreisen. Viele kommen per Bahn an und suchen eine Unterkunft nahe beim Bahnhof West oder Ost. Kurze Aufenthalte heissen viele Wechsel. Das verlangt eine zuverlässige Reinigung und einen Check-in, der ohne Schlüsselübergabe funktioniert."),
     ("Internationale Gäste", "Gäste aus Indien, den Golfstaaten, Korea und Amerika prägen Interlaken. Familien suchen grössere Wohnungen, Paare kleine Studios. Wir schreiben das Inserat so, dass es genau diese Gäste anspricht, und beantworten Anfragen rund um die Uhr."),
     ("Kurze Wege", "Von Grindelwald sind wir rasch in Interlaken, Wilderswil, Matten oder Unterseen. Reinigung und Kontrolle nach jedem Wechsel laufen über unser Team in der Region."),
   ],
   places=["Interlaken","Unterseen","Matten","Wilderswil","Bönigen","Ringgenberg"],
 ),
 "lauterbrunnen": dict(
   slug="airbnb-verwaltung-lauterbrunnen-wengen-muerren", name="Lauterbrunnen, Wengen und Mürren",
   title="Airbnb-Verwaltung Lauterbrunnen, Wengen, Mürren | Alpinhost",
   desc="Ferienwohnung in Lauterbrunnen, Wengen oder Mürren vermieten lassen. Wir kennen die autofreien Bergdörfer und betreuen Ihre Gäste von Anreise bis Abreise.",
   h1="Airbnb-Verwaltung in Lauterbrunnen, Wengen und Mürren",
   lead="Ein Tal mit Wasserfällen und zwei autofreie Bergdörfer. Hier braucht die Vermietung jemanden, der die Wege kennt.",
   photo=("lauterbrunnental", "Lauterbrunnental mit steilen Felswänden, dahinter verschneite Gipfel", (1600,1076)),
   photo2=("wengen-winter", "Das Dorf Wengen im Winter, umgeben von verschneiten Wiesen und Wald", (1600,1067)),
   body=[
     ("Autofrei heisst gut erklärt", "Wengen und Mürren erreichen Gäste nur mit Bahn oder Seilbahn. Wer das nicht weiss, steht mit drei Koffern am Parkplatz in Lauterbrunnen oder Stechelberg. Wir schicken jedem Gast vor der Anreise eine klare Wegbeschreibung mit Fahrplan, Gepäcktipps und dem Code für die Schlüsselbox."),
     ("Sommer im Tal, Winter auf dem Berg", "Lauterbrunnen ist im Sommer stark gebucht, Wengen und Mürren zusätzlich im Winter mit dem Skigebiet. Wir planen Preise und Mindestaufenthalte für beide Saisons getrennt."),
     ("Reinigung trotz langer Wege", "Ein Wechsel in Mürren dauert länger als im Tal. Wir planen die Reinigung so, dass das Team die Bahnzeiten einhält und die Wohnung pünktlich bereit ist."),
   ],
   places=["Lauterbrunnen","Wengen","Mürren","Gimmelwald","Stechelberg","Isenfluh"],
 ),
 "luzern": dict(
   slug="airbnb-verwaltung-luzern", name="Luzern und Innerschweiz",
   title="Airbnb-Verwaltung Luzern | Ferienwohnung vermieten | Alpinhost",
   desc="Ferienwohnung in Luzern, Weggis, Vitznau oder Engelberg vermieten lassen. Vor Ort in Luzern. Airbnb, Booking.com, Reinigung und Gäste aus einer Hand.",
   h1="Airbnb-Verwaltung in Luzern und der Innerschweiz",
   lead="Wir wohnen in Luzern und betreuen Wohnungen in der Stadt, am Vierwaldstättersee und in den Bergen der Innerschweiz.",
   photo=("luzern-kapellbruecke", "Kapellbrücke und Wasserturm in Luzern an der Reuss", (1600,1067)),
   photo2=("weggis-vierwaldstaettersee", "Wohnhäuser in Weggis am Ufer des Vierwaldstättersees", (1600,1054)),
   body=[
     ("Stadt, See und Berge", "Luzern verbindet Städtereisende, Geschäftsgäste und Feriengäste, die auf die Rigi, den Pilatus oder den Titlis wollen. Am See kommen Familien und Paare für längere Aufenthalte. Jede Lage braucht ein anderes Inserat und eine andere Preisstrategie."),
     ("Ferienwohnungen am See", "In Weggis, Vitznau und Gersau suchen Gäste Seesicht, Ruhe und eine gute Verbindung per Schiff. Wir zeigen genau das im Inserat und erklären die Anreise mit Schiff, Bahn oder Auto."),
     ("Vor Ort in Luzern", "Wir sind in Luzern zuhause. Reinigung, Kontrollen und kleine Reparaturen erledigen wir mit unserem Team in der Region, in der Stadt meist am selben Tag."),
   ],
   places=["Luzern","Kriens","Horw","Weggis","Vitznau","Gersau","Engelberg","Zug","Andermatt"],
 ),
 "bern": dict(
   slug="airbnb-verwaltung-bern", name="Bern",
   title="Airbnb-Verwaltung Bern | Wohnung vermieten | Alpinhost",
   desc="Wohnung in Bern oder Thun auf Airbnb und Booking.com vermieten lassen. Inserat, Preise, Gäste, Reinigung und Abrechnung. 18 % oder 21 %.",
   h1="Airbnb-Verwaltung in Bern",
   lead="Bern zieht Städtereisende, Geschäftsgäste und Besucher an, die von hier ins Berner Oberland fahren. Wir vermieten Ihre Wohnung an genau diese Gäste.",
   photo=("bern-altstadt-aare", "Altstadt von Bern mit Münster an der Aare", (1600,1063)),
   photo2=None,
   body=[
     ("Geschäftsgäste unter der Woche, Städtereisende am Wochenende", "In Bern sind Wohnungen unter der Woche oft von Geschäftsgästen gebucht, am Wochenende von Städtereisenden. Wir passen Preise und Mindestaufenthalte an diesen Rhythmus an, damit keine Lücken entstehen."),
     ("Saubere Wechsel, zuverlässig", "Geschäftsgäste erwarten eine Wohnung, die funktioniert: schnelles WLAN, ein Arbeitsplatz, frische Wäsche. Wir prüfen das bei jedem Wechsel mit Checkliste und Fotos."),
     ("Bern und Umgebung bis Thun", "Wir betreuen Wohnungen in der Stadt Bern und im Umland bis nach Thun und Spiez, am Tor zum Berner Oberland."),
   ],
   places=["Bern Altstadt","Länggasse","Breitenrain","Kirchenfeld","Köniz","Muri","Thun","Spiez"],
 ),
 "schweiz": dict(
   slug="airbnb-verwaltung-schweiz", name="ganze Schweiz",
   title="Airbnb-Verwaltung in der ganzen Schweiz | Alpinhost",
   desc="Ferienwohnung in der ganzen Schweiz professionell vermieten lassen. Inserat, Preise, Gäste und Abrechnung von uns, Reinigung über geprüfte Teams vor Ort.",
   h1="Airbnb-Verwaltung in der ganzen Schweiz",
   lead="Bergort, Stadt oder See: Wir führen Ihre Vermietung in jedem Kanton. Inserat, Preise, Gäste und Abrechnung von uns, Reinigung und Schlüssel über geprüfte Teams vor Ort.",
   photo=("grindelwald-fruehling", "Frühlingswiese mit Krokussen oberhalb von Grindelwald, dahinter Eiger und Wetterhorn", (1600,1067)),
   photo2=None,
   body=[
     ("So arbeiten wir ausserhalb unserer Regionen", "Zum Start besuchen wir die Wohnung, machen die Bestandesaufnahme und organisieren die Fotos. Danach arbeiten wir mit einem geprüften Reinigungsteam vor Ort, das nach unserer Checkliste reinigt und jede Kontrolle mit Fotos dokumentiert."),
     ("Was von uns kommt", "Inserat, tägliche Preisanpassung, Gästebetreuung rund um die Uhr, Koordination der Reinigung und der Monatsbericht kommen immer von uns, egal wo die Wohnung steht."),
     ("Vor Ort in drei Regionen", "In der Jungfrau Region, in Bern und in der Innerschweiz sind wir selbst vor Ort. Dort betreuen wir auch Wohnungen, bei denen öfter jemand vorbeischauen muss."),
   ],
   places=["Graubünden","Wallis","Tessin","Zürich","Ostschweiz","Westschweiz"],
 ),
}

exec(open("ratgeber.py", encoding="utf-8").read())

def head(title, desc, path, root, schema_list, ogimg="img/og-grindelwald-eiger.jpg"):
    url = DOMAIN + "/" + path
    schemas = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema_list)
    return f"""<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="de-CH" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_CH">
<meta property="og:site_name" content="Alpinhost">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="theme-color" content="#0F2230">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;700;800&family=Figtree:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{root}assets/site.css?v={AV_CSS}">
{schemas}
"""

ORG = {
  "@context":"https://schema.org","@type":"ProfessionalService","@id":DOMAIN+"/#org",
  "name":"Alpinhost","url":DOMAIN+"/","telephone":PHONE.replace(" ",""),
  "description":"Ferienwohnungs-Management für Airbnb und Booking.com in der ganzen Schweiz. Vor Ort in der Jungfrau Region, in Bern und in der Innerschweiz.",
  "image":DOMAIN+"/img/grindelwald-eiger-1600.webp","logo":DOMAIN+"/favicon.svg",
  "email":"info@alpinhost.ch",
  "parentOrganization":{"@type":"Organization","name":"R&B Digital Market KlG","address":{"@type":"PostalAddress","streetAddress":"Kellerstrasse 29","postalCode":"6005","addressLocality":"Luzern","addressCountry":"CH"}},
  "areaServed":[{"@type":"Country","name":"Schweiz"},{"@type":"Place","name":"Jungfrau Region"},{"@type":"City","name":"Grindelwald"},{"@type":"City","name":"Interlaken"},{"@type":"City","name":"Lauterbrunnen"},{"@type":"City","name":"Wengen"},{"@type":"City","name":"Luzern"},{"@type":"City","name":"Bern"}],
  "knowsLanguage":["de","en","fr","it","es"],
  "makesOffer":[
    {"@type":"Offer","name":"Basis","description":"18 % vom Übernachtungsumsatz nach Plattformgebühr. Inserat, Preise, Gästebetreuung, Monatsbericht.","itemOffered":{"@type":"Service","name":"Airbnb-Verwaltung Basis"}},
    {"@type":"Offer","name":"Komplett","description":"21 % vom Übernachtungsumsatz nach Plattformgebühr. Alles inklusive Reinigung, Wäsche, Check-in und Kontrolle.","itemOffered":{"@type":"Service","name":"Airbnb-Verwaltung Komplett"}}
  ],
  "priceRange":"18 % – 21 % Provision"
}

FAQ_NAV = re.findall(r'<details id="(frage-\d+)"><summary>(.*?)</summary>', src)
def nav_html(root, home=False):
    """Hauptnavigation. Grosse Reiter mit Unterreitern, die beim Ueberfahren aufklappen."""
    a = lambda h: (h if home else f"{root}{h}")
    chev = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
    def group(label, href, items, extra=""):
        subs = "".join(f'<a href="{h}">{t}</a>' for t, h in items)
        return f'<div class="mi"{extra}><a class="mt" href="{href}">{label}{chev}</a><div class="sub"><div>{subs}</div></div></div>'
    leist = [("Inserat und Fotos","#l-inserat"),("Preise jeden Tag","#l-preise"),("Gäste rund um die Uhr","#l-gaeste"),("Check-in ohne Schlüsselübergabe","#l-checkin"),("Reinigung und Wäsche","#l-reinigung"),("Abrechnung und Bericht","#l-bericht")]
    preise = [("Basis 18 %","#p-basis"),("Komplett 21 %","#p-komplett"),("Eine Buchung, offen gerechnet.","#p-beispiel")]
    regs = [((r["name"][0].upper()+r["name"][1:]), f'{root}{r["slug"]}/') for r in REGIONS.values()]
    cats = []
    for art in ARTICLES:
        if art["cat"] not in cats: cats.append(art["cat"])
    rg = [(c, f'{root}ratgeber/#{rg_cat_id(c)}') for c in cats] + [("Alle Artikel", f'{root}ratgeber/')]
    return (group("Leistungen", a("#leistungen"), [(t, a(h)) for t, h in leist])
          + group("Preise", a("#preise"), [(t, a(h)) for t, h in preise])
          + f'<a class="mt" href="{a("#rechner")}">Rechner</a>'
          + group("Regionen", a("#regionen"), regs)
          + group("Fragen", a("#fragen"), [(t, a("#"+i)) for i, t in FAQ_NAV])
          + group("Ratgeber", f"{root}ratgeber/", rg, " data-de-only"))

def header(root, home=False):
    a = lambda h: (h if home else f"{root}{h}")
    return f"""<header class="top">
  <div class="wrap">
    <a class="brand" href="{root or './'}" aria-label="Alpinhost, Startseite">
      <svg class="mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="9" fill="var(--ink)"/><path d="M7 27 L16 13 L21 20 L25 15 L33 27 Z" fill="var(--snow)"/><path d="M7 31 H33" stroke="var(--lake)" stroke-width="2.4" stroke-linecap="round"/></svg>
      <span>Alpinhost<small>Ferienwohnungs-Management</small></span>
    </a>
    <nav class="main" aria-label="Hauptnavigation">
      {nav_html(root, home)}
    </nav>
    <!--LANGSW-->
    <a class="btn btn-primary" href="{a('#kontakt')}"><span class="long">Wohnung prüfen lassen</span><span class="short">Anfrage</span></a>
  </div>
</header>"""

def footer(root, credits=""):
    reg = "".join(f'<a href="{root}{r["slug"]}/">{"Airbnb-Verwaltung " + r["name"] if k!="schweiz" else "Airbnb-Verwaltung Schweiz"}</a>' for k, r in REGIONS.items())
    return f"""<footer>
  <div class="wrap">
    <div><b>Alpinhost</b><br>Ferienwohnungs-Management für Airbnb und Booking.com in der ganzen Schweiz.<br><br>WhatsApp und Telefon: {PHONE}<br>E-Mail: <a href="mailto:info@alpinhost.ch" style="color:inherit">info@alpinhost.ch</a></div>
    <div class="footlinks"><b>Regionen</b>{reg}</div>
    <div class="footlinks"><b>Unternehmen</b><a href="{root}#preise">Preise</a><a href="{root}#fragen">Fragen</a><a href="{root}ratgeber/" data-de-only>Ratgeber</a><a href="{root}impressum/">Impressum</a><a href="{root}datenschutz/">Datenschutz</a><span>Alpinhost ist eine Marke der R&amp;B Digital Market KlG</span><span style="margin-top:8px">Schwesterunternehmen</span><a href="https://grindelwaldexperiences.ch/" rel="noopener">Grindelwald Experiences</a><a href="https://www.jungfrauflights.com/" rel="noopener">Jungfrau Flights</a></div>
    <p class="credits">Fotos: Wikimedia Commons. Grindelwald mit Eiger und Kapellbrücke Luzern: Leonhard Lenz, CC0 · Frühling über Grindelwald: Speedy Füllemann, CC BY 3.0 · Winter bei Grindelwald: Robert Campbell KOR, CC BY 2.0 · Bern Altstadt: August Geyler, CC BY-SA 4.0 · Weggis: Arkelin, CC BY 4.0 · Interlaken vom Harder Kulm: Ank Kumar, CC BY-SA 4.0 · Lauterbrunnental: Chensiyuan, CC BY-SA 4.0 · Wengen im Winter: Jpatokal, CC BY-SA 4.0 · Schlüsselbox: Brainy J, CC0. Marktdaten: GuestFavorites, November 2025 bis Oktober 2026.</p>{f'<p class="credits" data-de-only>{credits}</p>' if credits else ""}
  </div>
</footer>"""

MODAL = src[src.index('<div class="modal" id="pkgmodal"'):src.index('<footer>')].strip()

def page_shell(headhtml, body, root, home=False, credits=""):
    return f"""<!doctype html>
<html lang="de-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{headhtml}</head>
<body>
{header(root, home)}
{body}
{MODAL}
{footer(root, credits)}
<script src="{root}assets/site.js?v={AV_JS}" defer></script>
</body>
</html>
"""

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

# ---------- assets
os.makedirs(OUT + "/assets", exist_ok=True)
open(OUT + "/assets/site.css", "w").write(CSS + EXTRA_CSS)
JS_SAFE = JS.replace('document.getElementById("calcform").addEventListener("change", calc);\n  calc();',
  'var cf=document.getElementById("calcform"); if(cf){ cf.addEventListener("change", calc); calc(); }')
JS_SAFE = JS_SAFE.replace('  var f = document.getElementById("leadform");\n  f.addEventListener(', '  var f = document.getElementById("leadform");\n  if (f) f.addEventListener(')
JS_SAFE += """
(function(){
  var ms=document.querySelectorAll("nav.main .mi");
  ms.forEach(function(m){
    var cx=0, cy=0;
    function mv(e){ if(Math.abs(e.clientX-cx)+Math.abs(e.clientY-cy)<8) return; var t=m.querySelector(".mt"); if(t&&t.matches(":hover")) return; m.classList.remove("shut"); document.removeEventListener("mousemove",mv); }
    m.addEventListener("click",function(e){ if(e.target.closest(".sub a")){ cx=e.clientX; cy=e.clientY; m.classList.add("shut"); if(document.activeElement) document.activeElement.blur(); document.addEventListener("mousemove",mv); } });
    m.addEventListener("keydown",function(e){ if(e.key==="Escape"){ m.classList.add("shut"); var t=m.querySelector(".mt"); if(t) t.focus(); } });
    m.addEventListener("focusout",function(e){ if(!m.contains(e.relatedTarget)&&!m.matches(":hover")) m.classList.remove("shut"); });
  });
  function openFaq(){ var h=location.hash.slice(1); if(!/^frage-\\d+$/.test(h)) return; var d=document.getElementById(h); if(d&&d.tagName==="DETAILS"){ d.open=true; d.scrollIntoView({block:"start"}); } }
  window.addEventListener("hashchange",openFaq); openFaq();
})();
"""
open(OUT + "/assets/site.js", "w").write(JS_SAFE)
import hashlib
AV_CSS = hashlib.md5((CSS + EXTRA_CSS).encode()).hexdigest()[:8]
AV_JS = hashlib.md5(JS_SAFE.encode()).hexdigest()[:8]
open(OUT + "/favicon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#0F2230"/><path d="M7 27 L16 13 L21 20 L25 15 L33 27 Z" fill="#F2F5F6"/><path d="M7 31 H33" stroke="#1C5E74" stroke-width="2.4" stroke-linecap="round"/></svg>')

# ---------- home
body = re.search(r"</header>(.*?)<div class=\"modal\" id=\"pkgmodal\"", src, re.S).group(1)
body = body.replace('<img src="{{HERO}}" alt="Chalets im Dorf Grindelwald, dahinter der Eiger" width="1600" height="1068">',
                    img("grindelwald-eiger", "Chalets im Dorf Grindelwald, dahinter der Eiger", eager=True, wh=(1600,1068)))
body = body.replace('<img src="{{WINTER}}" alt="Tief verschneite Holzhütten bei Grindelwald im Winter" width="900" height="675">',
                    img("grindelwald-winter", "Tief verschneite Holzhütten bei Grindelwald im Winter", wh=(1600,1200)))
# regions: photos + links
reg_start = body.index('<div class="regions">'); reg_end = body.index('</div>\n  </div>\n</section>', reg_start)
def card(key, pill, h3, text, places, photo):
    r = REGIONS[key]
    return f"""      <article class="region">
        <a class="cover" href="{r['slug']}/" aria-label="{h3}"><div class="img">{img(photo[0], photo[1], sizes="(max-width: 620px) 100vw, (max-width: 1060px) 50vw, 25vw", wh=photo[2])}</div></a>
        <div class="txt">
          <span class="pill{' alt' if pill!='Vor Ort' else ''}">{pill}</span>
          <h3><a href="{r['slug']}/" style="text-decoration:none;color:inherit">{h3}</a></h3>
          <p>{text}</p>
          <p class="places">{places}</p>
          <a class="more" href="{r['slug']}/">{ {"schweiz":"Mehr zur ganzen Schweiz","grindelwald":"Mehr zur Jungfrau Region","luzern":"Mehr zur Innerschweiz"}.get(key, "Mehr zu " + h3) } →</a>
        </div>
      </article>
"""
cards = '<div class="regions">\n' + \
  card("grindelwald","Vor Ort","Jungfrau Region","Unser Zuhause. Ganzjährige Nachfrage, Sommer und Winter. Gäste aus der ganzen Welt, viele aus Asien, Amerika und den Golfstaaten.",
       '<a href="airbnb-verwaltung-grindelwald/">Grindelwald</a> · <a href="airbnb-verwaltung-lauterbrunnen-wengen-muerren/">Wengen</a> · <a href="airbnb-verwaltung-lauterbrunnen-wengen-muerren/">Mürren</a> · <a href="airbnb-verwaltung-lauterbrunnen-wengen-muerren/">Lauterbrunnen</a> · <a href="airbnb-verwaltung-interlaken/">Interlaken</a>',
       ("grindelwald-fruehling","Frühlingswiese mit Krokussen oberhalb von Grindelwald, dahinter Eiger und Wetterhorn",(1600,1067))) + \
  card("bern","Vor Ort","Bern","Stadtwohnungen für Geschäfts- und Städtereisende, dazu das Umland bis Thun.","Bern · Köniz · Muri · Ostermundigen · Thun · Spiez",
       ("bern-altstadt-aare","Altstadt von Bern mit Münster an der Aare",(1600,1063))) + \
  card("luzern","Vor Ort","Innerschweiz","Stadtwohnungen in Luzern und Ferienwohnungen am See und in den Bergen.","Luzern · Weggis · Vitznau · Engelberg · Zug · Andermatt",
       ("luzern-kapellbruecke","Kapellbrücke und Wasserturm in Luzern an der Reuss",(1600,1067))) + \
  card("schweiz","Mit Partnern","Ganze Schweiz","Wir besuchen die Wohnung zum Start und arbeiten danach mit einem geprüften Team vor Ort.","In allen Kantonen",
       ("weggis-vierwaldstaettersee","Wohnhäuser in Weggis am Ufer des Vierwaldstättersees",(1600,1054)))
body = body[:reg_start] + cards + "    " + body[reg_end:]
# timetable with lockbox photo
tt_start = body.index('<div class="timetable">')
tt_end = body.index('</div>\n    </div>\n  </div>\n</section>', tt_start) + len('</div>\n    </div>')
tt = body[tt_start:tt_end]
tt_new = '<div class="timetable"><div class="tt-wrap"><div>' + tt[len('<div class="timetable">'):-len('</div>')] + \
  f'</div><figure class="tt-photo" style="margin:0">{img("schluesselbox","Geöffnete Schlüsselbox mit Wohnungsschlüssel und Zahlenschloss", sizes="(max-width: 900px) 100vw, 30vw", wh=(1600,1323))}<figcaption>Check-in mit Schlüsselbox</figcaption></figure></div></div>'
body = body[:tt_start] + tt_new + body[tt_end:]
body = body.replace('<section class="block" id="fragen"', rg_home_teaser() + '<section class="block" id="fragen"', 1)
assert "{{" not in body, "placeholder left"

faqs = re.findall(r'<details(?: id="[^"]*")?><summary>(.*?)</summary><div class="ans">(.*?)</div></details>', body, re.S)
assert len(faqs) >= 6, "FAQ der Startseite nicht gefunden"
FAQ = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub("<[^>]+>","",a)}} for q,a in faqs]}
WEB = {"@context":"https://schema.org","@type":"WebSite","name":"Alpinhost","url":DOMAIN+"/","inLanguage":"de-CH","publisher":{"@id":DOMAIN+"/#org"}}
home_title = "Airbnb-Verwaltung Schweiz – Ferienwohnung vermieten | Alpinhost"
home_desc = "Wir vermieten und betreuen Ihre Ferienwohnung auf Airbnb und Booking.com. Ganze Schweiz, vor Ort in Jungfrau Region, Bern und Innerschweiz. 18 % oder 21 %."
write("index.html", page_shell(head(home_title, home_desc, "", "", [ORG, WEB, FAQ]), body, "", home=True, credits=RG_HOME_CREDITS))

# ---------- region pages
for key, r in REGIONS.items():
    root = "../"
    url = f'{r["slug"]}/'
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Alpinhost","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":r["h1"],"item":DOMAIN+"/"+url}]}
    svc = {"@context":"https://schema.org","@type":"Service","name":r["h1"],"serviceType":"Ferienwohnungs-Management, Airbnb-Verwaltung",
           "provider":{"@id":DOMAIN+"/#org"},"areaServed":{"@type":"Place","name":r["name"]},"url":DOMAIN+"/"+url,
           "offers":[{"@type":"Offer","name":"Basis","description":"18 % vom Übernachtungsumsatz nach Plattformgebühr"},{"@type":"Offer","name":"Komplett","description":"21 % vom Übernachtungsumsatz nach Plattformgebühr"}]}
    secs = "".join(f"<h2>{h}</h2><p>{t}</p>" for h, t in r["body"])
    p2 = ""
    if r["photo2"]:
        p2 = f'<figure class="photo" style="margin:8px 0 0;aspect-ratio:16/10">{img(r["photo2"][0], r["photo2"][1], root=root, wh=r["photo2"][2])}</figure>'
    places = " · ".join(r["places"])
    others = " · ".join(f'<a href="{root}{o["slug"]}/">{"Ganze Schweiz" if k2=="schweiz" else o["name"]}</a>' for k2, o in REGIONS.items() if k2 != key)
    rg_html, rg_cred = rg_region_block(key, root)
    b = f"""<main>
<div class="wrap crumbs"><a href="{root}">Alpinhost</a> › {r['h1']}</div>
<section class="local-hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Airbnb- und Booking-Verwaltung · {r['name']}</p>
      <h1 style="margin-top:14px">{r['h1']}</h1>
      <p class="lead" style="margin-top:18px">{r['lead']}</p>
      <div class="terms num" aria-label="Konditionen auf einen Blick">
        <div><span>Provision</span><b>18 % oder 21 %</b></div>
        <div><span>Einrichtungsgebühr</span><b>CHF 0</b></div>
        <div><span>Bei Leerstand</span><b>CHF 0</b></div>
        <div><span>Kündigungsfrist</span><b>3 Monate</b></div>
      </div>
      <div class="cta-row"><a class="btn btn-primary" href="{root}#rechner">Ertrag berechnen</a><a class="btn btn-ghost" href="{root}#kontakt">Wohnung prüfen lassen</a></div>
    </div>
    <figure class="photo" style="margin:0">{img(r['photo'][0], r['photo'][1], root=root, eager=True, wh=r['photo'][2])}<figcaption>{r['photo'][1]}</figcaption></figure>
  </div>
</section>
<section class="block" style="padding-top:40px">
  <div class="wrap twocol">
    <div class="prose">{secs}{p2}
      <h2>Wo wir arbeiten</h2><p class="places">{places}</p>
      <h2>Weitere Regionen</h2><p class="places">{others}</p>
    </div>
    <aside class="sidecard">
      <p class="eyebrow">Konditionen</p>
      <div class="price-mini"><span>Basis</span><b>18 %</b></div>
      <div class="price-mini"><span>Komplett, inkl. Reinigung</span><b>21 %</b></div>
      <div class="price-mini"><span>Einrichtungsgebühr</span><b>CHF 0</b></div>
      <div class="price-mini"><span>Kündigungsfrist</span><b>3 Monate</b></div>
      <p style="color:var(--muted);font-size:14.5px">Gerechnet auf den Übernachtungsumsatz nach Plattformgebühr. Bei Leerstand zahlen Sie nichts.</p>
      <a class="btn btn-primary" href="{root}#kontakt">Kostenlos prüfen lassen</a>
      <p style="font-size:14px;color:var(--muted)">WhatsApp und Telefon: <b style="white-space:nowrap">{PHONE}</b><br>E-Mail: <a href="mailto:info@alpinhost.ch" style="color:inherit;font-weight:600">info@alpinhost.ch</a></p>
    </aside>
  </div>
</section>
{rg_html}</main>"""
    write(url + "index.html", page_shell(head(r["title"], r["desc"], url, root, [ORG, crumbs, svc], ogimg=f"img/og-{r['photo'][0]}.jpg"), b, root, credits=rg_cred))

# ---------- legal
def legal(slug, title, h1, html):
    root = "../"
    b = f'<main class="legal"><div class="wrap crumbs"><a href="{root}">Alpinhost</a> › {h1}</div><section class="block" style="padding-top:30px"><div class="wrap prose"><h1 style="font-size:clamp(32px,4vw,46px)">{h1}</h1>{html}</div></section></main>'
    h = head(title, f"{h1} von Alpinhost, Ferienwohnungs-Management Schweiz.", slug + "/", root, [ORG]).replace('<meta name="description"', '<meta name="robots" content="noindex, follow">\n<meta name="description"')
    write(slug + "/index.html", page_shell(h, b, root))

legal("impressum", "Impressum | Alpinhost", "Impressum",
 f"""<p><b>Alpinhost</b> ist eine Marke der</p><p>R&amp;B Digital Market KlG<br>Kellerstrasse 29<br>6005 Luzern<br>Schweiz</p>
<p>WhatsApp und Telefon: {PHONE}<br>E-Mail: <a href="mailto:info@alpinhost.ch">info@alpinhost.ch</a></p>
<h2>Haftung</h2><p>Die Angaben auf dieser Website wurden sorgfältig erstellt. Ertragsschätzungen sind unverbindlich und stellen keine Garantie dar.</p>
<h2>Bildnachweis</h2><p>Die Fotos stammen von Wikimedia Commons. Die Urheber und Lizenzen sind in der Fusszeile jeder Seite aufgeführt.</p>""")

legal("datenschutz", "Datenschutz | Alpinhost", "Datenschutzerklärung",
 """<p>Wir nehmen den Schutz Ihrer Daten ernst und bearbeiten Personendaten nach dem Schweizer Datenschutzgesetz (DSG).</p>
<h2>Verantwortlich</h2><p>R&amp;B Digital Market KlG, Marke Alpinhost, Kellerstrasse 29, 6005 Luzern. Kontakt: <a href="mailto:info@alpinhost.ch">info@alpinhost.ch</a> oder WhatsApp wie im Impressum angegeben.</p>
<h2>Anfragen</h2><p>Wenn Sie das Formular absenden, erhalten wir Ihre Angaben per E-Mail. Für die Übermittlung nutzen wir den Dienst FormSubmit, der die Angaben an unser Postfach weiterleitet. Wählen Sie WhatsApp, wird Ihre Nachricht in WhatsApp vorbereitet und erst gesendet, wenn Sie selbst auf Senden tippen. Wir verwenden Ihre Angaben nur, um Ihre Anfrage zu beantworten.</p>
<h2>Keine Cookies, kein Tracking</h2><p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Werbedienste.</p>
<h2>Hosting und Schriften</h2><p>Beim Aufruf der Website verarbeitet unser Hosting-Anbieter technisch notwendige Daten wie die IP-Adresse. Die Schriften werden von Google Fonts geladen. Dabei wird Ihre IP-Adresse an Google übermittelt.</p>
<h2>Ihre Rechte</h2><p>Sie können jederzeit Auskunft über Ihre bei uns gespeicherten Daten verlangen und deren Berichtigung oder Löschung beantragen.</p>""")

# ---------- 404
write("404.html", page_shell(head("Seite nicht gefunden | Alpinhost", "Diese Seite gibt es nicht.", "404.html", "/", [ORG]).replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"'),
  '<main><section class="block"><div class="wrap prose"><h1>Diese Seite gibt es nicht.</h1><p>Vielleicht hat sich die Adresse geändert. <a href="/">Zur Startseite</a></p></div></section></main>', "/"))

RG_URLS = build_ratgeber()

# ---------- sitemap, robots, llms, CNAME
urls = [""] + [r["slug"] + "/" for r in REGIONS.values()]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for u in urls:
    sm += f'  <url><loc>{DOMAIN}/{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{"1.0" if u=="" else "0.8"}</priority></url>\n'
sm += "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\n\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
llms = f"""# Alpinhost

> Alpinhost vermietet und betreut Ferienwohnungen auf Airbnb und Booking.com in der ganzen Schweiz. Vor Ort in der Jungfrau Region (Grindelwald, Interlaken, Lauterbrunnen, Wengen, Mürren), in Bern und in der Innerschweiz (Luzern, Vierwaldstättersee). Marke der R&B Digital Market KlG.

## Konditionen
- Basis: 18 % vom Übernachtungsumsatz nach Plattformgebühr (Inserat, Preise, Gästebetreuung, Monatsbericht)
- Komplett: 21 % (zusätzlich Reinigung, Wäsche, Check-in mit Schlüsselbox, Kontrolle, kleine Reparaturen)
- Keine Einrichtungsgebühr, keine Grundgebühr, bei Leerstand CHF 0, Kündigungsfrist 3 Monate
- Reinigung wird über die Reinigungsgebühr des Gastes gedeckt und im Komplett-Paket zum Selbstkostenpreis verrechnet
- Kontakt: WhatsApp und Telefon {PHONE}

## Seiten
- [Startseite]({DOMAIN}/)
""" + "".join(f"- [{r['h1']}]({DOMAIN}/{r['slug']}/)\n" for r in REGIONS.values()) + "\n## Ratgeber für Eigentümer\n" + f"- [Übersicht]({DOMAIN}/ratgeber/)\n" + "".join(f"- [{x['h1']}]({DOMAIN}/ratgeber/{x['slug']}/): {x['teaser']}\n" for x in ARTICLES)
write("llms.txt", llms)
write("CNAME", "alpinhost.ch\n")
write(".nojekyll", "")
print("built", len(urls), "indexable pages")
