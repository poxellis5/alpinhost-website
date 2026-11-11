
(function(){
  // Marktdaten pro Ort: Ø Auslastung und Ø Nachtpreis aller aktiven Airbnb-Inserate, Nov 2025 - Okt 2026 (GuestFavorites).
  // Der Ø Nachtpreis liegt über dem Median (grosse Chalets ziehen ihn hoch). 2 Zimmer = ca. 70 % davon, entspricht dem Median. Faktoren nach Grösse (1, 2, 3, 4+ Zimmer).
  var R = {
    grindelwald:{name:"Grindelwald", n:570, occ:0.72, adr:296},
    lauterbrunnen:{name:"Wengen, Mürren, Lauterbrunnen", n:535, occ:0.65, adr:343},
    interlaken:{name:"Interlaken", n:315, occ:0.67, adr:327},
    thun:{name:"Thun und Thunersee", n:111, occ:0.68, adr:197},
    gstaad:{name:"Gstaad und Saanenland", n:260, occ:0.61, adr:289},
    luzern:{name:"Stadt Luzern", n:256, occ:0.76, adr:277},
    vierwaldstaettersee:{name:"Vierwaldstättersee (Weggis, Vitznau, Brunnen)", n:0, occ:0.68, adr:230},
    engelberg:{name:"Engelberg", n:227, occ:0.61, adr:199},
    andermatt:{name:"Andermatt", n:244, occ:0.58, adr:229},
    zermatt:{name:"Zermatt", n:875, occ:0.61, adr:389},
    verbier:{name:"Verbier", n:762, occ:0.54, adr:401},
    saasfee:{name:"Saas-Fee", n:737, occ:0.54, adr:272},
    crans:{name:"Crans-Montana", n:664, occ:0.51, adr:202},
    stmoritz:{name:"St. Moritz und Engadin", n:372, occ:0.57, adr:293},
    davos:{name:"Davos und Klosters", n:607, occ:0.54, adr:237},
    laax:{name:"Laax und Flims", n:257, occ:0.54, adr:228},
    arosa:{name:"Arosa und Lenzerheide", n:257, occ:0.51, adr:226},
    zuerich:{name:"Zürich", n:1970, occ:0.67, adr:183},
    bern:{name:"Bern", n:309, occ:0.66, adr:144},
    basel:{name:"Basel", n:777, occ:0.63, adr:153},
    genf:{name:"Genf", n:704, occ:0.68, adr:149},
    lausanne:{name:"Lausanne", n:387, occ:0.67, adr:128},
    lugano:{name:"Lugano", n:567, occ:0.64, adr:145},
    locarno:{name:"Locarno und Ascona", n:270, occ:0.61, adr:161}
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
      document.getElementById("res").innerHTML = "Persönliche Schätzung";
      document.getElementById("lines").innerHTML = "";
      document.getElementById("basis").textContent = "";
      w.hidden=false; w.innerHTML='Für Ihren Ort rechnen wir mit echten Vergleichswohnungen aus der Nachbarschaft, kostenlos. <a href="#kontakt" style="color:inherit;font-weight:600">Wohnung prüfen lassen</a>';
      return;
    }
    var occ = Math.min(r.occ*SIZE_OCC[i], 0.85);
    var adr = Math.round(r.adr*SIZE_ADR[i]/5)*5;
    var nights = Math.round(365*occ);
    var gross = nights * adr;
    var fee = gross*FEE, net = gross-fee, comm = net*c, keep = net-comm;
    var m = keep/12;
    document.getElementById("res").innerHTML = chf(m*0.85) + " – " + chf(m*1.15).replace("CHF ","") + " <small>pro Monat</small>";
    document.getElementById("lines").innerHTML =
      "<div><span>Auslastung "+r.name+"</span><span>"+Math.round(occ*100)+" %</span></div>"+
      "<div><span>Gebuchte Nächte pro Jahr</span><span>"+nights+"</span></div>"+
      "<div><span>Nachtpreis im Schnitt</span><span>"+chf(adr)+"</span></div>"+
      "<div><span>Umsatz pro Jahr</span><span>"+chf(gross)+"</span></div>"+
      "<div><span>Plattformgebühr 15,5 %</span><span>− "+chf(fee).replace("CHF ","")+"</span></div>"+
      "<div><span>Provision "+Math.round(c*100)+" %</span><span>− "+chf(comm).replace("CHF ","")+"</span></div>"+
      "<div><span>Bleibt bei Ihnen pro Jahr</span><span>"+chf(keep)+"</span></div>";
    w.hidden=true;
    document.getElementById("basis").textContent = r.n ? "Basis: "+r.n.toLocaleString("de-CH").replace(/,/g,"’")+" aktive Airbnb-Inserate in "+r.name+", Ø Nachtpreis "+chf(r.adr)+", Ø Auslastung "+Math.round(r.occ*100)+" %." : "Basis: Durchschnitt der Airbnb-Inserate in der Zentralschweiz, Ø Nachtpreis "+chf(r.adr)+", Ø Auslastung "+Math.round(r.occ*100)+" %.";
  }
  var cf=document.getElementById("calcform"); if(cf){ cf.addEventListener("change", calc); calc(); }

  document.querySelectorAll("[data-copy]").forEach(function(b){
    b.addEventListener("click", function(){
      var t = document.getElementById(b.dataset.copy).textContent;
      var done = function(){ b.textContent="Kopiert"; setTimeout(function(){b.textContent="Kopieren";},1600); };
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
    card.setAttribute("tabindex","0"); card.setAttribute("role","button"); card.setAttribute("aria-label","Paket "+pkg+" wählen");
    card.addEventListener("click", function(e){ if(e.target.closest("summary,details p")) return; e.preventDefault(); openModal(pkg); });
    card.addEventListener("keydown", function(e){ if((e.key==="Enter"||e.key===" ") && e.target===card){ e.preventDefault(); openModal(pkg); } });
  });
  document.getElementById("m-form").addEventListener("submit", function(e){
    e.preventDefault();
    var g=function(id){return document.getElementById(id).value.trim();}, msg=document.getElementById("m-msg");
    var need=["m-name","m-tel","m-ort"].filter(function(id){return !g(id);});
    if(need.length){ msg.textContent="Bitte Name, Telefon und Ort der Wohnung ausfüllen."; document.getElementById(need[0]).focus(); return; }
    var text="Anfrage Alpinhost\nPaket: "+document.getElementById("m-pkgname").textContent+"\nName: "+g("m-name")+"\nTelefon: "+g("m-tel")+"\nOrt: "+g("m-ort")+"\nZimmer: "+g("m-zi");
    var url="https://wa.me/41795318111?text="+encodeURIComponent(text);
    msg.innerHTML='Ihre Anfrage ist vorbereitet. <a href="'+url+'" target="_blank" rel="noopener" style="color:var(--lake);font-weight:600">In WhatsApp öffnen und senden</a>. Lieber anrufen? <b>+41 79 531 81 11</b>';
  });
  var f = document.getElementById("leadform");
  if (f) f.addEventListener("submit", function(e){
    e.preventDefault();
    var msg = document.getElementById("formmsg");
    var need = ["f-name","f-tel","f-ort"].filter(function(id){ return !document.getElementById(id).value.trim(); });
    if (need.length){ msg.textContent = "Bitte Name, Telefon und Ort der Wohnung ausfüllen."; document.getElementById(need[0]).focus(); return; }
    var g = function(id){ return document.getElementById(id).value.trim(); };
    var text = "Anfrage Alpinhost\nName: "+g("f-name")+"\nTelefon: "+g("f-tel")+"\nOrt: "+g("f-ort")+"\nZimmer: "+g("f-zi")+"\nStatus: "+g("f-status")+"\nPaket: "+g("f-pkg")+(g("f-msg")?"\nNachricht: "+g("f-msg"):"");
    var url = "https://wa.me/41795318111?text=" + encodeURIComponent(text);
    msg.innerHTML = 'Ihre Anfrage ist vorbereitet. <a href="'+url+'" target="_blank" rel="noopener">In WhatsApp öffnen und senden</a>. Falls WhatsApp nicht öffnet, rufen Sie uns an.';
  });
})();
