
(function(){
  // Vorsichtige Annahmen pro Region. Nachtpreis nach Zimmerzahl (1, 2, 3, 4+), Auslastung.
  var R = {
    jungfrau:{name:"Grindelwald und Jungfrau Region", adr:[170,230,300,390], occ:0.60, cap:null},
    bern:{name:"Bern und Umgebung", adr:[130,170,225,300], occ:0.58, cap:null},
    innerschweiz:{name:"Luzern und Innerschweiz", adr:[140,180,240,320], occ:0.60, cap:null},
    ch:{name:"Übrige Schweiz", adr:[120,160,210,280], occ:0.50, cap:null}
  };
  var FEE = 0.155;
  function chf(n){ return "CHF " + Math.round(n).toLocaleString("de-CH").replace(/,/g,"’"); }
  function val(name){ var el=document.querySelector('input[name="'+name+'"]:checked'); return el?parseFloat(el.value):0; }
  function calc(){
    var r = R[document.getElementById("region").value];
    var i = val("rooms"), c = val("pkg");
    var nights = Math.round(365*r.occ);
    var capped = r.cap && nights > r.cap;
    if (capped) nights = r.cap;
    var gross = nights * r.adr[i];
    var fee = gross*FEE, net = gross-fee, comm = net*c, keep = net-comm;
    var m = keep/12;
    document.getElementById("res").innerHTML = chf(m*0.85) + " – " + chf(m*1.15).replace("CHF ","") + " <small>pro Monat</small>";
    document.getElementById("lines").innerHTML =
      "<div><span>Nächte pro Jahr</span><span>"+nights+"</span></div>"+
      "<div><span>Nachtpreis im Schnitt</span><span>"+chf(r.adr[i])+"</span></div>"+
      "<div><span>Umsatz pro Jahr</span><span>"+chf(gross)+"</span></div>"+
      "<div><span>Plattformgebühr 15,5 %</span><span>− "+chf(fee).replace("CHF ","")+"</span></div>"+
      "<div><span>Provision "+Math.round(c*100)+" %</span><span>− "+chf(comm).replace("CHF ","")+"</span></div>"+
      "<div><span>Bleibt bei Ihnen pro Jahr</span><span>"+chf(keep)+"</span></div>";
    var w = document.getElementById("warn");
    if (false){}
    else if (document.getElementById("region").value==="ch"){ w.hidden=false; w.textContent="Für die übrige Schweiz ist die Schätzung grob. Nachtpreise unterscheiden sich zwischen Bergort, Stadt und Land stark."; }
    else { w.hidden=true; }
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
