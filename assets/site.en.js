
(function(){
  // Marktdaten pro Ort: Ø Auslastung und Ø Nachtpreis aller aktiven Airbnb-Inserate, Nov 2025 - Okt 2026 (GuestFavorites).
  // Der Ø Nachtpreis liegt über dem Median (grosse Chalets ziehen ihn hoch). 2 Zimmer = ca. 70 % davon, entspricht dem Median. Faktoren nach Grösse (1, 2, 3, 4+ Zimmer).
  var R = {
    grindelwald:{name:"Grindelwald", n:570, occ:0.72, adr:296},
    lauterbrunnen:{name:"Wengen, Mürren, Lauterbrunnen", n:535, occ:0.65, adr:343},
    interlaken:{name:"Interlaken", n:315, occ:0.67, adr:327},
    thun:{name:"Thun and Lake Thun", n:111, occ:0.68, adr:197},
    gstaad:{name:"Gstaad and Saanenland", n:260, occ:0.61, adr:289},
    luzern:{name:"Lucerne city", n:256, occ:0.76, adr:277},
    vierwaldstaettersee:{name:"Lake Lucerne (Weggis, Vitznau, Brunnen)", n:0, occ:0.68, adr:230},
    engelberg:{name:"Engelberg", n:227, occ:0.61, adr:199},
    andermatt:{name:"Andermatt", n:244, occ:0.58, adr:229},
    zermatt:{name:"Zermatt", n:875, occ:0.61, adr:389},
    verbier:{name:"Verbier", n:762, occ:0.54, adr:401},
    saasfee:{name:"Saas-Fee", n:737, occ:0.54, adr:272},
    crans:{name:"Crans-Montana", n:664, occ:0.51, adr:202},
    stmoritz:{name:"St. Moritz and Engadine", n:372, occ:0.57, adr:293},
    davos:{name:"Davos and Klosters", n:607, occ:0.54, adr:237},
    laax:{name:"Laax and Flims", n:257, occ:0.54, adr:228},
    arosa:{name:"Arosa and Lenzerheide", n:257, occ:0.51, adr:226},
    zuerich:{name:"Zurich", n:1970, occ:0.67, adr:183},
    bern:{name:"Bern", n:309, occ:0.66, adr:144},
    basel:{name:"Basel", n:777, occ:0.63, adr:153},
    genf:{name:"Geneva", n:704, occ:0.68, adr:149},
    lausanne:{name:"Lausanne", n:387, occ:0.67, adr:128},
    lugano:{name:"Lugano", n:567, occ:0.64, adr:145},
    locarno:{name:"Locarno and Ascona", n:270, occ:0.61, adr:161}
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
      document.getElementById("res").innerHTML = "Personal estimate";
      document.getElementById("lines").innerHTML = "";
      document.getElementById("basis").textContent = "";
      w.hidden=false; w.innerHTML='For your location we calculate with real comparable apartments nearby, free of charge. <a href="#kontakt" style="color:inherit;font-weight:600">Get a free assessment</a>';
      return;
    }
    var occ = Math.min(r.occ*SIZE_OCC[i], 0.85);
    var adr = Math.round(r.adr*SIZE_ADR[i]/5)*5;
    var nights = Math.round(365*occ);
    var gross = nights * adr;
    var fee = gross*FEE, net = gross-fee, comm = net*c, keep = net-comm;
    var m = keep/12;
    document.getElementById("res").innerHTML = chf(m*0.85) + " – " + chf(m*1.15).replace("CHF ","") + " <small>per month</small>";
    document.getElementById("lines").innerHTML =
      "<div><span>Occupancy "+r.name+"</span><span>"+Math.round(occ*100)+" %</span></div>"+
      "<div><span>Booked nights per year</span><span>"+nights+"</span></div>"+
      "<div><span>Average nightly rate</span><span>"+chf(adr)+"</span></div>"+
      "<div><span>Revenue per year</span><span>"+chf(gross)+"</span></div>"+
      "<div><span>Platform fee 15.5 %</span><span>− "+chf(fee).replace("CHF ","")+"</span></div>"+
      "<div><span>Commission "+Math.round(c*100)+" %</span><span>− "+chf(comm).replace("CHF ","")+"</span></div>"+
      "<div><span>You keep per year</span><span>"+chf(keep)+"</span></div>";
    w.hidden=true;
    document.getElementById("basis").textContent = r.n ? "Based on "+r.n.toLocaleString("de-CH").replace(/,/g,"’")+" active Airbnb listings in "+r.name+", avg. nightly rate "+chf(r.adr)+", avg. occupancy "+Math.round(r.occ*100)+" %." : "Based on the average of Airbnb listings in Central Switzerland, avg. nightly rate "+chf(r.adr)+", avg. occupancy "+Math.round(r.occ*100)+" %.";
  }
  var cf=document.getElementById("calcform"); if(cf){ cf.addEventListener("change", calc); calc(); }

  document.querySelectorAll("[data-copy]").forEach(function(b){
    b.addEventListener("click", function(){
      var t = document.getElementById(b.dataset.copy).textContent;
      var done = function(){ b.textContent="Copied"; setTimeout(function(){b.textContent="Copy";},1600); };
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
    card.setAttribute("tabindex","0"); card.setAttribute("role","button"); card.setAttribute("aria-label","Choose package "+pkg);
    card.addEventListener("click", function(e){ if(e.target.closest("summary,details p")) return; e.preventDefault(); openModal(pkg); });
    card.addEventListener("keydown", function(e){ if((e.key==="Enter"||e.key===" ") && e.target===card){ e.preventDefault(); openModal(pkg); } });
  });
  var EP="https://formsubmit.co/ajax/info@alpinhost.ch", WA="https://wa.me/41795318111?text=";
  function fv(id){ return document.getElementById(id).value.trim(); }
  function sendMail(data, msg, btn, waUrl){
    var old=btn.textContent; btn.disabled=true; btn.textContent="Sending …";
    data._template="table"; data._captcha="false"; data.Sprache=document.documentElement.lang; data.Seite=location.pathname;
    fetch(EP,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
      .then(function(r){ return r.json(); })
      .then(function(j){ if(String(j.success)!=="true") throw new Error("send"); msg.innerHTML='<b>Thank you, we have received your enquiry.</b> We will get back to you the same working day.'; btn.textContent="Sent"; })
      .catch(function(){ btn.disabled=false; btn.textContent=old; msg.innerHTML='Sending did not work. Please <a href="'+waUrl+'" target="_blank" rel="noopener" style="color:var(--lake);font-weight:600">send via WhatsApp</a> or write to <a href="mailto:info@alpinhost.ch" style="color:var(--lake);font-weight:600">info@alpinhost.ch</a>.'; });
  }
  function openWa(url, msg){
    window.open(url, "_blank", "noopener");
    msg.innerHTML='Your enquiry is ready. <a href="'+url+'" target="_blank" rel="noopener" style="color:var(--lake);font-weight:600">Open and send in WhatsApp</a>. Prefer to call? <b>+41 79 531 81 11</b>';
  }
  // Paket-Fenster
  function mData(){
    var msg=document.getElementById("m-msg");
    var need=["m-name","m-tel","m-ort"].filter(function(id){return !fv(id);});
    if(need.length){ msg.textContent="Please fill in name, phone and apartment location."; document.getElementById(need[0]).focus(); return null; }
    var pkg=document.getElementById("m-pkgname").textContent;
    var text="Alpinhost enquiry (EN)\nPackage: "+pkg+"\nName: "+fv("m-name")+"\nPhone: "+fv("m-tel")+"\nLocation: "+fv("m-ort")+"\nRooms: "+fv("m-zi");
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
    if(need.length){ msg.textContent="Please fill in name, phone and apartment location."; document.getElementById(need[0]).focus(); return null; }
    var text="Alpinhost enquiry (EN)\nName: "+fv("f-name")+"\nPhone: "+fv("f-tel")+(fv("f-mail")?"\nE-Mail: "+fv("f-mail"):"")+"\nLocation: "+fv("f-ort")+"\nRooms: "+fv("f-zi")+"\nStatus: "+fv("f-status")+"\nPackage: "+fv("f-pkg")+(fv("f-msg")?"\nMessage: "+fv("f-msg"):"");
    var data={_subject:"Anfrage Alpinhost: "+fv("f-ort"), Name:fv("f-name"), Telefon:fv("f-tel"), Ort:fv("f-ort"), Zimmer:fv("f-zi"), Status:fv("f-status"), Paket:fv("f-pkg")};
    if(fv("f-mail")){ data["E-Mail"]=fv("f-mail"); data._replyto=fv("f-mail"); }
    if(fv("f-msg")) data.Nachricht=fv("f-msg");
    return {msg:msg, wa:WA+encodeURIComponent(text), data:data};
  }
  var f=document.getElementById("leadform");
  f.addEventListener("submit", function(e){
    e.preventDefault();
    var d=fData(); if(!d) return;
    if(fv("f-hp")) return;
    sendMail(d.data, d.msg, f.querySelector('button[type="submit"]'), d.wa);
  });
  document.getElementById("f-wa").addEventListener("click", function(){ var d=fData(); if(d) openWa(d.wa, d.msg); });
})();
