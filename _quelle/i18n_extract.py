"""Sammelt alle übersetzbaren Einheiten aus den deutschen Seiten."""
import os, re, json
from bs4 import BeautifulSoup, NavigableString, Tag, Comment
INLINE = {"a","b","strong","i","em","span","small","br","sup","sub","abbr","code","time","mark","u"}
SKIP = {"script","style","svg","noscript"}
ATTRS = ["alt","aria-label","title","placeholder"]
PAGES = ["index.html","impressum/index.html","datenschutz/index.html","404.html"] + [d+"/index.html" for d in sorted(os.listdir("site")) if d.startswith("airbnb-verwaltung-")]
def has_text(t): return bool(re.search(r"[A-Za-zÄÖÜäöüé]", t))
def is_unit(el):
    for d in el.descendants:
        if isinstance(d, Tag) and (d.name not in INLINE): return False
    return has_text(el.get_text())
def norm(h): return re.sub(r"\s+", " ", h).strip()
def units(root, out):
    for c in root.children:
        if isinstance(c, Comment): continue
        if isinstance(c, NavigableString):
            if has_text(str(c)): out.append(("text", norm(str(c))))
        elif isinstance(c, Tag):
            if c.name in SKIP: continue
            if c.name in ("title",): out.append(("html", norm(c.decode_contents()))); continue
            if is_unit(c) and c.name not in INLINE|{"html","body","head"}:
                out.append(("html", norm(c.decode_contents())))
            else:
                units(c, out)
def collect():
    found = {}
    for p in PAGES:
        s = BeautifulSoup(open("site/"+p, encoding="utf-8").read(), "html.parser")
        out = []
        units(s.body, out); units(s.head, out)
        for el in s.find_all(True):
            if el.name in SKIP: continue
            for a in ATTRS:
                if el.get(a) and has_text(el[a]): out.append(("attr", norm(el[a])))
        for m in s.find_all("meta"):
            if m.get("name")=="description" or m.get("property") in ("og:title","og:description"):
                out.append(("attr", norm(m["content"])))
        for sc in s.find_all("script", type="application/ld+json"):
            def walk(o):
                if isinstance(o, dict): [walk(v) for k,v in o.items() if k not in ("@context","@type","@id","url","item","image","logo","telephone","email")]
                elif isinstance(o, list): [walk(v) for v in o]
                elif isinstance(o, str) and has_text(o): out.append(("json", norm(o)))
            walk(json.loads(sc.string))
        for kind, t in out:
            found.setdefault(t, set()).add(kind)
    return found
if __name__ == "__main__":
    f = collect()
    # JS-Strings
    js = open("site/assets/site.js", encoding="utf-8").read()
    jss = sorted(set(m for m in re.findall(r'"((?:[^"\\]|\\.)*?)"', js) + re.findall(r"'((?:[^'\\]|\\.)*?)'", js) if re.search(r"[a-zäöü]{3,} [A-Za-zäöü]|[ÄÖÜäöü]", m) and not re.search(r"querySelector|getElementById|\(|\[name", m)))
    json.dump({"units": sorted(f.keys(), key=len), "js": jss}, open("i18n/source.json","w"), ensure_ascii=False, indent=0)
    print(len(f), "units,", sum(len(k) for k in f), "chars;", len(jss), "js strings")
