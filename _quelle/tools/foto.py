#!/usr/bin/env python3
"""Fotos von Wikimedia Commons suchen und fuer die Website aufbereiten.

  python3 _quelle/tools/foto.py suchen "Lauterbrunnen Staubbachfall"
      -> listet Kandidaten (Titel, Groesse, Lizenz, Urheber) und speichert Vorschaubilder nach /tmp/foto-kandidaten/
         Vorschau IMMER ansehen: Das Bild muss genau zeigen, wovon der Text spricht.
  python3 _quelle/tools/foto.py holen "File:Genauer Titel.jpg" lauterbrunnen-staubbachfall
      -> laedt das Bild, schneidet auf 3:2, schreibt img/<name>-800.webp, img/<name>-1200.webp, img/<name>-1600.webp, img/og-<name>.jpg
         und traegt Urheber und Lizenz in _quelle/rg_img/meta.json ein.

Regeln: nur CC0, CC BY, CC BY-SA oder gemeinfrei. Querformat, mindestens 1600 px breit.
Wikimedia sperrt bei zu vielen Abrufen (HTTP 429): nur Standardbreiten laden, zwischen Downloads 25 s warten, nicht wiederholt probieren.
Keine Fotos erkennbarer Privatpersonen, keine Fotos bekannter Personen.
"""
import json, os, re, sys, time, urllib.parse, urllib.request
UA = {"User-Agent": "AlpinhostSiteBuilder/1.0 (https://alpinhost.ch; info@alpinhost.ch)"}
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
META = os.path.join(ROOT, "_quelle", "rg_img", "meta.json")
OKLIC = re.compile(r"(CC0|CC BY|Public domain|PD)")

def api(params):
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40))

def info(pages):
    out = []
    for p in sorted(pages, key=lambda x: x.get("index", 99)):
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        out.append({"title": p["title"], "w": ii["width"], "h": ii["height"],
                    "lic": m.get("LicenseShortName", {}).get("value", ""),
                    "author": re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()[:60],
                    "thumb": ii.get("thumburl", ""), "desc": ii["descriptionurl"]})
    return out

def suchen(q):
    r = api({"action": "query", "format": "json", "generator": "search", "gsrsearch": q + " filetype:bitmap", "gsrnamespace": 6,
             "gsrlimit": 20, "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 500})
    os.makedirs("/tmp/foto-kandidaten", exist_ok=True)
    n = 0
    for c in info(r.get("query", {}).get("pages", {}).values()):
        if c["w"] < 1600 or c["w"] < c["h"] * 1.2 or not OKLIC.match(c["lic"]): continue
        fn = f"/tmp/foto-kandidaten/{n}.jpg"
        try:
            open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(c["thumb"], headers=UA), timeout=40).read())
        except Exception as e:
            fn = "(Vorschau fehlgeschlagen: %s)" % str(e)[:40]
        print(f'{n}: {c["title"]} | {c["w"]}x{c["h"]} | {c["lic"]} | {c["author"]} | {fn}')
        n += 1; time.sleep(1.5)
        if n >= 6: break
    if not n: print("Keine passenden Kandidaten. Anderen Suchbegriff probieren (englisch und deutsch).")

def holen(title, name):
    from PIL import Image
    assert re.fullmatch(r"[a-z0-9-]+", name), "Name nur aus Kleinbuchstaben, Ziffern und Bindestrich"
    r = api({"action": "query", "format": "json", "titles": title, "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 500})
    c = info(r["query"]["pages"].values())[0]
    assert OKLIC.match(c["lic"]), "Lizenz nicht erlaubt: " + c["lic"]
    size = 1920 if c["w"] >= 1920 else 1280
    url = re.sub(r"/\d+px-", f"/{size}px-", c["thumb"])
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
    tmp = f"/tmp/{name}.src.jpg"; open(tmp, "wb").write(raw)
    im = Image.open(tmp).convert("RGB"); w, h = im.size
    tw, th = (w, int(w * 2 / 3)) if w / h < 1.5 else (int(h * 1.5), h)
    l, t = (w - tw) // 2, (h - th) // 2
    im = im.crop((l, t, l + tw, t + th)); out = os.path.join(ROOT, "img") + "/"
    im.resize((1600, 1067), Image.LANCZOS).save(f"{out}{name}-1600.webp", quality=78, method=6)
    im.resize((1200, 800), Image.LANCZOS).save(f"{out}{name}-1200.webp", quality=77, method=6)
    im.resize((800, 533), Image.LANCZOS).save(f"{out}{name}-800.webp", quality=76, method=6)
    im.resize((1200, 800), Image.LANCZOS).crop((0, 85, 1200, 715)).save(f"{out}og-{name}.jpg", quality=84, optimize=True)
    meta = json.load(open(META, encoding="utf-8"))
    meta[name] = {"title": c["title"], "author": c["author"], "lic": c["lic"], "desc": c["desc"], "src": [c["w"], c["h"]]}
    json.dump(meta, open(META, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ok:", name, "| Urheber:", c["author"], "| Lizenz:", c["lic"], "| Bild ansehen:", f"{out}{name}-800.webp")

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "suchen": suchen(sys.argv[2])
    elif len(sys.argv) >= 4 and sys.argv[1] == "holen": holen(sys.argv[2], sys.argv[3])
    else: print(__doc__)
