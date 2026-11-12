// Browser-Test nach dem Bauen. Aufruf aus dem Repo:  node _quelle/tools/test.js
// Startet einen lokalen Server auf dem Repo, prueft Startseite, alle Ratgeber-Seiten und Stichproben in 375 und 1366 px:
// keine seitliche Ueberbreite, keine kaputten Bilder, keine JavaScript-Fehler, Rechner liefert einen Betrag, Formular hat beide Knoepfe.
const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');const path=require('path');
const ROOT=path.resolve(__dirname,'..','..');
(async()=>{
 const srv=spawn('python3',['-m','http.server','8799'],{cwd:ROOT,stdio:'ignore'});await new Promise(r=>setTimeout(r,1200));
 const sm=fs.readFileSync(path.join(ROOT,'sitemap.xml'),'utf8');
 const all=[...sm.matchAll(/<loc>https:\/\/alpinhost\.ch([^<]*)<\/loc>/g)].map(m=>m[1]||'/');
 const pages=[...new Set(['/','/en/','/fr/','/it/','/es/',...all.filter(u=>u.startsWith('/ratgeber')),...all.filter(u=>u.includes('verwaltung')).slice(0,3)])];
 const b=await chromium.launch();let bad=0;const errs=[];
 for(const w of [375,1366]){const p=await b.newPage({viewport:{width:w,height:860}});p.on('pageerror',e=>errs.push(e.message));
  await p.route('**/formsubmit.co/**',r=>r.abort());
  for(const u of pages){const r=await p.goto('http://localhost:8799'+u);if(!r||!r.ok()){console.log('FEHLER',w,u,r&&r.status());bad++;continue}
   await p.evaluate(async()=>{for(const i of document.images)i.loading='eager';await new Promise(r=>setTimeout(r,350))});
   const ov=await p.evaluate(()=>document.documentElement.scrollWidth-window.innerWidth);
   const bi=await p.evaluate(()=>[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length);
   if(ov>0||bi>0){console.log('FEHLER',w,u,'ueberbreite',ov,'kaputte bilder',bi);bad++}}
  if(w===1366){await p.goto('http://localhost:8799/');
   const res=await p.evaluate(()=>(document.querySelector('#rechner')||document.body).innerText.match(/CHF\s[\d’']+/g)||[]);
   if(!res.some(x=>!/CHF\s0$/.test(x))){console.log('FEHLER Rechner liefert keinen Betrag');bad++}
   const btn=await p.evaluate(()=>[...document.querySelectorAll('#leadform button')].length);
   if(btn!==2){console.log('FEHLER Formular: erwartet 2 Knoepfe, gefunden',btn);bad++}}
  await p.close();}
 await b.close();srv.kill();
 if(errs.length){console.log('FEHLER JavaScript:',errs.slice(0,5));bad++}
 console.log(bad?('NICHT OK: '+bad+' Problem(e)'):('OK: '+pages.length+' Seiten in 2 Breiten geprueft'));process.exit(bad?1:0);
})();
