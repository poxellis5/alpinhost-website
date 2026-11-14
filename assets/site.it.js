
(function(){
  // Marktdaten pro Ort: Ø Auslastung und Ø Nachtpreis aller aktiven Airbnb-Inserate, Nov 2025 - Okt 2026 (GuestFavorites).
  // Der Ø Nachtpreis liegt über dem Median (grosse Chalets ziehen ihn hoch). 2 Zimmer = ca. 70 % davon, entspricht dem Median. Faktoren nach Grösse (1, 2, 3, 4+ Zimmer).
  var R = {
    grindelwald:{name:"Grindelwald", n:570, occ:0.72, adr:296},
    lauterbrunnen:{name:"Wengen, Mürren, Lauterbrunnen", n:535, occ:0.65, adr:343},
    interlaken:{name:"Interlaken", n:315, occ:0.67, adr:327},
    thun:{name:"Thun e lago di Thun", n:111, occ:0.68, adr:197},
    gstaad:{name:"Gstaad e Saanenland", n:260, occ:0.61, adr:289},
    luzern:{name:"Città di Lucerna", n:256, occ:0.76, adr:277},
    vierwaldstaettersee:{name:"Lago dei Quattro Cantoni (Weggis, Vitznau, Brunnen)", n:0, occ:0.68, adr:230},
    engelberg:{name:"Engelberg", n:227, occ:0.61, adr:199},
    andermatt:{name:"Andermatt", n:244, occ:0.58, adr:229},
    zermatt:{name:"Zermatt", n:875, occ:0.61, adr:389},
    verbier:{name:"Verbier", n:762, occ:0.54, adr:401},
    saasfee:{name:"Saas-Fee", n:737, occ:0.54, adr:272},
    crans:{name:"Crans-Montana", n:664, occ:0.51, adr:202},
    stmoritz:{name:"St. Moritz ed Engadina", n:372, occ:0.57, adr:293},
    davos:{name:"Davos e Klosters", n:607, occ:0.54, adr:237},
    laax:{name:"Laax e Flims", n:257, occ:0.54, adr:228},
    arosa:{name:"Arosa e Lenzerheide", n:257, occ:0.51, adr:226},
    zuerich:{name:"Zurigo", n:1970, occ:0.67, adr:183},
    bern:{name:"Berna", n:309, occ:0.66, adr:144},
    basel:{name:"Basilea", n:777, occ:0.63, adr:153},
    genf:{name:"Ginevra", n:704, occ:0.68, adr:149},
    lausanne:{name:"Lausanne", n:387, occ:0.67, adr:128},
    lugano:{name:"Lugano", n:567, occ:0.64, adr:145},
    locarno:{name:"Locarno e Ascona", n:270, occ:0.61, adr:161}
  };
  var SIZE_ADR = [0.55, 0.7, 0.95, 1.35], SIZE_OCC = [1.04, 1.0, 0.97, 0.92];
  var FEE = 0.155;
  function chf(n){ return "CHF " + Math.round(n).toLocaleString("de-CH").replace(/,/g,"’"); }
  function val(name){ var el=document.querySelector('input[name="'+name+'"]:checked'); return el?parseFloat(el.value):0; }
  function calc(){
    var key = document.getElementById("region").value, r = R[key];
    var i = val("rooms"), c = val("pkg");
    var w = document.getElementById("warn");
    if (!r){
      document.getElementById("res").innerHTML = "Stima personalizzata";
      document.getElementById("lines").innerHTML = "";
      document.getElementById("basis").textContent = "";
      w.hidden=false; w.innerHTML='Per la Sua località calcoliamo gratuitamente con veri appartamenti comparabili della zona. <a href="#kontakt" style="color:inherit;font-weight:600">Far valutare l’appartamento</a>';
      return;
    }
    var occ = Math.min(r.occ*SIZE_OCC[i], 0.85);
    var adr = Math.round(r.adr*SIZE_ADR[i]/5)*5;
    var nights = Math.round(365*occ);
    var gross = nights * adr;
    var fee = gross*FEE, net = gross-fee, comm = net*c, keep = net-comm;
    var m = keep/12;
    document.getElementById("res").innerHTML = chf(m*0.85) + " – " + chf(m*1.15).replace("CHF ","") + " <small>al mese</small>";
    document.getElementById("lines").innerHTML =
      "<div><span>Occupazione "+r.name+"</span><span>"+Math.round(occ*100)+" %</span></div>"+
      "<div><span>Notti prenotate all’anno</span><span>"+nights+"</span></div>"+
      "<div><span>Prezzo medio per notte</span><span>"+chf(adr)+"</span></div>"+
      "<div><span>Ricavi annui</span><span>"+chf(gross)+"</span></div>"+
      "<div><span>Commissione piattaforma 15,5 %</span><span>− "+chf(fee).replace("CHF ","")+"</span></div>"+
      "<div><span>Provvigione "+Math.round(c*100)+" %</span><span>− "+chf(comm).replace("CHF ","")+"</span></div>"+
      "<div><span>Le rimane all’anno</span><span>"+chf(keep)+"</span></div>";
    w.hidden=true;
    document.getElementById("basis").textContent = r.n ? "Base: "+r.n.toLocaleString("de-CH").replace(/,/g,"’")+" annunci Airbnb attivi a "+r.name+", prezzo medio per notte "+chf(r.adr)+", occupazione media "+Math.round(r.occ*100)+" %." : "Base: media degli annunci Airbnb nella Svizzera centrale, prezzo medio per notte "+chf(r.adr)+", occupazione media "+Math.round(r.occ*100)+" %.";
  }
  var cf=document.getElementById("calcform"); if(cf){ cf.addEventListener("change", calc); calc(); }

  document.querySelectorAll("[data-copy]").forEach(function(b){
    b.addEventListener("click", function(){
      var t = document.getElementById(b.dataset.copy).textContent;
      var done = function(){ b.textContent="Copiato"; setTimeout(function(){b.textContent="Copia";},1600); };
      try{ navigator.clipboard.writeText(t).then(done, function(){ selectText(b.dataset.copy); }); }catch(e){ selectText(b.dataset.copy); }
    });
  });
  function selectText(id){ var r=document.createRange(); r.selectNodeContents(document.getElementById(id)); var s=getSelection(); s.removeAllRanges(); s.addRange(r); }

  var modal=document.getElementById("pkgmodal"), lastFocus=null;
  function openModal(pkg){ lastFocus=document.activeElement; document.getElementById("m-pkgname").textContent=pkg; modal.hidden=false; document.body.style.overflow="hidden"; setTimeout(function(){document.getElementById("m-name").focus();},30); }
  function closeModal(){ modal.hidden=true; document.body.style.overflow=""; if(lastFocus&&lastFocus.focus) lastFocus.focus(); }
  document.getElementById("m-close").addEventListener("click", closeModal);
  modal.addEventListener("click", function(e){ if(e.target===modal) closeModal(); });
  document.addEventListener("keydown", function(e){ if(e.key==="Escape" && !modal.hidden) closeModal(); });
  document.querySelectorAll(".plan").forEach(function(card){
    var pkg=card.querySelector(".choose").dataset.pkg;
    card.setAttribute("tabindex","0"); card.setAttribute("role","button"); card.setAttribute("aria-label","Scegli il pacchetto "+pkg);
    card.addEventListener("click", function(e){ if(e.target.closest("summary,details p")) return; e.preventDefault(); openModal(pkg); });
    card.addEventListener("keydown", function(e){ if((e.key==="Enter"||e.key===" ") && e.target===card){ e.preventDefault(); openModal(pkg); } });
  });
  var EP="https://formsubmit.co/ajax/info@alpinhost.ch", WA="https://wa.me/41795318111?text=";
  function fv(id){ return document.getElementById(id).value.trim(); }
  function sendMail(data, msg, btn, waUrl){
    var old=btn.textContent; btn.disabled=true; btn.textContent="Invio in corso …";
    data._template="table"; data._captcha="false"; data.Sprache=document.documentElement.lang; data.Seite=location.pathname;
    fetch(EP,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
      .then(function(r){ return r.json(); })
      .then(function(j){ if(String(j.success)!=="true") throw new Error("send"); msg.innerHTML='<b>Grazie, abbiamo ricevuto la Sua richiesta.</b> La ricontattiamo in giornata.'; btn.textContent="Inviato"; })
      .catch(function(){ btn.disabled=false; btn.textContent=old; msg.innerHTML='L’invio non è riuscito. La preghiamo di <a href="'+waUrl+'" target="_blank" rel="noopener" style="color:var(--lake);font-weight:600">inviare via WhatsApp</a> o di scrivere a <a href="mailto:info@alpinhost.ch?subject='+encodeURIComponent(data._subject)+'&body='+waUrl.split("text=")[1]+'" style="color:var(--lake);font-weight:600">info@alpinhost.ch</a>.'; });
  }
  function openWa(url, msg){
    window.open(url, "_blank", "noopener");
    msg.innerHTML='La Sua richiesta è pronta. <a href="'+url+'" target="_blank" rel="noopener" style="color:var(--lake);font-weight:600">Apri e invia in WhatsApp</a>. Preferisce chiamare? <b>+41 79 531 81 11</b>';
  }
  // Paket-Fenster
  function mData(){
    var msg=document.getElementById("m-msg");
    var need=["m-name","m-tel","m-ort"].filter(function(id){return !fv(id);});
    if(need.length){ msg.textContent="Inserisca nome, telefono e località dell’appartamento."; document.getElementById(need[0]).focus(); return null; }
    var pkg=document.getElementById("m-pkgname").textContent;
    var text="Alpinhost enquiry (IT)\nPackage: "+pkg+"\nName: "+fv("m-name")+"\nPhone: "+fv("m-tel")+"\nLocation: "+fv("m-ort")+"\nRooms: "+fv("m-zi");
    return {msg:msg, wa:WA+encodeURIComponent(text), data:{_subject:"Anfrage Alpinhost: "+fv("m-ort"), Name:fv("m-name"), Telefon:fv("m-tel"), Ort:fv("m-ort"), Zimmer:fv("m-zi"), Paket:pkg}};
  }
  document.getElementById("m-form").addEventListener("submit", function(e){
    e.preventDefault();
    var d=mData(); if(!d) return;
    if(fv("m-hp")) return;
    sendMail(d.data, d.msg, e.target.querySelector('button[type="submit"]'), d.wa);
  });
  document.getElementById("m-wa").addEventListener("click", function(){ var d=mData(); if(d) openWa(d.wa, d.msg); });
  // Kontaktformular
  function fData(){
    var msg=document.getElementById("formmsg");
    var need=["f-name","f-tel","f-ort"].filter(function(id){ return !fv(id); });
    if(need.length){ msg.textContent="Inserisca nome, telefono e località dell’appartamento."; document.getElementById(need[0]).focus(); return null; }
    var text="Alpinhost enquiry (IT)\nName: "+fv("f-name")+"\nPhone: "+fv("f-tel")+(fv("f-mail")?"\nE-Mail: "+fv("f-mail"):"")+"\nLocation: "+fv("f-ort")+"\nRooms: "+fv("f-zi")+"\nStatus: "+fv("f-status")+"\nPackage: "+fv("f-pkg")+(fv("f-msg")?"\nMessage: "+fv("f-msg"):"");
    var data={_subject:"Anfrage Alpinhost: "+fv("f-ort"), Name:fv("f-name"), Telefon:fv("f-tel"), Ort:fv("f-ort"), Zimmer:fv("f-zi"), Status:fv("f-status"), Paket:fv("f-pkg")};
    if(fv("f-mail")){ data["E-Mail"]=fv("f-mail"); data._replyto=fv("f-mail"); }
    if(fv("f-msg")) data.Nachricht=fv("f-msg");
    return {msg:msg, wa:WA+encodeURIComponent(text), data:data};
  }
  var f=document.getElementById("leadform");
  if(f) f.addEventListener("submit", function(e){
    e.preventDefault();
    var d=fData(); if(!d) return;
    if(fv("f-hp")) return;
    sendMail(d.data, d.msg, f.querySelector('button[type="submit"]'), d.wa);
  });
  var fwa=document.getElementById("f-wa");
  if(fwa) fwa.addEventListener("click", function(){ var d=fData(); if(d) openWa(d.wa, d.msg); });
})();

(function(){
  var ms=document.querySelectorAll("nav.main .mi");
  ms.forEach(function(m){
    var cx=0, cy=0;
    function mv(e){ if(Math.abs(e.clientX-cx)+Math.abs(e.clientY-cy)<8) return; var t=m.querySelector(".mt"); if(t&&t.matches(":hover")) return; m.classList.remove("shut"); document.removeEventListener("mousemove",mv); }
    m.addEventListener("click",function(e){ if(e.target.closest(".sub a")){ cx=e.clientX; cy=e.clientY; m.classList.add("shut"); if(document.activeElement) document.activeElement.blur(); document.addEventListener("mousemove",mv); } });
    m.addEventListener("keydown",function(e){ if(e.key==="Escape"){ m.classList.add("shut"); var t=m.querySelector(".mt"); if(t) t.focus(); } });
    m.addEventListener("focusout",function(e){ if(!m.contains(e.relatedTarget)&&!m.matches(":hover")) m.classList.remove("shut"); });
  });
  function openFaq(){ var h=location.hash.slice(1); if(!/^frage-\d+$/.test(h)) return; var d=document.getElementById(h); if(d&&d.tagName==="DETAILS"){ d.open=true; d.scrollIntoView({block:"start"}); } }
  window.addEventListener("hashchange",openFaq); openFaq();
})();

(function(){
  var EP="https://grindelwaldexperiences.ch/api/stats",SRC="direct",L=document.documentElement.lang||"de";
  function hit(e){ try{ if(!/alpinhost\.ch$/.test(location.hostname)) return; navigator.sendBeacon(EP,JSON.stringify({e:e,s:SRC,l:L,w:"alpinhost"})); }catch(x){} }
  try{ SRC=sessionStorage.getItem("ah-src")||""; if(!SRC){
    var us=(new URLSearchParams(location.search).get("utm_source")||"").toLowerCase(),rh="";
    try{ rh=document.referrer?new URL(document.referrer).hostname.replace(/^www\./,""):""; }catch(x){}
    var KN=[["chatgpt","chatgpt"],["openai","chatgpt"],["perplexity","perplexity"],["gemini","gemini"],["copilot","copilot"],["claude.ai","claude"],["google","google"],["bing","bing"],["duckduckgo","duckduckgo"],["yahoo","yahoo"],["grindelwaldexperiences","grindelwaldexperiences"],["jungfrauflights","jungfrauflights"],["linkedin","linkedin"],["instagram","instagram"],["facebook","facebook"]],h=us+" "+rh;
    for(var k=0;k<KN.length;k++) if(h.indexOf(KN[k][0])>=0){ SRC=KN[k][1]; break; }
    if(!SRC) SRC=rh&&rh.indexOf("alpinhost")<0?("ref:"+rh).slice(0,40):(us?("utm:"+us).slice(0,40):"direct");
    sessionStorage.setItem("ah-src",SRC); hit("visit"); } }catch(x){ SRC=SRC||"direct"; }
  var lf=document.getElementById("leadform"); if(lf) lf.addEventListener("submit",function(){ hit("lead"); });
  document.addEventListener("click",function(e){ var a=e.target.closest&&e.target.closest('a[href*="wa.me"],a[href^="tel:"],a[href^="mailto:"]'); if(a) hit("lead"); },true);
})();
