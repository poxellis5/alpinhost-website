import os,re,json,sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
ROOT=sys.argv[1]; DOM="https://alpinhost.ch"
pages={}
for d,ds,fs in os.walk(ROOT):
    ds[:]=[x for x in ds if not x.startswith(("_","."))]   # _quelle und .git nicht pruefen
    for f in fs:
        if f.endswith(".html"):
            p=os.path.join(d,f); rel="/"+os.path.relpath(p,ROOT).replace("index.html","")
            pages[rel]=BeautifulSoup(open(p,encoding="utf-8").read(),"html.parser")
issues=[]
ids={u:{t.get("id") for t in s.find_all(id=True)} for u,s in pages.items()}
for u,s in pages.items():
    t=s.title.string if s.title else None
    d=s.find("meta",attrs={"name":"description"})
    if not t: issues.append((u,"no title"))
    elif len(t)>65: issues.append((u,f"title {len(t)}: {t}"))
    if d and len(d["content"])>160: issues.append((u,f"desc {len(d['content'])}"))
    h1=s.find_all("h1")
    if len(h1)!=1: issues.append((u,f"h1 count {len(h1)}"))
    for im in s.find_all("img"):
        if not im.get("alt"): issues.append((u,"img no alt "+im.get("src","")))
        src=im.get("src","")
        if not src.startswith("http"):
            fp=os.path.normpath(os.path.join(ROOT,urlparse(urljoin(DOM+u,src)).path.lstrip("/")))
            if not os.path.exists(fp): issues.append((u,"missing img "+src))
    for a in s.find_all("a",href=True):
        h=a["href"]
        if h.startswith(("mailto:","tel:","https://wa.me","javascript")): continue
        full=urljoin(DOM+u,h); pu=urlparse(full)
        if pu.netloc!="alpinhost.ch": continue
        path=pu.path
        if path not in pages and not os.path.exists(os.path.join(ROOT,path.lstrip("/"))): issues.append((u,"broken link "+h))
        elif pu.fragment and path in pages and pu.fragment not in ids[path]: issues.append((u,"broken anchor "+h))
    for sc in s.find_all("script",type="application/ld+json"):
        try: json.loads(sc.string)
        except Exception as e: issues.append((u,"jsonld "+str(e)))
    txt=s.get_text(" ")
    for bad in [";","ß","20 %","Übrige Schweiz","  "]:
        if bad in txt and bad!="  ":
            # report contexts
            for m in re.finditer(re.escape(bad),txt):
                issues.append((u,f"text '{bad}': ...{txt[max(0,m.start()-40):m.end()+30]!r}"))
for i in issues: print(i)
print(len(pages),"pages",len(issues),"issues")
