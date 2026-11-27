# Ratgeber für Eigentümer – Daten und Seitenaufbau. Wird von build.py per exec() geladen.
RG_DATE = "2026-11-12"
RG_STAND = "November 2026"
RG_CREDITS = json.load(open("rg_img/meta.json", encoding="utf-8"))

def _src(label, url=None):
    return (label, url)

ARTICLES = [
{
 "slug": "ferienwohnung-vermieten-ertrag", "cat": "Vermieten", "mins": 6,
 "h1": "Was bringt eine Ferienwohnung in der Schweiz wirklich ein?",
 "title": "Ferienwohnung vermieten: Lohnt es sich? Die Zahlen",
 "desc": "Auslastung und Nachtpreise von Airbnb-Wohnungen in 13 Schweizer Orten, von Zermatt bis Bern. Mit Rechenbeispiel und den Kosten, die oft vergessen gehen.",
 "teaser": "Auslastung und Nachtpreise in 13 Orten, von Zermatt bis Bern. Mit Rechenbeispiel.",
 "lead": "Die ehrliche Antwort hängt vom Ort, von der Grösse und vom Inserat ab. Wir zeigen die Marktzahlen für 13 Schweizer Orte und rechnen ein Beispiel durch.",
 "photo": ("zermatt-zmutt-matterhorn", "Alte Holzhäuser im Weiler Zmutt oberhalb von Zermatt, dahinter das Matterhorn",
           "Zmutt oberhalb von Zermatt mit dem Matterhorn. Zermatt gehört zu den Orten mit den höchsten Nachtpreisen der Schweiz."),
 "key": ["Im Schweizer Schnitt sind Airbnb-Wohnungen zu 59 % ausgelastet und kosten CHF 199 pro Nacht.",
         "Grindelwald erreicht 72 % Auslastung, die Stadt Luzern 76 %.",
         "Der Durchschnittspreis täuscht. Grosse Chalets ziehen ihn hoch, eine typische Wohnung liegt deutlich darunter.",
         "Am gleichen Ort sind gute Inserate oft doppelt so viele Nächte gebucht wie schwache."],
 "body": """
<h2>Die Zahlen pro Ort</h2>
<p>Die Tabelle zeigt alle aktiven Airbnb-Inserate eines Ortes über 12 Monate, von November 2025 bis Oktober 2026.</p>
<p class="swipe">Tabelle seitlich wischen →</p>
<div class="tbl wide"><table>
<thead><tr><th>Ort</th><th class="n">Inserate</th><th class="n">Auslastung</th><th class="n">Ø Nachtpreis</th><th class="n">Typische Wohnung</th></tr></thead>
<tbody>
<tr><td>Verbier (Val de Bagnes)</td><td class="n">762</td><td class="n">54 %</td><td class="n">CHF 401</td><td class="n">CHF 150</td></tr>
<tr><td>Zermatt</td><td class="n">875</td><td class="n">61 %</td><td class="n">CHF 389</td><td class="n">CHF 253</td></tr>
<tr><td>Lauterbrunnen, Wengen, Mürren</td><td class="n">535</td><td class="n">65 %</td><td class="n">CHF 343</td><td class="n">CHF 268</td></tr>
<tr><td>Interlaken</td><td class="n">315</td><td class="n">67 %</td><td class="n">CHF 327</td><td class="n">CHF 251</td></tr>
<tr><td>Grindelwald</td><td class="n">570</td><td class="n">72 %</td><td class="n">CHF 296</td><td class="n">CHF 206</td></tr>
<tr><td>St. Moritz</td><td class="n">372</td><td class="n">57 %</td><td class="n">CHF 293</td><td class="n">CHF 149</td></tr>
<tr><td>Stadt Luzern</td><td class="n">256</td><td class="n">76 %</td><td class="n">CHF 277</td><td class="n">CHF 219</td></tr>
<tr><td>Davos</td><td class="n">607</td><td class="n">54 %</td><td class="n">CHF 237</td><td class="n">CHF 117</td></tr>
<tr><td>Engelberg</td><td class="n">227</td><td class="n">61 %</td><td class="n">CHF 199</td><td class="n">CHF 150</td></tr>
<tr><td>Zürich</td><td class="n">1'970</td><td class="n">67 %</td><td class="n">CHF 183</td><td class="n">CHF 124</td></tr>
<tr><td>Genf</td><td class="n">704</td><td class="n">68 %</td><td class="n">CHF 149</td><td class="n">CHF 110</td></tr>
<tr><td>Lugano</td><td class="n">567</td><td class="n">64 %</td><td class="n">CHF 145</td><td class="n">CHF 112</td></tr>
<tr><td>Bern</td><td class="n">309</td><td class="n">66 %</td><td class="n">CHF 144</td><td class="n">CHF 117</td></tr>
</tbody></table></div>
<p>«Typische Wohnung» ist der Median: Die Hälfte der Inserate am Ort verlangt mehr, die andere Hälfte weniger. In der ganzen Schweiz liegt die <a href="../airbnb-auslastung-schweiz/">Auslastung</a> bei 59 % und der Durchschnittspreis bei CHF 199, gerechnet über 36'276 Inserate.</p>

<h2>Warum der Durchschnitt täuscht</h2>
<p><a href="../ferienwohnung-grindelwald-vermieten/">In Grindelwald</a> kostet eine Nacht im Durchschnitt CHF 296. Die typische Wohnung verlangt aber nur CHF 206. Der Grund sind grosse Chalets für acht oder zehn Personen, die den Durchschnitt nach oben ziehen. In Verbier ist der Abstand noch grösser: CHF 401 im Durchschnitt, CHF 150 im Median.</p>
<p>Wer eine 2-Zimmer-Wohnung besitzt, sollte deshalb mit dem Median rechnen und nicht mit dem Durchschnitt.</p>

<h2>Der Ort entscheidet nicht allein</h2>
<p>Am gleichen Ort liegen die Ergebnisse weit auseinander. In Grindelwald ist das schwächste Viertel der Inserate höchstens zu 38 % ausgelastet. Das stärkste Viertel erreicht 81 % und mehr. In Zermatt liegen die gleichen Werte bei 31 % und 75 %.</p>
<p>Den Unterschied machen Dinge, die Sie beeinflussen können: Fotos, Preise, die sich der Nachfrage anpassen, schnelle Antworten und gute Bewertungen.</p>

<h2>Rechenbeispiel: 2-Zimmer-Wohnung in Grindelwald</h2>
<div class="tbl"><table>
<tbody>
<tr><td>Nachtpreis im Jahresschnitt</td><td class="n">CHF 205</td></tr>
<tr><td>Auslastung 72 %, gebuchte Nächte</td><td class="n">263</td></tr>
<tr><td>Umsatz pro Jahr</td><td class="n">CHF 53'915</td></tr>
<tr><td><a href="../airbnb-oder-booking/">Plattformgebühr</a> 15,5 %</td><td class="n">− CHF 8'357</td></tr>
<tr><td><b>Bleibt nach Plattformgebühr</b></td><td class="n"><b>CHF 45'558</b></td></tr>
</tbody></table></div>
<p>Wer selbst vermietet, behält diesen Betrag und macht die Arbeit selbst. Mit unserem Komplett-Paket (21 %) bleiben CHF 35'991 pro Jahr, also rund CHF 3'000 pro Monat. Die Reinigung deckt die Reinigungsgebühr, die der Gast zusätzlich bezahlt.</p>

<h2>Was Sie vom Ertrag noch abziehen müssen</h2>
<ul>
<li>Nebenkosten: Heizung, Strom, Wasser, Internet</li>
<li><a href="../versicherung-ferienwohnung-vermieten/">Versicherungen</a> und Unterhalt der Wohnung</li>
<li>Verbrauchsmaterial wie Kaffee, Seife und WC-Papier</li>
<li>Steuern auf den Mieteinnahmen</li>
<li>Hypothekarzinsen, falls vorhanden</li>
</ul>
<p>Mehr dazu lesen Sie in den Artikeln zu <a href="../airbnb-einnahmen-versteuern/">Steuern</a> und zur <a href="../kurtaxe-ferienwohnung/">Kurtaxe</a>.</p>

<h2>So schätzen Sie Ihre eigene Wohnung ein</h2>
<p>Unser <a href="../../#rechner">Ertragsrechner</a> rechnet mit den Marktdaten von 24 Orten und passt den Nachtpreis der Wohnungsgrösse an. Für eine genaue Zahl schauen wir uns Ihre Wohnung kostenlos an. Eine Ertragsgarantie geben wir nicht, weil sie niemand seriös geben kann.</p>
""",
 "faq": [("Wie hoch ist die Auslastung von Airbnb-Wohnungen in der Schweiz?", "Im Durchschnitt 59 %, gerechnet über alle aktiven Inserate von November 2025 bis Oktober 2026. In Grindelwald sind es 72 %, in der Stadt Luzern 76 %, in Davos 54 %."),
         ("Wie viele Nächte ist eine Ferienwohnung in Grindelwald pro Jahr gebucht?", "Bei der durchschnittlichen Auslastung von 72 % sind es rund 263 Nächte. Das schwächste Viertel der Inserate erreicht höchstens 38 %, das stärkste Viertel mindestens 81 %."),
         ("Mit welchem Nachtpreis soll ich rechnen?", "Mit dem Median Ihres Ortes, nicht mit dem Durchschnitt. Grosse Chalets ziehen den Durchschnitt hoch. In Grindelwald liegt der Median bei CHF 206, der Durchschnitt bei CHF 296.")],
 "sources": [("GuestFavorites: Airbnb-Auslastung nach Ort in der Schweiz, Stand November 2026", "https://www.guestfavorites.com/airbnb-occupancy-rates-by-city-in-switzerland"),
             ("Airbnb Hilfe-Center: Servicegebühren", "https://www.airbnb.ch/help/article/1857")],
},
{
 "slug": "airbnb-oder-booking", "cat": "Vermieten", "mins": 5,
 "h1": "Airbnb oder Booking.com: Wo vermieten Sie Ihre Ferienwohnung besser?",
 "title": "Airbnb oder Booking.com: Gebühren für Gastgeber",
 "desc": "Gebühren, Auszahlung, Kurtaxe und Bewertungen im Vergleich. Mit Rechenbeispiel für eine Wohnung in Grindelwald und einer klaren Empfehlung.",
 "teaser": "Gebühren, Auszahlung, Kurtaxe und Bewertungen im Vergleich, mit Rechenbeispiel.",
 "lead": "Beide Plattformen kosten ähnlich viel. Die Unterschiede liegen bei der Zahlung, der Kurtaxe und den Bewertungen. Unsere Empfehlung: beide nutzen, mit einem gemeinsamen Kalender.",
 "photo": ("grindelwald-chalets-winter", "Zwei Chalets in Grindelwald im Winter, dahinter verschneite Berge",
           "Chalets in Grindelwald im Winter. Das Rechenbeispiel im Text geht von einer 2-Zimmer-Wohnung in Grindelwald aus."),
 "key": ["Airbnb zieht den meisten Gastgebern 15,5 % von der Auszahlung ab.",
         "Booking.com verlangt meist rund 15 % Provision, dazu kommt je nach Vertrag eine Zahlungsgebühr.",
         "Nur Airbnb zieht die Kurtaxe in zehn Kantonen automatisch ein. Bern, Wallis und Graubünden gehören nicht dazu.",
         "Wer beide Plattformen nutzt, braucht einen gemeinsamen Kalender. Sonst drohen Doppelbuchungen."],
 "body": """
<h2>Die Gebühren im Vergleich</h2>
<div class="tbl"><table>
<thead><tr><td></td><th>Airbnb</th><th>Booking.com</th></tr></thead>
<tbody>
<tr><td>Gebühr für Gastgeber</td><td>meist 15,5 %, sonst 14 bis 16 %</td><td>meist rund 15 %</td></tr>
<tr><td>Zahlungsabwicklung</td><td>inbegriffen</td><td>1,1 bis 3,1 % zusätzlich, wenn Booking.com die Zahlung abwickelt</td></tr>
<tr><td>Kurtaxe</td><td>automatisch in zehn Kantonen</td><td>rechnen Sie selbst ab</td></tr>
<tr><td>Bewertungen</td><td>Gast und Gastgeber bewerten sich gegenseitig</td><td>nur der Gast bewertet</td></tr>
</tbody></table></div>
<p>Airbnb stellt derzeit alle Gastgeber auf eine einheitliche Gebühr um. Sie wird ganz von der Auszahlung abgezogen. Für Gastgeber, die eine Verwaltungssoftware nutzen, ist dieses Modell bereits Pflicht. Das frühere Modell mit 3 % für den Gastgeber und einer separaten Gebühr für den Gast läuft aus.</p>
<p>Der genaue Satz bei Booking.com steht in Ihrem Vertrag mit Booking.com und hängt vom Standort und von Zusatzprogrammen ab.</p>

<h2>Rechenbeispiel: 3 Nächte in Grindelwald</h2>
<p>Eine 2-Zimmer-Wohnung, 3 Nächte zu CHF 205, also CHF 615 Übernachtungsumsatz.</p>
<div class="tbl"><table>
<thead><tr><td></td><th class="n">Airbnb</th><th class="n">Booking.com</th></tr></thead>
<tbody>
<tr><td>Übernachtungsumsatz</td><td class="n">CHF 615.00</td><td class="n">CHF 615.00</td></tr>
<tr><td>Gebühr</td><td class="n">− 95.33 (15,5 %)</td><td class="n">− 92.25 (15 %)</td></tr>
<tr><td>Zahlungsgebühr</td><td class="n">inbegriffen</td><td class="n">− 6.77 bis − 19.07</td></tr>
<tr><td><b>Bleibt bei Ihnen</b></td><td class="n"><b>CHF 519.67</b></td><td class="n"><b>CHF 504 bis 516</b></td></tr>
</tbody></table></div>
<p>Unter dem Strich ist der Unterschied klein. Wichtiger ist, auf welcher Plattform Ihre Wohnung <a href="../airbnb-auslastung-schweiz/">mehr Nächte füllt</a>.</p>

<h2>Der Preisüberwacher und Booking.com</h2>
<p>Im Mai 2025 hat der Preisüberwacher verfügt, dass Booking.com die Kommissionen für Schweizer Hotels um knapp ein Viertel senken muss. Die Senkung gilt drei Monate nach Rechtskraft und ist auf drei Jahre befristet. Booking.com konnte den Entscheid beim Bundesverwaltungsgericht anfechten. Die Verfügung nennt Hotels. Ob Ferienwohnungen davon profitieren, ist offen.</p>

<h2>Zahlung und Auszahlung</h2>
<p>Bei Airbnb zahlt der Gast immer an die Plattform. Airbnb überweist Ihnen den Betrag nach der Anreise. Bei Booking.com gibt es zwei Wege: Der Gast zahlt direkt an Sie, oder Booking.com wickelt die Zahlung gegen eine Gebühr ab.</p>

<h2>Kurtaxe: ein echter Unterschied</h2>
<p>Airbnb zieht die Tourismusabgaben in zehn Kantonen automatisch ein und leitet sie weiter: Luzern, Zürich, Basel-Landschaft, Basel-Stadt, Zug, Genf, Schaffhausen, Waadt, Freiburg und St. Gallen.</p>
<p>In allen anderen Kantonen und bei jeder Buchung über Booking.com rechnen Sie die Kurtaxe selbst ab. Das gilt zum Beispiel für das ganze Berner Oberland. Wie das geht, steht im Artikel zur <a href="../kurtaxe-ferienwohnung/">Kurtaxe</a>.</p>

<h2>Unsere Empfehlung: beide Plattformen, ein Kalender</h2>
<p>Mit beiden Plattformen erreichen Sie mehr Gäste. Entscheidend ist, dass eine Buchung auf der einen Plattform das Datum auf der anderen sofort sperrt. Ohne diese Verbindung kommt es früher oder später zu einer Doppelbuchung, und eine Absage kostet Bewertungen.</p>
<p>Wir führen Inserate auf Airbnb und Booking.com mit einem gemeinsamen Kalender. Die Konten bleiben Ihre. <a href="../../#preise">Zu den Konditionen</a></p>
""",
 "faq": [("Wie hoch ist die Airbnb-Gebühr für Gastgeber?", "Bei der einheitlichen Gebühr zahlen die meisten Gastgeber 15,5 %, die übrigen in der Regel 14 bis 16 %. Die Gebühr wird von der Auszahlung abgezogen. Airbnb stellt derzeit alle Gastgeber auf dieses Modell um."),
         ("Kann ich meine Wohnung gleichzeitig auf Airbnb und Booking.com anbieten?", "Ja. Wichtig ist ein gemeinsamer Kalender, damit eine Buchung das Datum auf der anderen Plattform sofort sperrt. Sonst riskieren Sie Doppelbuchungen."),
         ("Zieht Booking.com die Kurtaxe automatisch ein?", "Nein. Bei Booking.com rechnen Sie die Kurtaxe selbst ab. Airbnb zieht die Tourismusabgaben in zehn Kantonen automatisch ein.")],
 "sources": [("Airbnb Hilfe-Center: Servicegebühren", "https://www.airbnb.ch/help/article/1857"),
             ("Your.Rentals: Booking.com Gebühren für Gastgeber, 2025", "https://your.rentals/de/blog/booking-com-gebuehren-fuer-gastgeber-im-jahr-2025-preise-kosten/"),
             ("Preisüberwacher: Medienmitteilung vom 21. Mai 2025 zu Booking.com", "https://www.admin.ch/en/newnsb/3bBOJ_Hlr0i9FEX_Gy48M"),
             ("Airbnb: Tourismusabgaben, Mitteilung vom 8. Juli 2025", "https://news.airbnb.com/de/airbnb-zieht-tourismusabgaben-automatisch-ein-jetzt-auch-im-kanton-st-gallen/")],
},
{
 "slug": "selbst-vermieten-oder-verwaltung", "cat": "Vermieten", "mins": 5,
 "h1": "Selbst vermieten oder eine Verwaltung beauftragen?",
 "title": "Selbst vermieten oder Airbnb-Verwaltung? Die Kosten",
 "desc": "Was bei jeder Buchung anfällt, was eine Verwaltung kostet und wann sich welcher Weg lohnt. Mit sieben Fragen, die Sie jeder Verwaltung stellen sollten.",
 "teaser": "Aufwand, Kosten und sieben Fragen, die Sie jeder Verwaltung stellen sollten.",
 "lead": "Selbst vermieten bringt mehr Geld pro Buchung und kostet Zeit. Eine Verwaltung kostet Provision und nimmt Ihnen die Arbeit ab. Hier steht, wie Sie ehrlich vergleichen.",
 "photo": ("bett-weisse-waesche", "Benutztes Bett mit weisser Bettwäsche und mehreren Kissen",
           "Nach der Abreise beginnt die Arbeit: Bett abziehen, Wäsche waschen, frisch beziehen."),
 "key": ["Jede Buchung löst die gleiche Kette aus: Nachrichten, Anreise, Reinigung, Wäsche, Kontrolle, Bewertung.",
         "In der Schweiz verlangen Verwaltungen meist 15 bis 25 Prozent.",
         "Entscheidend ist, worauf der Prozentsatz gerechnet wird und was darin enthalten ist.",
         "Selbst vermieten lohnt sich, wenn Sie in der Nähe wohnen und auch abends erreichbar sind."],
 "body": """
<h2>Was bei jeder Buchung anfällt</h2>
<ul>
<li>Anfrage beantworten, oft auf Englisch und oft abends</li>
<li>Anreise erklären: Weg, Parkplatz, <a href="../self-check-in-ferienwohnung/">Schlüssel</a>, Hausordnung</li>
<li>Erreichbar sein, wenn der Gast den Schlüssel nicht findet oder die Heizung streikt</li>
<li>Nach der Abreise reinigen, Betten frisch beziehen, Wäsche waschen</li>
<li>Wohnung kontrollieren und Schäden festhalten</li>
<li>Verbrauchsmaterial nachfüllen</li>
<li>Gast bewerten, <a href="../kurtaxe-ferienwohnung/">Kurtaxe abrechnen</a>, <a href="../airbnb-einnahmen-versteuern/">Einnahmen für die Steuern</a> festhalten</li>
</ul>
<p>Dazu kommt die Arbeit im Hintergrund: Preise an Saison und Nachfrage anpassen, Kalender pflegen, Inserat und Fotos aktuell halten.</p>

<h2>Der Aufwand, ehrlich gerechnet</h2>
<p>Nehmen wir eine Wohnung in Grindelwald mit der <a href="../airbnb-auslastung-schweiz/">durchschnittlichen Auslastung</a> von 72 %. Das sind 263 gebuchte Nächte pro Jahr. Bleiben die Gäste im Schnitt drei Nächte, ergibt das rund 88 Gästewechsel. Die drei Nächte sind eine Annahme, in den Bergen sind kurze Aufenthalte häufig.</p>
<p>88 Wechsel heissen 88 Reinigungen und 88 Anreisen, verteilt über das ganze Jahr, auch an Weihnachten und in Ihren eigenen Ferien.</p>

<h2>Was eine Verwaltung kostet</h2>
<p>Marktüblich sind in der Schweiz 15 bis 25 Prozent. Die Zahl allein sagt wenig. Fragen Sie immer nach der Berechnungsgrundlage: Wird der Prozentsatz vor oder nach Abzug der <a href="../airbnb-oder-booking/">Plattformgebühr</a> gerechnet? Zählt die Reinigungsgebühr dazu?</p>
<p>Ein Beispiel mit unseren Konditionen: Nach der Plattformgebühr bleiben in Grindelwald <a href="../ferienwohnung-vermieten-ertrag/">rund CHF 45'558 pro Jahr</a>. Davon gehen im Komplett-Paket 21 % an uns, also CHF 9'567. Bei Ihnen bleiben CHF 35'991. Reinigung, Wäsche, Anreise und Kontrolle sind darin organisiert.</p>

<h2>Wann sich selbst vermieten lohnt</h2>
<ul>
<li>Sie wohnen in der Nähe und können schnell vor Ort sein.</li>
<li>Sie haben ein verlässliches Reinigungsteam.</li>
<li>Sie antworten gern auf Nachrichten, auch am Wochenende.</li>
<li>Sie vermieten nur wenige Wochen pro Jahr.</li>
</ul>

<h2>Wann eine Verwaltung sinnvoll ist</h2>
<ul>
<li>Die Wohnung liegt weit von Ihrem Wohnort entfernt.</li>
<li>Sie möchten das ganze Jahr vermieten.</li>
<li>Sie wollen Preise, die sich täglich der Nachfrage anpassen.</li>
<li>Sie möchten in Ihren Ferien nicht erreichbar sein müssen.</li>
</ul>

<h2>Sieben Fragen an jede Verwaltung</h2>
<ol>
<li>Worauf genau wird die Provision gerechnet?</li>
<li>Wer bezahlt die <a href="../ferienwohnung-reinigung-waesche/">Reinigung</a>, und zu welchem Preis?</li>
<li>Gibt es eine Einrichtungsgebühr oder eine Grundgebühr bei Leerstand?</li>
<li>Wem gehören die Inserate und die Konten auf den Plattformen?</li>
<li>Auf welches Konto zahlt die Plattform aus?</li>
<li>Wie lange ist die Kündigungsfrist?</li>
<li>Was steht im Monatsbericht?</li>
</ol>
<p>Unsere Antworten: Wir rechnen auf den Übernachtungsumsatz nach Plattformgebühr. Es gibt keine Einrichtungsgebühr und keine Kosten bei Leerstand. Die Konten bleiben Ihre, die Plattform zahlt direkt an Sie aus, und die Kündigungsfrist beträgt 3 Monate. <a href="../../#preise">Alle Konditionen</a></p>
""",
 "faq": [("Was kostet eine Airbnb-Verwaltung in der Schweiz?", "Marktüblich sind 15 bis 25 Prozent. Wichtig ist die Berechnungsgrundlage. Alpinhost verlangt 18 % im Basis-Paket und 21 % im Komplett-Paket, gerechnet auf den Übernachtungsumsatz nach Plattformgebühr."),
         ("Wem gehört das Inserat, wenn eine Verwaltung es führt?", "Das ist je nach Anbieter verschieden. Fragen Sie vor Vertragsabschluss danach. Bei Alpinhost bleiben Inserate und Konten beim Eigentümer.")],
 "sources": [("GuestFavorites: Airbnb-Auslastung in Grindelwald, Stand November 2026", "https://www.guestfavorites.com/airbnb-occupancy-rates-by-city-in-switzerland"),
             ("Alpinhost: Konditionen", "https://alpinhost.ch/#preise")],
},
{
 "slug": "self-check-in-ferienwohnung", "cat": "Vermieten", "mins": 6, "date": "2026-11-13",
 "h1": "Self-Check-in in der Ferienwohnung: Schlüsselbox, Smart Lock und Anreise-Nachricht",
 "title": "Self-Check-in: Schlüsselbox oder Smart Lock?",
 "desc": "Self-Check-in für Airbnb und Booking.com: Schlüsselbox und Smart Lock im Vergleich, Kosten, typische Pannen und eine Anreise-Nachricht als Vorlage.",
 "teaser": "Schlüsselbox und Smart Lock im Vergleich, typische Pannen und eine Vorlage für die Anreise-Nachricht.",
 "lead": "Mit Self-Check-in kommen Gäste ohne Schlüsselübergabe in die Wohnung, auch um 23 Uhr. Eine Schlüsselbox gibt es ab rund 30 Franken. Ob die Anreise klappt, entscheidet aber meist die Nachricht, die Sie vorher schicken.",
 "photo": ("schluesselboxen-zahlencode-wand", "Mehrere Schlüsselboxen mit Zahlencode an einer Backsteinmauer, zwei davon geöffnet",
           "Schlüsselboxen mit Zahlencode an einer Hauswand. Im Fach hinter der Klappe liegt der Schlüssel."),
 "key": ["Self-Check-in gehört auf Airbnb weltweit zu den zehn meistgesuchten Ausstattungen (Zahlen 2025).",
         "Eine Schlüsselbox mit Zahlencode kostet ab rund CHF 30, ein elektronisches Schloss mit Codefeld CHF 238 bis 438 (Beispielpreise November 2026).",
         "Airbnb zeigt Gästen die genaue Anleitung erst 24 bis 48 Stunden vor der Anreise.",
         "Die häufigsten Pannen: Box geht nicht auf, Gastgeber nicht erreichbar, Eingang nicht gefunden."],
 "body": """
<h2>Was Self-Check-in bedeutet</h2>
<p>Self-Check-in heisst: Gäste kommen in die Wohnung, ohne dass jemand vor Ort sein muss. Sie reisen an, wann der Zug oder der Flug es erlaubt, und Sie müssen keinen Abend freihalten. Auf Airbnb gehört Self-Check-in weltweit zu den zehn meistgesuchten Ausstattungen (Zahlen 2025). Viele Gäste filtern die Suche danach.</p>
<p>Airbnb zählt vier Wege als Self-Check-in:</p>
<ul>
<li><strong>Schlüsselbox:</strong> ein kleiner Tresor mit Zahlencode, in dem der Schlüssel liegt</li>
<li><strong>Tastenfeld:</strong> ein elektronisches Schloss, das sich mit einem Code öffnet</li>
<li><strong>Smart Lock:</strong> ein Schloss mit Internetverbindung, das sich per Code oder App öffnet</li>
<li><strong>Personal im Haus:</strong> zum Beispiel eine Rezeption, die rund um die Uhr besetzt ist</li>
</ul>
<p>Booking.com kennt ähnliche Angaben: Türcode, Schlüsselbox, Rezeption, persönliche Übergabe oder ein vereinbarter Ort für den Schlüssel. Tragen Sie die Art der Anreise auf beiden Plattformen ein, sonst sehen Gäste sie nicht.</p>

<h2>Schlüsselbox oder Smart Lock: der Vergleich</h2>
<div class="tbl wide"><table>
<thead><tr><td></td><th>Schlüsselbox</th><th>Elektronisches Schloss mit Codefeld</th><th>Persönliche Übergabe</th></tr></thead>
<tbody>
<tr><td>Anschaffung (Beispielpreise November 2026)</td><td>ab rund CHF 30</td><td>CHF 238 bis 438</td><td>CHF 0</td></tr>
<tr><td>Eigener Code pro Gast</td><td>nur, wenn jemand den Code vor Ort umstellt</td><td>ja, aus der Ferne, mit Ablaufdatum</td><td>nicht nötig</td></tr>
<tr><td>Strom und Verbindung</td><td>nicht nötig</td><td>Batterien, je nach Modell Internet</td><td>nicht nötig</td></tr>
<tr><td>Anreise spät am Abend</td><td>ja</td><td>ja</td><td>nur, wenn jemand wartet</td></tr>
<tr><td>Typische Pannen</td><td>falscher Code, klemmendes Zahlenrad, Schlüssel nicht zurückgelegt, Frost</td><td>leere Batterie, Verbindung weg, Code zu spät verschickt</td><td>Verspätung des Gastes, niemand erreichbar</td></tr>
</tbody></table></div>
<p>So setzen sich die Beispielpreise zusammen: Eine Schlüsselbox für die Wand mit vierstelligem Zahlencode kostet im Schweizer Onlinehandel CHF 30.50. Ein elektronisches Schloss zum Nachrüsten kostet beim Hersteller je nach Modell CHF 149 bis 349, das Codefeld dazu CHF 89. Zusammen ergibt das CHF 238 bis 438. Die Montage ist nicht eingerechnet.</p>
<p>Als Faustregel: Für eine einzelne Wohnung mit wenigen Wechseln genügt eine gute Schlüsselbox. Bei vielen Wechseln, mehreren Wohnungen oder wenn niemand in der Nähe wohnt, lohnt sich das elektronische Schloss, weil Sie Codes aus der Ferne vergeben und sperren.</p>

<h2>Die Schlüsselbox richtig einsetzen</h2>
<ul>
<li>Montieren Sie die Box fest an der Wand, nicht an einem Geländer oder Rohr, und nicht direkt neben der Wohnungstür mit Namensschild.</li>
<li>Wählen Sie einen Ort mit Licht. Im Dunkeln lassen sich Zahlenräder kaum ablesen.</li>
<li>Stellen Sie nach jedem Gast einen neuen Code ein. Vier Stellen ergeben 10'000 mögliche Codes, das Geburtsjahr und 1234 gehören nicht dazu.</li>
<li>In einem Mehrfamilienhaus sprechen Sie den Ort vorher mit der Hausverwaltung ab.</li>
<li>In den Bergen: Wählen Sie eine wetterfeste Box an einer geschützten Stelle. Schnee und Eis blockieren Zahlenräder und Klappen. Mehr dazu im Artikel <a href="../ferienwohnung-winter-vermieten/">Ferienwohnung im Winter vermieten</a>.</li>
<li>Hinterlegen Sie einen zweiten Schlüssel bei einer Person im Ort.</li>
</ul>

<h2>Das elektronische Schloss richtig einsetzen</h2>
<ul>
<li>Vergeben Sie für jede Buchung einen eigenen Code, der nach der Abreise abläuft. Das gilt für jede Art von Self-Check-in.</li>
<li>Wechseln Sie die Batterien nach Plan und nicht erst bei der Warnung. Bei einem verbreiteten Modell hält die Batterie des Codefelds bis 18 Monate.</li>
<li>Prüfen Sie vor dem Kauf, ob das Schloss zu Ihrem Zylinder und zu Ihrer Tür passt.</li>
<li>Behalten Sie einen Weg ohne Strom: einen normalen Schlüssel in einer Schlüsselbox oder bei einer Person im Ort.</li>
<li>Bei einer Haustür mit Gegensprechanlage braucht es eine Lösung für beide Türen.</li>
</ul>

<h2>Was bei der Anreise schiefgeht</h2>
<p>Eine im Mai 2026 veröffentlichte Auswertung von 37'359 Gästeanfragen an Ferienunterkünfte zeigt: 3'822 davon drehten sich um den Check-in, also rund jede zehnte. Die drei häufigsten Probleme:</p>
<ol>
<li>Die Schlüsselbox oder das Schloss geht nicht auf.</li>
<li>Der Gastgeber ist nicht erreichbar.</li>
<li>Der Gast findet den Eingang nicht.</li>
</ol>
<p>Gäste scheitern also selten am Self-Check-in an sich. Sie scheitern an einem falschen Code, an einer ungenauen Beschreibung oder daran, dass es keinen Plan B gibt. Alle drei Punkte lösen Sie mit einer guten Anreise-Nachricht.</p>

<h2>Die Anreise-Nachricht: Checkliste</h2>
<ul>
<li>Check-in-Zeit und was gilt, wenn der Gast früher kommt</li>
<li>Genaue Adresse mit Kartenlink, dazu Stockwerk und Name an der Klingel</li>
<li>Foto des Eingangs und der Schlüsselbox, bei Tageslicht aufgenommen</li>
<li>Schritt für Schritt: Code eingeben, Klappe öffnen, Schlüssel nehmen, Box wieder schliessen</li>
<li>Parkplatz oder Weg vom Bahnhof, in autofreien Orten wie Wengen und Mürren mit Gehzeit</li>
<li>WLAN-Name und Passwort</li>
<li>Telefonnummer für den Notfall und was der Gast tun soll, wenn die Tür nicht aufgeht</li>
</ul>
<p>Airbnb zeigt die Art der Anreise sofort nach der Buchung, die genaue Anleitung aber erst 24 bis 48 Stunden vor dem Check-in. Bis zur Anreise ist diese Nachricht oft nach unten gerutscht. Schicken Sie darum am Vortag oder am Morgen der Anreise eine eigene, kurze Nachricht. Bei Booking.com lässt sich hinterlegen, wann Sie die Anleitung schicken: sofort, einen Monat vorher, eine Woche vorher oder am Anreisetag.</p>

<h3>Vorlage zum Anpassen</h3>
<p><em>Beispiel:</em> «Guten Tag Frau Muster, morgen ist es so weit. Check-in ab 16 Uhr. Adresse: Dorfstrasse 1, 2. Stock, Klingel Alpenblick (Kartenlink). Die Schlüsselbox hängt rechts neben der Haustür, siehe Foto. Code: 4071. Bitte legen Sie den Schlüssel bei der Abreise zurück und verdrehen Sie die Zahlen. WLAN: Alpenblick, Passwort im Wohnzimmer. Geht etwas nicht, erreichen Sie uns unter [Ihre Nummer], auch abends.»</p>
<p>Schreiben Sie die Nachricht in der Sprache des Gastes, mindestens auf Deutsch und Englisch. Speichern Sie sie als Vorlage, dann ist sie mit zwei Klicks verschickt.</p>

<h2>Vor dem ersten Gast: einmal selbst anreisen</h2>
<p>Bitten Sie eine Person, die die Wohnung nicht kennt, nur mit Ihrer Nachricht hineinzukommen, am besten bei Dunkelheit. Wo sie zögert, fehlt ein Satz oder ein Foto. Was sonst in die Wohnung gehört, steht in der <a href="../ferienwohnung-einrichten-checkliste/">Checkliste zum Einrichten</a>. Und wer nachts ans Telefon geht, wenn der Code nicht stimmt, ist eine der Fragen im Vergleich <a href="../selbst-vermieten-oder-verwaltung/">selbst vermieten oder Verwaltung</a>.</p>
<p>Alpinhost richtet für Ihre Wohnung eine Schlüsselbox oder ein Smart Lock ein, vergibt einen Code pro Gast und schickt die Anreise-Informationen in der Sprache des Gastes. <a href="../../#kontakt">Wohnung prüfen lassen</a></p>
""",
 "faq": [("Was ist Self-Check-in bei Airbnb?", "Self-Check-in bedeutet, dass Gäste ohne Gastgeber in die Unterkunft kommen. Airbnb zählt dazu Schlüsselbox, Tastenfeld, Smart Lock und Personal im Haus, das rund um die Uhr erreichbar ist."),
         ("Wann erhalten Gäste den Code für die Schlüsselbox?", "Airbnb zeigt die Art der Anreise sofort nach der Buchung und die genaue Anleitung 24 bis 48 Stunden vor dem Check-in. Schicken Sie zusätzlich am Vortag oder am Morgen der Anreise eine eigene Nachricht mit Code, Foto und Notfallnummer."),
         ("Schlüsselbox oder Smart Lock: Was ist besser?", "Eine Schlüsselbox kostet ab rund CHF 30 und braucht keinen Strom, der Code muss aber vor Ort umgestellt werden. Ein elektronisches Schloss mit Codefeld kostet CHF 238 bis 438 (Beispielpreise November 2026) und erlaubt einen eigenen Code pro Gast aus der Ferne. Bei vielen Wechseln oder wenn niemand in der Nähe wohnt, lohnt sich das elektronische Schloss."),
         ("Was tun, wenn der Gast nicht in die Wohnung kommt?", "Wichtig ist ein Plan B, der in der Anreise-Nachricht steht: eine Telefonnummer, die auch abends erreichbar ist, und ein zweiter Schlüssel bei einer Person im Ort oder in einer zweiten Schlüsselbox.")],
 "sources": [("Airbnb-Hilfe: Was bedeutet Self-Check-in?", "https://www.airbnb.com/help/article/1207"),
             ("Airbnb-Hilfe: Check-in-Anleitung zum Inserat hinzufügen", "https://www.airbnb.com/help/article/1926"),
             ("Airbnb Resource Center: How to provide self check-in for smooth arrivals, 31. August 2026", "https://www.airbnb.com/resources/hosting-homes/a/how-to-provide-self-check-in-for-smooth-arrivals-238"),
             ("Booking.com Connectivity: Check-in Methods", "https://developers.booking.com/connectivity/docs/checkin-methods-api/methods-descriptions"),
             ("Touch Stay: What 3,822 Guest Questions Reveal About What Goes Wrong at Check-in, 25. Mai 2026", "https://touchstay.com/blog/self-check-in-rental-problems"),
             ("Galaxus: Schlüsselbox mit vierstelligem Zahlencode, Preis abgerufen am 13. November 2026", "https://www.galaxus.ch/en/s4/product/master-lock-5401eurd-key-safes-key-cabinets-3454677"),
             ("Nuki: Preise und Angaben zu Smart Lock und Keypad für Ferienwohnungen, abgerufen am 13. November 2026", "https://nuki.io/en-ch/solutions/for-your-vacation-rental/find-your-setup")],
},
{
 "slug": "airbnb-einnahmen-versteuern", "cat": "Kosten und Steuern", "mins": 6,
 "h1": "Airbnb-Einnahmen versteuern: Was Eigentümer in der Schweiz wissen müssen",
 "title": "Airbnb Steuern Schweiz: Einnahmen richtig versteuern",
 "desc": "Einkommenssteuer, Pauschalabzug im Kanton Bern, Mehrwertsteuer ab CHF 100'000 und die Abschaffung des Eigenmietwerts. Verständlich erklärt, mit Quellen.",
 "teaser": "Einkommenssteuer, Pauschalabzug, Mehrwertsteuer und Eigenmietwert, verständlich erklärt.",
 "lead": "Mieteinnahmen aus der Ferienwohnung sind steuerbares Einkommen. Wie viel Sie abziehen dürfen, regelt jeder Kanton selbst. Wir zeigen die Grundsätze und das Beispiel des Kantons Bern.",
 "photo": ("schweizer-muenzen", "Ein Haufen Schweizer Münzen, vor allem Franken und Rappen",
           "Schweizer Münzen: Jeder Franken Mietertrag aus der Ferienwohnung gehört in die Steuererklärung."),
 "key": ["Mieteinnahmen aus Airbnb und Booking.com sind steuerbares Einkommen.",
         "Im Kanton Bern werden pauschal 33,33 % des Bruttomietertrags abgezogen, automatisch.",
         "Ab CHF 100'000 Umsatz pro Jahr werden Sie mehrwertsteuerpflichtig. Für Ferienwohnungen gilt der Sondersatz von 3,8 %.",
         "Die Abschaffung des Eigenmietwerts ist beschlossen, aber noch nicht in Kraft."],
 "body": """
<p class="note">Dieser Artikel ist eine Orientierung und keine Steuerberatung. Die Regeln unterscheiden sich von Kanton zu Kanton. Verbindlich sind die Wegleitung Ihres Kantons und die Auskunft Ihrer Steuerverwaltung.</p>

<h2>Einkommenssteuer: der Grundsatz</h2>
<p>Wer eine möblierte Wohnung vermietet, versteuert den Mietzins als Einkommen. Das gilt für die klassische Ferienwohnung genauso wie für die Vermietung über Airbnb oder Booking.com. In die Steuererklärung gehört der Bruttomietertrag, also alle Mieteinnahmen inklusive Nebenkosten.</p>
<p>Besteuert wird die Liegenschaft dort, wo sie steht. Wer in Zürich wohnt und eine Wohnung in Grindelwald vermietet, versteuert den Ertrag im Kanton Bern.</p>

<h2>Das Beispiel Kanton Bern: 33,33 % Pauschalabzug</h2>
<p>Im Kanton Bern werden die Kosten der möblierten Vermietung mit einem pauschalen Abzug von 33,33 % des Bruttomietertrags berücksichtigt. Sie müssen den Abzug nicht verlangen, die Steuerverwaltung gewährt ihn automatisch.</p>
<p>Mit der Pauschale sind unter anderem abgegolten:</p>
<ul>
<li>Heizung, Wasser und Strom</li>
<li>Abnutzung von Möbeln, Wäsche und Geschirr</li>
<li>Reinigung</li>
<li>Kurtaxe und Tourismusabgaben</li>
<li>Vermittlungsgebühren, Werbung und Inserate</li>
<li>Internet und Mobiliarversicherung</li>
</ul>
<p>Diese Kosten können Sie nicht zusätzlich als tatsächliche Kosten abziehen. Der Unterhalt der Liegenschaft selbst bleibt nach den üblichen Regeln abziehbar.</p>

<h2>Eigennutzung und Eigenmietwert</h2>
<p>Für die Zeit, in der Sie die Wohnung selbst nutzen können, versteuern Sie heute den Eigenmietwert. Für die vermieteten Wochen wird er gekürzt. Die Berner Steuerverwaltung rechnet dazu ein Beispiel vor:</p>
<div class="tbl"><table>
<tbody>
<tr><td>Eigenmietwert für 12 Monate</td><td class="n">CHF 12'000</td></tr>
<tr><td>Abzug für 3 vermietete Monate</td><td class="n">− CHF 3'000</td></tr>
<tr><td>Korrigierter Eigenmietwert</td><td class="n">CHF 9'000</td></tr>
<tr><td>Mieteinnahmen aus 3 Monaten</td><td class="n">CHF 6'000</td></tr>
<tr><td>Pauschalabzug 33,33 %</td><td class="n">− CHF 2'000</td></tr>
</tbody></table></div>

<h2>Die Abschaffung des Eigenmietwerts</h2>
<p>Am 28. September 2025 haben die Stimmberechtigten die Abschaffung des Eigenmietwerts mit 57,7 % angenommen. Die Kantone dürfen neu eine besondere Liegenschaftssteuer auf Zweitliegenschaften einführen. Bei vermieteten Liegenschaften bleibt der Unterhalt abziehbar.</p>
<p>Das neue Recht ist noch nicht in Kraft. Den Zeitpunkt legt der Bundesrat fest. Bis dahin gelten die heutigen Regeln. Welche Kantone eine Zweitwohnungssteuer einführen und wie hoch sie ausfällt, ist noch offen.</p>

<h2>Mehrwertsteuer: ab CHF 100'000 Umsatz</h2>
<p>Die Vermietung von Ferienwohnungen gilt bei der Mehrwertsteuer als Beherbergung. Wer damit pro Jahr mehr als CHF 100'000 Umsatz erzielt, muss sich registrieren. Es gilt der Sondersatz von 3,8 %, egal ob Sie direkt oder über eine Plattform vermieten.</p>
<p>Achtung bei mehreren Wohnungen: Auch der Wert der eigenen Nutzung kann zum Umsatz zählen. Wer nahe an der Grenze liegt, sollte das jedes Jahr prüfen.</p>

<h2>Wann aus der Vermietung ein Gewerbe wird</h2>
<p>Wer mehrere Wohnungen vermietet oder Leistungen wie in einem Hotel anbietet, kann steuerlich als selbständig erwerbend gelten. Dann fallen auch Sozialversicherungsbeiträge an. Die Steuerverwaltung beurteilt das im Einzelfall. Fragen Sie nach, bevor Sie eine zweite oder dritte Wohnung dazunehmen.</p>

<h2>Was Sie aufbewahren sollten</h2>
<ul>
<li>Alle Abrechnungen der Plattformen</li>
<li>Die Anzahl der vermieteten und der selbst genutzten Nächte</li>
<li>Belege für Unterhalt und Reparaturen</li>
<li>Die Abrechnungen der Kurtaxe</li>
</ul>
<p>Unsere Kunden erhalten jeden Monat einen Bericht mit allen Buchungen und Einnahmen. Damit sind die Belege für die Steuererklärung schon beisammen.</p>
""",
 "faq": [("Muss ich Airbnb-Einnahmen in der Schweiz versteuern?", "Ja. Mieteinnahmen aus der Vermietung möblierter Wohnungen sind steuerbares Einkommen. In die Steuererklärung gehört der Bruttomietertrag. Welche Kosten Sie abziehen dürfen, regelt Ihr Kanton."),
         ("Wie hoch ist der Pauschalabzug für Ferienwohnungen im Kanton Bern?", "33,33 % des Bruttomietertrags. Die Steuerverwaltung gewährt den Abzug automatisch. Er deckt unter anderem Heizung, Reinigung, Abnutzung der Möbel, Kurtaxe und Vermittlungsgebühren."),
         ("Ab wann bin ich mit einer Ferienwohnung mehrwertsteuerpflichtig?", "Ab einem Umsatz von CHF 100'000 pro Jahr. Für die Beherbergung in Ferienwohnungen gilt der Sondersatz von 3,8 %.")],
 "sources": [("Steuerverwaltung des Kantons Bern, TaxInfo: Vermietung möblierter Liegenschaften", "https://www.taxinfo.sv.fin.be.ch/taxinfo/649588d4-12bb-415e-aa77-4c26e39284a7"),
             ("Steuerverwaltung des Kantons Bern, Wegleitung 2024: Vermietung Ferienwohnung (Rechenbeispiel, Pauschalabzug selbst berechnet)", "https://www.wegleitung.sv.fin.be.ch/de/start/np2024/grundstuecke-im-privatvermoegen/vermietete-ferienwohnungen.html"),
             ("Eidgenössische Steuerverwaltung: Mehrwertsteuersätze", "https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz"),
             ("Forvis Mazars: Mehrwertsteuer und Privatpersonen, November 2025", "https://www.forvismazars.com/ch/de/insights/swiss-tax-newsletter/swiss-tax-newsletter-november-2025/mwst-privatpersonen-auswirkungen-auf-immobilien"),
             ("Zürcher Kantonalbank: Abschaffung des Eigenmietwerts", "https://www.zkb.ch/de/blog/immobilien/abschaffung-eigenmietwert-was-passiert.html"),
             ("SRF: Abstimmungsresultat vom 28. September 2025", "https://www.srf.ch/news/schweiz/abstimmung-28-september-57-7-prozent-sagen-ja-zur-abschaffung-des-eigenmietwerts")],
},
{
 "slug": "kurtaxe-ferienwohnung", "cat": "Kosten und Steuern", "mins": 5,
 "h1": "Kurtaxe für Ferienwohnungen: Wer zahlt, wer rechnet ab?",
 "title": "Kurtaxe bei Airbnb und Ferienwohnung: Wer zahlt was?",
 "desc": "Was die Kurtaxe ist, wie hoch sie in Grindelwald ausfällt, was in Interlaken gilt und in welchen zehn Kantonen Airbnb sie automatisch einzieht.",
 "teaser": "Was in Grindelwald und Interlaken gilt und wo Airbnb die Kurtaxe automatisch einzieht.",
 "lead": "Die Kurtaxe zahlt der Gast. Abrechnen müssen meistens Sie. Wir erklären das System am Beispiel von Grindelwald und Interlaken und zeigen, wo Airbnb Ihnen die Arbeit abnimmt.",
 "photo": ("bahnhof-interlaken-ost", "Bahnhofgebäude Interlaken Ost mit Vorplatz, dahinter bewaldete Berge",
           "Bahnhof Interlaken Ost: Wer hier ankommt und in einer Ferienwohnung übernachtet, zahlt Kurtaxe und hat Anrecht auf die Gästekarte Interlaken."),
 "key": ["Die Kurtaxe wird pro Person und Nacht erhoben. Der Gast zahlt, der Vermieter rechnet ab.",
         "In Grindelwald beträgt sie CHF 3.70 pro Nacht (Stand 2022), dazu kommt CHF 1.00 kantonale Beherbergungsabgabe.",
         "Im Raum Interlaken müssen sich Vermieter registrieren und brauchen eine Bewilligung der Gemeinde.",
         "Airbnb zieht die Abgabe in zehn Kantonen automatisch ein. Der Kanton Bern gehört nicht dazu."],
 "body": """
<h2>Was die Kurtaxe ist</h2>
<p>Die Kurtaxe ist eine Abgabe, die Gäste pro Übernachtung bezahlen. Je nach Ort heisst sie auch Gästetaxe oder Tourismusabgabe. Mit dem Geld finanzieren die Gemeinden Angebote für Gäste. Der Vermieter zieht die Abgabe ein und liefert sie der Gemeinde oder der Tourismusorganisation ab.</p>
<p>Oft kommen weitere Abgaben dazu. Im Kanton Bern sind es bis zu drei: die Kurtaxe der Gemeinde, die kantonale Beherbergungsabgabe und eine Tourismusförderungsabgabe.</p>

<h2>Beispiel Grindelwald</h2>
<div class="tbl"><table>
<tbody>
<tr><td>Kurtaxe pro Übernachtung</td><td class="n">CHF 3.70</td></tr>
<tr><td>Kantonale Beherbergungsabgabe pro Übernachtung</td><td class="n">CHF 1.00</td></tr>
<tr><td>Pauschalkurtaxe bei Eigennutzung, 2-Zimmer-Wohnung</td><td class="n">CHF 444 pro Jahr</td></tr>
<tr><td>Pauschalkurtaxe bei Eigennutzung, 3-Zimmer-Wohnung</td><td class="n">CHF 592 pro Jahr</td></tr>
</tbody></table></div>
<p>Die Zahlen haben den Stand April 2022. Die Pauschale für die eigene Nutzung rechnet die Gemeinde mit 40 Nächten pro Bett und Jahr. Wer seine Wohnung gegen Entgelt vermietet, zahlt zusätzlich eine Tourismusförderungsabgabe. Fragen Sie die aktuellen Ansätze bei der Gemeinde nach, sie können sich seither geändert haben.</p>

<h2>Beispiel Interlaken</h2>
<p>In Interlaken, Matten, Unterseen, Wilderswil, Gsteigwiler und Saxeten gilt eine Registrierungspflicht. Vermieter von Ferienwohnungen brauchen zuerst eine Bewilligung der Standortgemeinde. Danach melden sie die Unterkunft bei der Tourismus-Organisation Interlaken an. Das gilt unabhängig davon, über welche Plattform vermietet wird.</p>
<p>Abgerechnet werden die Kurtaxe, die kantonale Beherbergungsabgabe und die Tourismusförderungsabgabe. Im Gegenzug hat jeder Gast Anrecht auf die Gästekarte Interlaken. Die Registrierungspflicht gilt auch für Eigentümer, die ihre Wohnung nur selbst nutzen. Sie zahlen eine Pauschalkurtaxe.</p>

<h2>Wo Airbnb die Abgabe automatisch einzieht</h2>
<p>In zehn Kantonen zieht Airbnb die Tourismusabgabe bei jeder Buchung vom Gast ein und leitet sie weiter:</p>
<ul>
<li>Luzern, Zürich, Zug, Schaffhausen, St. Gallen</li>
<li>Basel-Stadt und Basel-Landschaft</li>
<li>Genf, Waadt und Freiburg</li>
</ul>
<p>Im Kanton Luzern gilt das seit dem 1. Januar 2020 für die kantonale Beherbergungsabgabe, im Kanton St. Gallen seit dem 14. Juli 2025. In allen anderen Kantonen rechnen Sie selbst ab. Das betrifft das Berner Oberland, das Wallis, Graubünden und das Tessin. Bei Buchungen über Booking.com rechnen Sie überall selbst ab.</p>

<h2>So gehen Sie vor</h2>
<ol>
<li>Fragen Sie bei der Gemeinde nach, welche Abgaben gelten und wo Sie sich anmelden müssen.</li>
<li>Weisen Sie die Kurtaxe im Inserat aus oder rechnen Sie sie in den Preis ein.</li>
<li>Führen Sie eine Liste mit Personen und Nächten pro Buchung.</li>
<li>Rechnen Sie zum verlangten Termin ab und bewahren Sie die Abrechnung auf.</li>
</ol>
<p>Im Kanton Bern ist die Kurtaxe mit dem <a href="../airbnb-einnahmen-versteuern/">Pauschalabzug von 33,33 %</a> bei den Steuern bereits abgegolten.</p>
<p>Unsere Kunden erhalten jeden Monat einen Bericht mit allen Buchungen, Personen und Nächten. Damit ist die Abrechnung der Kurtaxe in wenigen Minuten erledigt.</p>
""",
 "faq": [("Wer bezahlt die Kurtaxe bei einer Ferienwohnung?", "Der Gast. Der Vermieter zieht die Abgabe ein und liefert sie der Gemeinde oder der Tourismusorganisation ab. In zehn Kantonen übernimmt Airbnb den Einzug automatisch."),
         ("Wie hoch ist die Kurtaxe in Grindelwald?", "Sie beträgt CHF 3.70 pro Übernachtung (Stand April 2022). Dazu kommt die kantonale Beherbergungsabgabe von CHF 1.00. Die aktuellen Ansätze nennt die Gemeinde."),
         ("Zieht Airbnb die Kurtaxe im Berner Oberland automatisch ein?", "Nein. Der Kanton Bern gehört nicht zu den zehn Kantonen mit einer Vereinbarung. In Grindelwald, Interlaken oder Wengen rechnen Vermieter die Kurtaxe selbst ab.")],
 "sources": [("Gemeinde Grindelwald: Infoblatt Steuern, Gebühren, Abgaben, Stand 1. April 2022", "https://www.gemeinde-grindelwald.ch/wp-content/uploads/2020/06/Infoblatt-2022-Steuern-Gebuehren-Abgaben.pdf"),
             ("Interlaken Tourismus: Informationen für Beherbergende", "https://www.interlaken.swiss/info-service/informationen-fuer-beherbergende"),
             ("Airbnb: Tourismusabgaben, Mitteilung vom 8. Juli 2025", "https://news.airbnb.com/de/airbnb-zieht-tourismusabgaben-automatisch-ein-jetzt-auch-im-kanton-st-gallen/"),
             ("Airbnb Hilfe-Center: Die Stadt Luzern", "https://www.airbnb.ch/help/article/3821"),
             ("Steuerverwaltung des Kantons Bern, TaxInfo: Vermietung möblierter Liegenschaften", "https://www.taxinfo.sv.fin.be.ch/taxinfo/649588d4-12bb-415e-aa77-4c26e39284a7")],
},
{
 "slug": "airbnb-regeln-bewilligung-schweiz", "cat": "Kosten und Steuern", "mins": 6,
 "h1": "Brauche ich eine Bewilligung? Regeln für Airbnb in der Schweiz",
 "title": "Airbnb in der Schweiz: Regeln, Bewilligung, 90 Nächte",
 "desc": "Zweitwohnungsgesetz, 90-Nächte-Regel in Luzern, Berner Altstadt, Interlaken, Stockwerkeigentum und Meldepflicht. Die wichtigsten Regeln im Überblick.",
 "teaser": "Zweitwohnungsgesetz, 90-Nächte-Regeln, Stockwerkeigentum und Meldepflicht im Überblick.",
 "lead": "Eine nationale Airbnb-Bewilligung gibt es nicht. Ob und wie lange Sie vermieten dürfen, entscheiden Bund, Gemeinde und die eigene Hausgemeinschaft. Hier sind die Regeln, die Sie prüfen müssen.",
 "photo": ("bern-kramgasse-zytglogge", "Kramgasse in der Berner Altstadt mit Lauben, Fahnen und dem Zytglogge-Turm",
           "Kramgasse in der Berner Altstadt mit dem Zytglogge. Für die Altstadt haben die Stimmberechtigten 2022 eine Obergrenze von 90 Nächten angenommen."),
 "key": ["Es gibt keine nationale Bewilligung. Entscheidend sind Gemeinde, Zone und Hausreglement.",
         "In der Stadt Luzern gilt seit 2025 eine Obergrenze von 90 Nächten pro Jahr, mit Ausnahmen.",
         "Im Raum Interlaken brauchen Vermieter eine Bewilligung der Gemeinde.",
         "Im Stockwerkeigentum kann das Reglement die Kurzzeitvermietung verbieten."],
 "body": """
<p class="note">Dieser Artikel ist ein Überblick und keine Rechtsberatung. Die Regeln ändern sich laufend. Verbindlich ist die Auskunft Ihrer Gemeinde.</p>

<h2>1. Das Zweitwohnungsgesetz</h2>
<p>In Gemeinden mit mehr als 20 % Zweitwohnungen dürfen keine neuen Zweitwohnungen mehr bewilligt werden. Das betrifft die meisten Ferienorte in den Bergen. Ausführlich erklärt im Artikel <a href="../zweitwohnungsgesetz-ferienwohnung/">Zweitwohnungsgesetz für Eigentümer</a>. Für Eigentümer ist wichtig, wann die Wohnung entstanden ist:</p>
<ul>
<li><b>Altrechtliche Wohnungen:</b> Wohnungen, die am 11. März 2012 bestanden oder bewilligt waren, sind in der Art der Wohnnutzung frei. Sie dürfen als Ferienwohnung vermietet werden.</li>
<li><b>Neuere Wohnungen:</b> Sie wurden nur als Erstwohnung oder als touristisch bewirtschaftete Wohnung bewilligt. Was erlaubt ist, steht in der Baubewilligung und im Grundbuch.</li>
</ul>

<h2>2. Regeln der Städte und Gemeinden</h2>
<h3>Stadt Luzern: 90 Nächte</h3>
<p>Seit dem 1. Januar 2025 gilt in der Stadt Luzern ein Reglement über die Kurzzeitvermietung. Wohnungen dürfen höchstens 90 Nächte pro Kalenderjahr für Aufenthalte unter drei Monaten vermietet werden. Das Angebot muss der Stadt gemeldet werden, und die Registrierungsnummer gehört ins Inserat.</p>
<p>Ausgenommen sind Tourismuszonen und Landwirtschaftszonen. Ausgenommen ist auch, wer Zimmer am eigenen Hauptwohnsitz vermietet und damit keinen missbräuchlichen Gewinn erzielt. Mehr als 90 Nächte sind möglich, wenn die Räume seit 2010 nicht als Wohnraum genutzt wurden. Dafür braucht es eine Bestätigung der Stadt.</p>

<h3>Stadt Bern: Altstadt</h3>
<p>Im Februar 2022 haben die Stimmberechtigten mit über 80 % eine Änderung der Bauordnung angenommen. Sie begrenzt die Kurzzeitvermietung in der Altstadt auf 90 Nächte pro Jahr. Betroffen wären in der unteren Altstadt Wohnungen ab dem zweiten Stock und in der oberen Altstadt die Dachgeschosse.</p>
<p>Die Regel war im Februar 2025 noch nicht in Kraft, weil eine Beschwerde vor dem Verwaltungsgericht hängig war. Fragen Sie den aktuellen Stand bei der Stadt nach.</p>

<h3>Interlaken und Umgebung</h3>
<p>In Interlaken, Matten, Unterseen, Wilderswil, Gsteigwiler und Saxeten brauchen Vermieter von Ferienwohnungen eine Bewilligung der Standortgemeinde. Danach folgt die Registrierung bei der Tourismus-Organisation Interlaken.</p>

<h3>Andere Orte</h3>
<p>Auch Genf begrenzt die Vermietung ganzer Wohnungen auf 90 Tage pro Jahr. Weitere Gemeinden diskutieren eigene Regeln. Ein Anruf bei der Bauverwaltung klärt die Lage in zehn Minuten.</p>

<h2>3. Stockwerkeigentum und Mietrecht</h2>
<p>Im Stockwerkeigentum gilt das Reglement der Gemeinschaft. Es kann die gewerbsmässige Kurzzeitvermietung einschränken oder verbieten. Das Bundesgericht hat 2019 ein solches Verbot geschützt. Lesen Sie das Reglement, bevor Sie inserieren, und sprechen Sie mit der Verwaltung.</p>
<p>Wer selbst Mieter ist, braucht für die Untervermietung die Zustimmung des Vermieters.</p>

<h2>4. Meldepflichten</h2>
<ul>
<li><b>Ausländische Gäste:</b> Wer gewerbsmässig beherbergt, muss ausländische Gäste der zuständigen Behörde melden. Viele Gemeinden nutzen dafür einen Meldeschein.</li>
<li><b>Kurtaxe:</b> Die meisten Ferienorte verlangen eine Anmeldung bei der Gemeinde oder der Tourismusorganisation. Mehr dazu im Artikel zur <a href="../kurtaxe-ferienwohnung/">Kurtaxe</a>.</li>
<li><b>Steuern:</b> Die Einnahmen gehören in die Steuererklärung. Mehr dazu im Artikel zu den <a href="../airbnb-einnahmen-versteuern/">Steuern</a>.</li>
</ul>

<h2>Fünf Fragen, bevor Sie starten</h2>
<ol>
<li>Ist die Wohnung altrechtlich, oder steht eine Nutzungsauflage im Grundbuch?</li>
<li>Kennt die Gemeinde eine Obergrenze, eine Bewilligung oder eine Registrierung?</li>
<li>Was sagt das Reglement der Stockwerkeigentümer?</li>
<li>Wo melde ich die Kurtaxe an?</li>
<li>Weiss meine Versicherung von der Vermietung?</li>
</ol>
<p>Bei einer kostenlosen Prüfung gehen wir diese Punkte mit Ihnen durch. <a href="../../#kontakt">Wohnung prüfen lassen</a></p>
""",
 "faq": [("Brauche ich in der Schweiz eine Bewilligung für Airbnb?", "Eine nationale Bewilligung gibt es nicht. Einzelne Gemeinden verlangen eine Bewilligung oder Registrierung, zum Beispiel die Gemeinden im Raum Interlaken und die Stadt Luzern. Fragen Sie bei Ihrer Gemeinde nach."),
         ("Wie viele Nächte darf ich in der Stadt Luzern über Airbnb vermieten?", "Seit dem 1. Januar 2025 höchstens 90 Nächte pro Kalenderjahr für Aufenthalte unter drei Monaten. Ausgenommen sind unter anderem Tourismuszonen und die Vermietung am eigenen Hauptwohnsitz."),
         ("Darf die Stockwerkeigentümer-Gemeinschaft Airbnb verbieten?", "Ja, das Reglement kann die gewerbsmässige Kurzzeitvermietung einschränken oder verbieten. Das Bundesgericht hat 2019 ein solches Verbot geschützt.")],
 "sources": [("Bundesgesetz über Zweitwohnungen (ZWG), Art. 7 und 11", None),
             ("Airbnb Hilfe-Center: Die Stadt Luzern", "https://www.airbnb.ch/help/article/3821"),
             ("Plattform J: Bericht vom 19. Februar 2025 zur Berner Altstadt", "https://www.plattformj.ch/artikel/229614/"),
             ("SRF: Maximal 90 Nächte in der Berner Altstadt", "https://www.srf.ch/news/maximal-90-naechte-weniger-airbnb-uebernachtungen-in-bern"),
             ("Interlaken Tourismus: Informationen für Beherbergende", "https://www.interlaken.swiss/info-service/informationen-fuer-beherbergende"),
             ("Bundesgericht, Urteil 5A_436/2018 vom 4. April 2019", None),
             ("Ausländer- und Integrationsgesetz (AIG), Art. 16, und Obligationenrecht, Art. 262", None)],
},
{
 "slug": "zweitwohnungsgesetz-ferienwohnung", "cat": "Kosten und Steuern", "mins": 6, "date": "2026-11-20", "stand": "November 2026",
 "h1": "Zweitwohnungsgesetz: Was Eigentümer einer Ferienwohnung wissen müssen",
 "title": "Zweitwohnungsgesetz: Was Eigentümer wissen müssen",
 "desc": "Darf ich meine Wohnung auf Airbnb vermieten? Altrechtlich, Erstwohnung oder touristisch bewirtschaftet: das Zweitwohnungsgesetz für Eigentümer erklärt.",
 "teaser": "Altrechtlich, Erstwohnung oder touristisch bewirtschaftet: was das Gesetz für die Vermietung bedeutet.",
 "lead": "Ob Sie Ihre Wohnung an Feriengäste vermieten dürfen, hängt vor allem von einem Datum ab: dem 11. März 2012. Wohnungen, die damals schon bestanden, sind frei. Für neuere Wohnungen in Gemeinden mit über 20 Prozent Zweitwohnungen gelten Auflagen, die im Grundbuch stehen. Hier steht, wie Sie das prüfen und was erlaubt ist.",
 "photo": ("wengen-dorf-sommer", "Blick auf das Dorf Wengen im Sommer mit Chalets, Hotels und Wohnhäusern am Hang",
           "Wengen gehört zur Gemeinde Lauterbrunnen. Dort sind 61 % aller Wohnungen Zweitwohnungen (Stand Oktober 2026)."),
 "key": ["In 326 von 2110 Schweizer Gemeinden liegt der Zweitwohnungsanteil über 20 Prozent, darunter Grindelwald und Lauterbrunnen (Stand Oktober 2026).",
         "Wohnungen, die am 11. März 2012 bestanden oder bewilligt waren, dürfen als Ferienwohnung vermietet werden, sofern Kanton und Gemeinde nichts Strengeres vorschreiben.",
         "Neue Wohnungen in diesen Gemeinden werden mit wenigen Ausnahmen nur als Erstwohnung oder touristisch bewirtschaftete Wohnung bewilligt. Die Auflage steht im Grundbuch.",
         "Seit 1. Oktober 2024 dürfen altrechtliche Wohnungen um bis zu 30 % erweitert und abgebrochen und neu gebaut werden, ohne die freie Nutzung zu verlieren."],
 "body": """
<p class="note">Dieser Artikel ist ein Überblick und keine Rechtsberatung. Verbindlich sind Baubewilligung, Grundbuch und die Auskunft Ihrer Gemeinde.</p>

<h2>Worum es geht</h2>
<p>Das Bundesgesetz über Zweitwohnungen gilt seit dem 1. Januar 2016. Es setzt die Zweitwohnungsinitiative um, die am 11. März 2012 angenommen wurde. Der Kern: In Gemeinden mit mehr als 20 Prozent Zweitwohnungen dürfen keine neuen Zweitwohnungen bewilligt werden.</p>
<p>Als Zweitwohnung gilt jede Wohnung, in der niemand mit Hauptwohnsitz gemeldet ist. Eine Ferienwohnung, die Sie selbst nutzen oder an Gäste vermieten, ist also eine Zweitwohnung. Wohnungen für Wochenaufenthalter, Dienstwohnungen im Gastgewerbe oder Wohnungen, die höchstens zwei Jahre leer stehen und zur Dauermiete angeboten werden, sind den Erstwohnungen gleichgestellt.</p>

<h2>Betrifft es meine Gemeinde?</h2>
<p>Jede Gemeinde führt ein Wohnungsinventar. Das Bundesamt für Raumentwicklung wertet es aus und veröffentlicht die Anteile. Im Datenstand vom 31. Oktober 2026 unterstehen 326 von 2110 Gemeinden den Bauvorschriften des Gesetzes. Ab 2027 rechnet der Bund die Anteile direkt aus dem eidgenössischen Gebäude- und Wohnungsregister.</p>
<div class="tbl"><table>
<thead><tr><th>Gemeinde</th><th class="n">Anteil</th><th>Gesetz gilt</th></tr></thead>
<tbody>
<tr><td>Grindelwald</td><td class="n">62,8 %</td><td>ja</td></tr>
<tr><td>Lauterbrunnen</td><td class="n">61,4 %</td><td>ja</td></tr>
<tr><td>Engelberg</td><td class="n">55,9 %</td><td>ja</td></tr>
<tr><td>Zermatt</td><td class="n">51,9 %</td><td>ja</td></tr>
<tr><td>Brienz (BE)</td><td class="n">37,8 %</td><td>ja</td></tr>
<tr><td>Weggis</td><td class="n">25,0 %</td><td>ja</td></tr>
<tr><td>Interlaken</td><td class="n">15,3 %</td><td>nein</td></tr>
<tr><td>Bern</td><td class="n">13,4 %</td><td>nein</td></tr>
<tr><td>Wilderswil</td><td class="n">13,1 %</td><td>nein</td></tr>
<tr><td>Luzern</td><td class="n">10,1 %</td><td>nein</td></tr>
</tbody></table></div>
<p>Wengen und Mürren gehören zur Gemeinde Lauterbrunnen. Liegt Ihre Gemeinde unter 20 Prozent, schränkt das Zweitwohnungsgesetz die Vermietung nicht ein. Andere Regeln können trotzdem gelten, etwa die 90-Nächte-Grenze in der Stadt Luzern oder die Bewilligung im Raum Interlaken. Mehr dazu im Artikel <a href="../airbnb-regeln-bewilligung-schweiz/">Regeln für Airbnb in der Schweiz</a>.</p>

<h2>Die drei Arten von Wohnungen</h2>
<h3>1. Altrechtliche Wohnung</h3>
<p>Altrechtlich ist eine Wohnung, die am 11. März 2012 rechtmässig bestand oder rechtskräftig bewilligt war. Sie ist in der Art der Nutzung frei. Sie dürfen sie selbst bewohnen, als Ferienwohnung nutzen, an Gäste vermieten oder verkaufen. Kantone und Gemeinden dürfen aber strengere Regeln erlassen, um Missbrauch zu verhindern, und die Umnutzung von Erst- zu Zweitwohnungen bewilligungspflichtig machen.</p>
<h3>2. Erstwohnung mit Auflage</h3>
<p>Neue Wohnungen in Gemeinden über 20 Prozent werden mit wenigen Ausnahmen nur als Erstwohnung oder als touristisch bewirtschaftete Wohnung bewilligt. Bei einer Erstwohnung muss dort jemand mit Hauptwohnsitz leben oder eine gleichgestellte Nutzung bestehen. Vermieten dürfen Sie die Wohnung nur so, dass die Auflage eingehalten bleibt, also an Mieter, die dort wohnen. Kurzzeitvermietung an Feriengäste ist nicht erlaubt.</p>
<h3>3. Touristisch bewirtschaftete Wohnung</h3>
<p>Diese Wohnungen muss der Eigentümer dauerhaft und ausschliesslich Gästen für kurze Aufenthalte anbieten, zu markt- und ortsüblichen Bedingungen. Das Gesetz kennt zwei Fälle:</p>
<ul>
<li><b>Einliegerwohnung:</b> Die Wohnung liegt im selben Haus, in dem der Eigentümer seinen Hauptwohnsitz hat.</li>
<li><b>Wohnung in einem strukturierten Beherbergungsbetrieb:</b> Die Wohnung ist nicht auf den Eigentümer zugeschnitten. Der Betrieb bietet hotelmässige Dienstleistungen, die die Mehrheit der Gäste nutzt, hat ein hotelähnliches Konzept und wird einheitlich bewirtschaftet.</li>
</ul>
<p>Eigene Ferien in dieser Wohnung sind damit ausgeschlossen. Wer von einer Erstwohnung zu einer touristisch bewirtschafteten Wohnung wechseln will, braucht eine Baubewilligung.</p>

<h2>So finden Sie heraus, was für Ihre Wohnung gilt</h2>
<ol>
<li><b>Baujahr und Bewilligung:</b> Stand die Wohnung am 11. März 2012 schon, oder war sie da rechtskräftig bewilligt?</li>
<li><b>Grundbuchauszug:</b> Eine Nutzungsbeschränkung ist im Grundbuch angemerkt, als Erstwohnung, Einliegerwohnung oder Wohnung in einem Beherbergungsbetrieb.</li>
<li><b>Baubewilligung:</b> Dort steht die Auflage im Wortlaut.</li>
<li><b>Gemeinde:</b> Fragen Sie die Bauverwaltung, ob kommunale Regeln gelten, auch für altrechtliche Wohnungen.</li>
<li><b>Stockwerkeigentum:</b> Das Reglement kann die Kurzzeitvermietung zusätzlich einschränken.</li>
</ol>

<h2>Umbau und Erweiterung seit Oktober 2024</h2>
<p>Seit dem 1. Oktober 2024 gilt eine Lockerung für altrechtliche Wohnungen. Sie dürfen erneuert, umgebaut, abgebrochen und neu aufgebaut werden, ohne dass eine Nutzungsbeschränkung entsteht. In der Bauzone darf die Hauptnutzfläche um höchstens 30 % der Fläche vom 11. März 2012 wachsen. In diesem Rahmen sind auch zusätzliche Wohnungen erlaubt. Geht die Erweiterung über 30 % hinaus, muss der zusätzliche Teil als Erstwohnung oder touristisch bewirtschaftete Wohnung genutzt werden.</p>
<p><b>Rechenbeispiel (Annahme):</b> Eine altrechtliche Wohnung hatte am 11. März 2012 eine Hauptnutzfläche von 80 m². 30 % davon sind 24 m². Nach dem Umbau darf sie bis 104 m² gross sein und bleibt frei vermietbar. Kanton und Gemeinde können solche Änderungen stärker einschränken und eine Baubewilligung verlangen.</p>

<h2>Wenn die Erstwohnung nicht mehr genutzt wird</h2>
<p>Die Auflage einer Erstwohnung kann vorübergehend ausgesetzt werden. Das ist möglich bei Todesfall, Wohnsitzwechsel oder Änderung des Zivilstands, oder wenn die Wohnung trotz öffentlicher Ausschreibung zu einem angemessenen Preis keinen Mieter oder Käufer findet. Die Behörde befristet die Aussetzung auf höchstens zwei Jahre. Wer sich auf die erfolglose Ausschreibung beruft, muss regelmässige Inserate zu markt- und ortsüblichen Bedingungen nachweisen und belegen, dass die Wohnung jederzeit bezugsbereit war.</p>
<p>Wer eine Wohnung entgegen der Auflage nutzt, riskiert ein Benutzungsverbot. Vorsätzliche Verstösse bestraft das Gesetz mit Freiheitsstrafe bis zu drei Jahren oder Geldstrafe.</p>

<h2>Was das für die Vermietung heisst</h2>
<p>In Grindelwald, Wengen oder Mürren lohnt sich der Blick ins Grundbuch vor dem ersten Inserat. Eine altrechtliche Wohnung kann voll vermietet werden. Wie gut Ferienwohnungen am Ort gebucht sind, zeigt die <a href="../airbnb-auslastung-schweiz/">Auslastung von 23 Schweizer Orten</a>. Was Ihre Wohnung einbringen könnte, rechnet der <a href="../../#rechner">Ertragsrechner</a>.</p>
<p>Alpinhost prüft mit Ihnen kostenlos, ob und wie Ihre Wohnung vermietet werden kann, und übernimmt danach die Vermietung auf Airbnb und Booking.com. <a href="../../#kontakt">Wohnung prüfen lassen</a></p>
""",
 "faq": [("Darf ich meine Ferienwohnung in Grindelwald auf Airbnb vermieten?", "Grindelwald hat einen Zweitwohnungsanteil von 62,8 % (Stand Oktober 2026). Altrechtliche Wohnungen, die am 11. März 2012 bestanden oder bewilligt waren, dürfen Sie vermieten, sofern die Gemeinde nichts Strengeres vorschreibt. Bei neueren Wohnungen entscheidet die Auflage in Baubewilligung und Grundbuch."),
         ("Was ist eine altrechtliche Wohnung?", "Eine Wohnung, die am 11. März 2012 rechtmässig bestand oder rechtskräftig bewilligt war. Sie ist in der Art der Nutzung frei, unter Vorbehalt strengerer Regeln von Kanton und Gemeinde."),
         ("Darf ich eine Erstwohnung kurzzeitig an Feriengäste vermieten?", "Nein. Eine Wohnung mit Erstwohnungsauflage muss von Personen mit Hauptwohnsitz oder gleichgestellt genutzt werden. Vermieten dürfen Sie sie nur an Mieter, die dort wohnen. Für den Wechsel zu einer touristisch bewirtschafteten Wohnung braucht es eine Baubewilligung."),
         ("Wo sehe ich, ob meine Wohnung eine Nutzungsbeschränkung hat?", "Im Grundbuchauszug ist die Beschränkung angemerkt. Den genauen Wortlaut finden Sie in der Baubewilligung. Bei Unklarheit hilft die Bauverwaltung der Gemeinde.")],
 "sources": [("Bundesgesetz über Zweitwohnungen (ZWG), SR 702, Stand 1. Oktober 2024", "https://lexfind.ch/tolv/248202/de"),
             ("Zweitwohnungsverordnung (ZWV), SR 702.1", "https://res.cloudinary.com/adminch/image/private/s--Dd0fjiqX--/v1719842660/Bundespublikationen/702-1d.pdf"),
             ("Bundesamt für Raumentwicklung: Wohnungsinventar und Zweitwohnungsanteil, Datenstand 31. Oktober 2026", "https://data.geo.admin.ch/api/stac/v0.9/collections/ch.are.wohnungsinventar-zweitwohnungsanteil"),
             ("Bundesrat: Medienmitteilung zum Zweitwohnungsanteil vom 31. März 2026", "https://www.admin.ch/de/newnsb/Hqdc7I9fzT_q-r_RJkn85"),
             ("LawMedia: Gelockertes Zweitwohnungsgesetz ab 1. Oktober 2024, 16. September 2024", "https://law.ch/lawnews/2024/09/gelockertes-zweitwohnungsgesetz-br-setzt-es-auf-01-10-2024-in-kraft/"),
             ("ch.ch: Zweit- oder Ferienwohnung kaufen", "https://www.ch.ch/de/wohnen/wohneigentum/immobilien-kaufen/zweit-oder-ferienwohnung-kaufen")],
},
{
 "slug": "ferienwohnung-einrichten-checkliste", "cat": "Wohnung fit machen", "mins": 5,
 "h1": "Ferienwohnung einrichten: Die Checkliste für gute Bewertungen",
 "title": "Ferienwohnung einrichten: Checkliste für Airbnb",
 "desc": "Was Gäste in einer Ferienwohnung erwarten: Betten, Küche, WLAN, Sicherheit und Anreise ohne Schlüsselübergabe. Die Checkliste zum Abhaken.",
 "teaser": "Betten, Küche, WLAN, Sicherheit und Anreise: die Checkliste zum Abhaken.",
 "lead": "Gäste verzeihen eine kleine Wohnung, aber kein schlechtes Bett und kein langsames WLAN. Mit dieser Checkliste ist Ihre Wohnung bereit für die ersten Gäste.",
 "photo": ("schlafzimmer-ferienwohnung-holz", "Schlafzimmer einer Ferienwohnung mit Holztäfer, Doppelbett und weisser Bettwäsche",
           "Schlafzimmer einer Ferienwohnung mit Holztäfer und frisch bezogenem Doppelbett."),
 "key": ["Das Bett ist der wichtigste Einzelposten: gute Matratze, zwei Sätze Wäsche pro Bett.",
         "Die Küche braucht eine vollständige Grundausstattung für die maximale Gästezahl.",
         "Eine Schlüsselbox macht die Anreise unabhängig von Ihrer Zeit.",
         "Rauchmelder, Feuerlöscher und Notfallnummern gehören in jede Wohnung."],
 "body": """
<h2>Schlafen</h2>
<ul>
<li>Gute Matratzen und Matratzenschoner</li>
<li>Zwei Sätze Bettwäsche pro Bett, damit immer ein Satz bereit ist (mehr dazu im Artikel <a href="../ferienwohnung-reinigung-waesche/">Reinigung und Wäsche</a>)</li>
<li>Zwei Kissen pro Person, eines davon flach</li>
<li>Vorhänge oder Läden, die das Zimmer abdunkeln</li>
<li>Nachttisch, Leselampe und eine freie Steckdose neben dem Bett</li>
<li>Kleiderbügel und Platz für den Koffer</li>
</ul>

<h2>Küche</h2>
<ul>
<li>Geschirr, Gläser und Besteck für die maximale Gästezahl, plus Reserve</li>
<li>Pfannen, scharfe Messer, Schneidebrett, Sieb, Dosenöffner, Korkenzieher</li>
<li>Kaffeemaschine und Wasserkocher</li>
<li>Grundvorrat: Salz, Pfeffer, Öl, Kaffee, Tee, Zucker</li>
<li>Abwaschmittel, Schwamm, Geschirrtücher, Abfallsäcke</li>
<li>Eine kurze Anleitung zur Abfalltrennung, in der Schweiz für viele Gäste neu</li>
</ul>

<h2>Bad</h2>
<ul>
<li>Pro Person ein grosses und ein kleines Frottiertuch, dazu eine Badematte</li>
<li>Seife, Duschmittel, WC-Papier in Reserve</li>
<li>Föhn</li>
<li>Haken und Ablagen, damit nichts auf dem Boden liegt</li>
</ul>

<h2>Wohnen und Arbeiten</h2>
<ul>
<li>Schnelles, stabiles WLAN. Name und Passwort gut sichtbar</li>
<li>Ein Tisch, an dem alle Gäste gleichzeitig essen können</li>
<li>Genügend Steckdosen und ein Adapter für ausländische Stecker</li>
<li><a href="../ferienwohnung-winter-vermieten/">Heizung</a>, die Gäste selbst bedienen können, mit kurzer Anleitung</li>
</ul>

<h2>In den Bergen zusätzlich</h2>
<ul>
<li>Platz für Ski, Schlitten und nasse Schuhe</li>
<li>Möglichkeit, Kleider zu trocknen</li>
<li>Wegbeschreibung mit Fotos, besonders in autofreien Orten wie Wengen und Mürren</li>
<li>Hinweise zu Bahnen, Bus und Einkaufen im Ort</li>
</ul>

<h2>Sicherheit</h2>
<ul>
<li>Rauchmelder in Schlafzimmern und im Wohnbereich</li>
<li>Feuerlöscher oder Löschdecke in der Küche</li>
<li>Kleine Hausapotheke</li>
<li>Notfallnummern und die genaue Adresse der Wohnung, gut sichtbar</li>
</ul>

<h2>Anreise ohne Schlüsselübergabe</h2>
<p>Mit einer Schlüsselbox oder einem elektronischen Schloss reisen Gäste selbständig an, auch spät am Abend. Sie müssen nicht vor Ort sein. Ändern Sie den Code regelmässig und schicken Sie ihn erst kurz vor der Anreise. Den Vergleich und eine Vorlage für die Nachricht finden Sie im Ratgeber <a href="../self-check-in-ferienwohnung/">Self-Check-in</a>.</p>

<h2>Ihre eigenen Sachen</h2>
<p>Richten Sie einen abschliessbaren Schrank oder ein Kellerabteil für persönliche Dinge ein. So bleibt die Wohnung für Gäste aufgeräumt, und Sie finden Ihre Sachen wieder, wenn Sie selbst kommen.</p>

<h2>Die Gästemappe</h2>
<p>Eine Seite pro Thema genügt: WLAN, Heizung, Abfall, Hausordnung, Notfall, Tipps für Restaurants und Ausflüge. Am besten auf Deutsch und Englisch, digital und ausgedruckt.</p>
<p>Zum Start machen wir mit unseren Kunden eine Bestandesaufnahme. Fehlt etwas, erhalten Sie eine Liste und eine Offerte zum Fixpreis. Sie entscheiden, was Sie selbst kaufen.</p>
""",
 "faq": [("Wie viel Bettwäsche brauche ich für eine Ferienwohnung?", "Mindestens zwei Sätze pro Bett. So liegt nach jeder Abreise ein frischer Satz bereit, während der andere in der Wäsche ist."),
         ("Muss eine Ferienwohnung voll möbliert sein?", "Ja. Gäste erwarten eine vollständig ausgestattete Wohnung mit Betten, Küche, Geschirr, Wäsche und WLAN. Fehlt etwas Wichtiges, zeigt sich das schnell in den Bewertungen.")],
 "sources": [("Alpinhost: Erfahrung aus der Betreuung von Ferienwohnungen", "https://alpinhost.ch/#leistungen")],
},
{
 "slug": "versicherung-ferienwohnung-vermieten", "cat": "Wohnung fit machen", "mins": 5,
 "h1": "Versicherung für die Ferienwohnung: Was bei der Vermietung gilt",
 "title": "Airbnb Versicherung Schweiz: Was bei Vermietung gilt",
 "desc": "Gebäude, Hausrat, Haftpflicht und der Schutz von Airbnb: Welche Versicherung bei der Vermietung an Feriengäste zahlt und was Sie vorher klären müssen.",
 "teaser": "Gebäude, Hausrat, Haftpflicht und AirCover: was Sie vor dem ersten Gast klären müssen.",
 "lead": "Die meisten Policen wurden für die eigene Nutzung abgeschlossen. Bevor der erste Gast kommt, sollte Ihre Versicherung von der Vermietung wissen. Diese Punkte gehören geklärt.",
 "photo": ("wasserschaden-decke", "Wasserschaden an einer Zimmerdecke, die Tapete hängt in grossen Fetzen herunter",
           "Wasserschaden durch die Decke aus der Wohnung darüber. Schäden durch Leitungswasser sind meist nur über eine Zusatzversicherung gedeckt."),
 "key": ["Melden Sie die Vermietung Ihrer Versicherung, bevor der erste Gast kommt.",
         "Wasser ist in der Gebäudeversicherung oft nicht automatisch dabei.",
         "Airbnb deckt Sachschäden bis 3 Millionen US-Dollar, aber nur bei Buchungen über Airbnb.",
         "Fotos nach jeder Reinigung sind im Schadenfall der beste Beweis."],
 "body": """
<p class="note">Dieser Artikel ist ein Überblick. Was gedeckt ist, steht in Ihrer Police. Fragen Sie Ihre Versicherung schriftlich an und bewahren Sie die Antwort auf.</p>

<h2>Gebäudeversicherung</h2>
<p>Sie deckt Schäden am Gebäude durch Feuer und Elementarereignisse wie Sturm, Hagel oder Überschwemmung. In den meisten Kantonen ist sie bei der kantonalen Gebäudeversicherung obligatorisch. In einigen Kantonen, zum Beispiel im Wallis, läuft sie über private Versicherer.</p>
<p>Wasserschäden aus Leitungen und Glasbruch sind meist nicht automatisch dabei. Sie werden über eine Zusatzversicherung gedeckt. Im Stockwerkeigentum schliesst in der Regel die Gemeinschaft die Gebäudeversicherung ab.</p>

<h2>Hausrat</h2>
<p>Die Hausratversicherung deckt Möbel, Geräte und Wäsche in der Wohnung. Klären Sie zwei Dinge:</p>
<ul>
<li>Gilt die Deckung auch, wenn die Wohnung regelmässig an Feriengäste vermietet wird?</li>
<li>Was gilt, wenn ein Gast etwas beschädigt oder mitnimmt?</li>
</ul>

<h2>Haftpflicht</h2>
<p>Stürzt ein Gast auf der Treppe oder wird durch einen Mangel in der Wohnung verletzt, kann der Eigentümer haften. Dafür gibt es die Gebäudehaftpflicht. Bei Einfamilienhäusern und selbst genutzten Wohnungen ist sie oft in der Privathaftpflicht enthalten. Bei regelmässiger Vermietung ist das nicht selbstverständlich. Fragen Sie nach.</p>

<h2>Was Airbnb abdeckt</h2>
<p>Airbnb bietet Gastgebern einen Schutz mit dem Namen AirCover. Er umfasst:</p>
<ul>
<li>Schutz bei Sachschäden bis 3 Millionen US-Dollar, wenn der Gast nicht für den Schaden aufkommt</li>
<li>Haftpflichtversicherung bis 1 Million US-Dollar, falls ein Gast verletzt wird oder sein Eigentum beschädigt wird</li>
</ul>
<p>Der Schutz gilt nur für Buchungen über Airbnb. Bei Buchungen über Booking.com oder bei direkten Buchungen greift er nicht. Er ersetzt deshalb keine eigene Versicherung.</p>

<h2>Schäden sauber belegen</h2>
<p>Im Schadenfall zählt, was Sie beweisen können. Bewährt hat sich ein einfacher Ablauf:</p>
<ol>
<li>Nach jeder Reinigung Fotos von allen Räumen machen.</li>
<li>Schäden sofort mit Datum festhalten.</li>
<li>Den Schaden über die Plattform melden, solange die Frist läuft.</li>
<li>Belege für die Reparatur oder den Ersatz aufbewahren.</li>
</ol>
<p>Wir prüfen die Wohnung nach jeder Reinigung nach Checkliste und machen Fotos. Schäden melden wir mit den Fotos bei der Plattform.</p>

<h2>Fünf Fragen an Ihre Versicherung</h2>
<ol>
<li>Ist die Vermietung an wechselnde Feriengäste in meiner Police gedeckt?</li>
<li>Sind Wasserschäden und Glasbruch versichert?</li>
<li>Wer zahlt, wenn ein Gast Mobiliar beschädigt oder stiehlt?</li>
<li>Bin ich als Eigentümer haftpflichtversichert, wenn sich ein Gast verletzt?</li>
<li>Ändert sich die Prämie durch die Vermietung?</li>
</ol>
<p>Vor dem Start gehen wir diese Fragen mit unseren Kunden durch.</p>
""",
 "faq": [("Muss ich meiner Versicherung melden, dass ich über Airbnb vermiete?", "Ja, das empfehlen wir dringend. Viele Policen wurden für die eigene Nutzung abgeschlossen. Fragen Sie schriftlich an, ob die Vermietung an wechselnde Feriengäste gedeckt ist."),
         ("Reicht der Schutz von Airbnb als Versicherung?", "Nein. AirCover deckt Sachschäden bis 3 Millionen US-Dollar und Haftpflicht bis 1 Million US-Dollar, aber nur bei Buchungen über Airbnb. Für andere Buchungen und für das Gebäude brauchen Sie eigene Versicherungen.")],
 "sources": [("Airbnb: AirCover für Gastgeber", "https://www.airbnb.ch/aircover-for-hosts")],
},
{
 "slug": "ferienwohnung-winter-vermieten", "cat": "Wohnung fit machen", "mins": 6, "date": "2026-11-17", "updated": "2026-11-19", "stand": "November 2026",
 "h1": "Ferienwohnung im Winter vermieten: Heizung, Schnee, Skiraum und Anreise",
 "title": "Ferienwohnung im Winter vermieten: Checkliste",
 "desc": "Ferienwohnung im Winter vermieten: Heizung aus der Ferne steuern, Frost vermeiden, Skiraum einrichten und die Anreise im Schnee planen. Mit Checkliste.",
 "teaser": "Heizung aus der Ferne, Frost vermeiden, Platz für Skis und eine Anreise ohne Pannen. Mit Checkliste.",
 "lead": "Im Winter sind Ferienwohnungen in den Bergen am gefragtesten, und gleichzeitig geht am meisten schief: kalte Wohnung bei der Ankunft, eingefrorene Leitung, kein Platz für nasse Skischuhe. Mit vier Vorbereitungen vermeiden Sie das meiste davon.",
 "photo": ("skiraum-skis-snowboards", "Skis und Snowboards mit Skistöcken an der Wand eines Skiraums",
           "Skis und Snowboards in einem Skiraum. Gäste im Winter brauchen einen Platz für ihre Ausrüstung ausserhalb der Wohnung."),
 "key": ["Zwischen zwei Buchungen genügen in einer Wohnung 12 bis 15 °C, in einem Chalet 6 bis 10 °C.",
         "Eine Heizungsfernsteuerung kostet mit Einbau rund CHF 500 bis 2'500 und spart bis 60 % Heizenergie.",
         "Gäste brauchen einen Platz für Skis, Schuhe und nasse Kleider, am besten ausserhalb der Wohnung.",
         "Die Anreise-Nachricht im Winter nennt Parkplatz, Bahn und den Weg im Schnee."],
 "body": """
<h2>Warum der Winter eigene Vorbereitung braucht</h2>
<p>In der Jungfrau Region beginnt die Skisaison Ende November. Den Skipass für die Jungfrau Ski Region verkaufen die Bergbahnen für die Saison 2026/27 vom 21. November 2026 bis 25. April 2027, mit 211 Pistenkilometern in drei Skigebieten. Wann die Anlagen tatsächlich fahren, hängt vom Schnee ab. Bis Ende November laufen sie oft nur am Wochenende oder teilweise.</p>
<p>Für Eigentümer heisst das: Die Wohnung muss ab Ende November bereit sein und bis Ende April zuverlässig funktionieren, auch wenn zwischen zwei Buchungen niemand vor Ort ist. In den Bergen dauert die Heizperiode acht Monate oder länger.</p>

<h2>1. Heizung: aus der Ferne steuern</h2>
<p>Eine leere Ferienwohnung muss nicht warm sein. EnergieSchweiz empfiehlt für die Zeit ohne Gäste:</p>
<div class="tbl"><table>
<thead><tr><th>Situation</th><th class="n">Raumtemperatur</th></tr></thead>
<tbody>
<tr><td>Wohnung, keine Gäste</td><td class="n">12 bis 15 °C</td></tr>
<tr><td>Chalet, keine Gäste</td><td class="n">6 bis 10 °C</td></tr>
<tr><td>Wohnräume, wenn Gäste da sind</td><td class="n">rund 20 °C</td></tr>
</tbody></table></div>
<p>Jedes Grad Raumtemperatur mehr erhöht die Heizkosten um 6 bis 10 %. Das Absenken lohnt sich: Sie sparen mehr Energie, als das spätere Aufheizen vor der Anreise braucht.</p>
<p>Damit das funktioniert, ohne dass jemand vorbeigeht, braucht es eine Heizungsfernsteuerung. Sie schaltet die Heizung per App ein und aus. Mit zusätzlichen Fühlern sehen Sie auch die Temperatur in den Räumen. Einbau und Gerät kosten rund CHF 500 bis 2'500, die Einsparung liegt bei bis zu 60 %. Die Fernsteuerung funktioniert mit den meisten Heizungen, ein Cheminée lässt sich so nicht steuern.</p>

<h3>Rechenbeispiel</h3>
<p><em>Beispiel mit angenommenen Zahlen:</em> Eine Wohnung kostet bei durchgehend 21 °C CHF 2'500 Heizung pro Winter. Mit Fernsteuerung bleibt sie zwischen den Buchungen auf 15 °C.</p>
<div class="tbl"><table>
<tbody>
<tr><td>Heizkosten pro Winter ohne Absenkung (Annahme)</td><td class="n">CHF 2'500</td></tr>
<tr><td>Einsparung, wenn die Hälfte der Zeit abgesenkt wird (Annahme rund 15 %)</td><td class="n">− CHF 375</td></tr>
<tr><td>Einsparung, wenn fast immer abgesenkt wird (rund 30 %)</td><td class="n">− CHF 750</td></tr>
<tr><td>Fernsteuerung mit Einbau (Mitte der Spanne)</td><td class="n">CHF 1'500</td></tr>
<tr><td><b>Bezahlt nach</b></td><td class="n"><b>2 bis 4 Wintern</b></td></tr>
</tbody></table></div>
<p>Je öfter die Wohnung leer steht, desto schneller ist die Steuerung bezahlt. Bei einer sehr gut gebuchten Wohnung ist der Spareffekt kleiner, der Komfort bleibt: Die Gäste kommen nie in eine kalte Wohnung.</p>

<h2>2. Frost: Leitungen schützen</h2>
<p>Eine abgesenkte Heizung ist kein Problem, eine ausgefallene schon. Friert eine Wasserleitung ein und platzt, entsteht oft ein grosser Wasserschaden, und den bemerkt in einer leeren Wohnung tagelang niemand.</p>
<ul>
<li>Heizung nie ganz abschalten, wenn Wasser in den Leitungen ist.</li>
<li>Leitungen in kalten Räumen wie Keller, Garage oder Skiraum isolieren. Wo das nicht reicht, hilft ein Frostschutz-Heizkabel mit Thermostat. Die Montage besprechen Sie mit einer Elektrikerin oder einem Elektriker.</li>
<li>Aussenwasserhähne vor dem ersten Frost absperren und entleeren.</li>
<li>Bei einer Fernsteuerung mit Fühlern einen Alarm setzen, wenn die Temperatur in der Wohnung unter einen Wert fällt.</li>
<li>Eine Person im Ort, die einen Schlüssel hat und bei einem Alarm nachsieht.</li>
</ul>
<p>Welche Versicherung einen Wasserschaden bezahlt, steht im Artikel <a href="../versicherung-ferienwohnung-vermieten/">Versicherung für die Ferienwohnung</a>.</p>

<h2>3. Skiraum, Schuhe und nasse Kleider</h2>
<p>Gäste im Winter bringen Skis, Snowboards, Stöcke und nasse Schuhe mit. Ohne Platz dafür landet das alles im Gang oder im Wohnzimmer. Klären Sie, was Ihr Haus bietet, und schreiben Sie es ins Inserat und in die Hausordnung.</p>
<ul>
<li><strong>Skiraum oder Keller:</strong> Ein abschliessbarer Platz im Haus ist ideal. Ein Ständer für Skis und Snowboards hält Ordnung.</li>
<li><strong>Schuhe:</strong> Ein Schuhtrockner, ein Schuhgestell beim Eingang und eine Matte für Schnee.</li>
<li><strong>Nasse Kleider:</strong> Haken oder ein Ständer zum Trocknen, nicht über dem Heizkörper im Schlafzimmer.</li>
<li><strong>Kein Skiraum:</strong> Fragen Sie im Sportgeschäft oder bei der Bergbahn im Ort nach einem Skidepot und nennen Sie es in der Gästemappe.</li>
<li><strong>Für die Wohnung:</strong> zusätzliche Wolldecken, Hausschuhe oder Finken und ein Fusselroller für Wollsachen.</li>
</ul>

<h2>4. Anreise im Schnee</h2>
<p>Im Winter kommen Gäste später, müder und mit mehr Gepäck an. Planen Sie die Anreise darum genauer als im Sommer:</p>
<ul>
<li><strong>Weg zum Haus:</strong> Wer räumt Zugang und Parkplatz, wenn es über Nacht schneit? Regeln Sie das mit der Hauswartung oder einer Person im Ort und legen Sie eine Schneeschaufel bereit.</li>
<li><strong>Schlüsselbox:</strong> wetterfest und geschützt montieren. Schnee und Eis blockieren Zahlenräder. Mehr dazu im Artikel <a href="../self-check-in-ferienwohnung/">Self-Check-in</a>.</li>
<li><strong>Autofreie Orte:</strong> Wengen ist autofrei, Gäste lassen das Auto in Lauterbrunnen und fahren mit der Bahn weiter. Das Parkhaus Lauterbrunnen hat 974 Plätze, ist rund um die Uhr offen und kostet CHF 18 für 8 Stunden. Die Plätze lassen sich online buchen.</li>
<li><strong>Anreise-Nachricht:</strong> Parkplatz oder Bahnverbindung, Gehzeit vom Bahnhof, ein Foto vom Eingang mit Schnee, Notfallnummer.</li>
<li><strong>Wetter:</strong> Airbnb empfiehlt, in der Hausordnung auf das saisonale Wetter hinzuweisen und Notfallnummern sowie die genaue Adresse sichtbar in der Wohnung aufzuhängen.</li>
</ul>

<h2>Checkliste vor dem ersten Wintergast</h2>
<ul>
<li>Heizung gewartet, Fernsteuerung getestet, Temperaturen für leer und belegt eingestellt</li>
<li>Frostschutz geprüft: Aussenhähne entleert, Leitungen in kalten Räumen isoliert</li>
<li>Person im Ort mit Schlüssel und Telefonnummer</li>
<li>Platz für Skis und Schuhe, Schuhtrockner, Haken für nasse Kleider</li>
<li>Schneeräumung von Zugang und Parkplatz geregelt, Schneeschaufel bereit</li>
<li>Schlüsselbox frostsicher, Ersatzschlüssel im Ort</li>
<li>Inserat ergänzt: Skiraum, Parkplatz, Weg zur nächsten Bahn</li>
<li>Kalender für die ganze Saison geöffnet und Tage gesperrt, an denen Sie selbst in der Wohnung sind</li>
</ul>
<p>Was sonst in eine Ferienwohnung gehört, steht in der <a href="../ferienwohnung-einrichten-checkliste/">Checkliste zum Einrichten</a>. Wie gut Wohnungen in Ihrem Ort gebucht sind, zeigt der <a href="../../#rechner">Ertragsrechner</a>.</p>
<p>Alpinhost kümmert sich in der Jungfrau Region um alles, was im Winter vor Ort passieren muss: Heizung vor der Anreise, Kontrolle bei Frost, Schneeräumung organisieren und Gäste, die nicht in die Wohnung kommen. <a href="../../#kontakt">Wohnung prüfen lassen</a></p>
""",
 "faq": [("Wie warm muss eine leere Ferienwohnung im Winter sein?", "EnergieSchweiz empfiehlt ohne Gäste 12 bis 15 °C in einer Wohnung und 6 bis 10 °C in einem Chalet. Vor der Anreise heizen Sie die Wohnräume wieder auf rund 20 °C. Ganz abschalten sollten Sie die Heizung nicht, solange Wasser in den Leitungen ist."),
         ("Lohnt sich eine Heizungsfernsteuerung für die Ferienwohnung?", "Meist ja. Einbau und Gerät kosten rund CHF 500 bis 2'500, die Einsparung beträgt bis zu 60 % der Heizenergie. Je öfter die Wohnung leer steht, desto schneller ist sie bezahlt. Dazu kommen Gäste nie in eine kalte Wohnung."),
         ("Wie verhindere ich eingefrorene Wasserleitungen?", "Heizung nie ganz abschalten, Leitungen in kalten Räumen isolieren, Aussenhähne vor dem Frost entleeren und bei Bedarf ein Frostschutz-Heizkabel mit Thermostat montieren lassen. Ein Temperaturalarm und eine Person im Ort mit Schlüssel helfen, einen Schaden früh zu bemerken."),
         ("Wann beginnt die Wintersaison in Grindelwald?", "Den Skipass für die Jungfrau Ski Region verkaufen die Bergbahnen für die Saison 2026/27 vom 21. November 2026 bis 25. April 2027. Wann die Anlagen fahren, hängt vom Schnee ab. Bis Ende November laufen sie oft nur am Wochenende oder teilweise.")],
 "sources": [("EnergieSchweiz: Heizungsfernsteuerung für Zweitwohnungen, abgerufen am 17. November 2026", "https://www.energieschweiz.ch/wohnen/heizungssysteme/heizungsfernsteuerung/"),
             ("EnergieSchweiz: So verheizen Sie kein Geld mehr für Ihre Zweitwohnung", "https://www.energieschweiz.ch/stories/zweitwohnung-heizen/"),
             ("EnergieSchweiz: Heizen mit Köpfchen, Stand Februar 2022, abgerufen am 19. November 2026", "https://pubdb.bfe.admin.ch/de/publication/download/447"),
             ("Die Mobiliar: Wasserleitung eingefroren, Stand September 2026", "https://www.mobiliar.ch/ratgeber/wasserleitung-eingefroren"),
             ("Jungfraubahnen: Jungfrau Ski Region, Skipass Saison 2026/27, abgerufen am 17. November 2026", "https://www.jungfrau.ch/de-ch/jungfrau-ski-region/"),
             ("Jungfraubahnen: Parkhaus Lauterbrunnen, abgerufen am 17. November 2026", "https://www.jungfrau.ch/de-ch/anreise-bahnhoefe-parking/parkieren/parkhaus-lauterbrunnen/"),
             ("Airbnb Resource Center: Plan ahead for weather emergencies, 26. Juni 2024, aktualisiert 8. August 2024", "https://airbnb.com/resources/hosting-homes/a/preparing-your-spaceand-your-guestsfor-emergencies-134")],
},
{
 "slug": "ferienwohnung-reinigung-waesche", "cat": "Wohnung fit machen", "mins": 6, "date": "2026-11-24", "stand": "November 2026",
 "h1": "Reinigung und Wäsche in der Ferienwohnung: Ablauf, Zeit und Kosten pro Wechsel",
 "title": "Reinigung der Ferienwohnung: Ablauf und Kosten",
 "desc": "Reinigung und Wäsche bei jedem Gästewechsel: Ablauf, Checkliste, Kosten mit Rechenbeispiel und was Gäste auf Airbnb seit 20. November 2026 noch tun müssen.",
 "teaser": "Ablauf und Checkliste für jeden Gästewechsel, Kosten mit Rechenbeispiel und die neuen Airbnb-Regeln zum Check-out.",
 "lead": "Nach jeder Abreise muss die Wohnung bis zum nächsten Check-in wieder wie neu sein, auch nach nur einer Nacht. Wie lange das dauert und was es kostet, hängt vom Ablauf ab. Und seit dem 20. November 2026 dürfen Gastgeber auf Airbnb weniger Arbeit an die Gäste abgeben.",
 "photo": ("bett-weisse-waesche", "Benutztes Bett mit zerwühlter weisser Bettwäsche und mehreren Kissen",
           "So sieht das Bett nach der Abreise aus. Bei jedem Wechsel kommt die ganze Wäsche weg und das Bett wird frisch bezogen."),
 "key": ["Jeder Aufenthalt braucht eine volle Reinigung, auch eine einzige Nacht.",
         "Seit dem 20. November 2026 dürfen Gastgeber auf Airbnb von Gästen nicht mehr verlangen, Geschirr zu spülen, Betten abzuziehen oder den Abfall hinauszubringen.",
         "Auf Airbnb lässt sich eine tiefere Reinigungsgebühr für Aufenthalte von 1 bis 2 Nächten festlegen.",
         "Ein zweites Set Wäsche pro Bett macht kurze Wechsel am selben Tag erst möglich."],
 "body": """
<h2>Was bei jedem Wechsel anfällt</h2>
<p>Zwischen Check-out und Check-in liegen oft nur wenige Stunden. In dieser Zeit muss die Wohnung gereinigt, die Wäsche gewechselt und das Verbrauchsmaterial aufgefüllt sein. Gäste, die eine Reinigungsgebühr bezahlen, erwarten ausdrücklich einen hohen Standard. Ein Haar im Bad oder ein Krümel im Besteckfach kostet schneller einen Stern als eine kleine Küche.</p>
<p>Bewährt hat sich, mit der Wäsche zu beginnen: alle Betten abziehen und die Tücher einsammeln. So läuft die Waschmaschine, während der Rest der Wohnung gereinigt wird. Wer am selben Tag einen neuen Gast hat, braucht ein Ersatzset Bettwäsche und Tücher, das schon sauber im Schrank liegt.</p>

<h2>Der Ablauf in 8 Schritten</h2>
<ol>
<li><strong>Lüften und Kontrolle:</strong> Fenster öffnen, kurz durch alle Räume gehen, Schäden und Fundsachen mit Foto festhalten.</li>
<li><strong>Wäsche:</strong> Betten abziehen, Tücher, Geschirrtücher und Badvorleger einsammeln, erste Maschine starten.</li>
<li><strong>Küche:</strong> Geschirr spülen und einräumen, Kühlschrank leeren, Backofen, Kochfeld, Kaffeemaschine und Abfalleimer reinigen.</li>
<li><strong>Bad:</strong> WC, Dusche, Lavabo, Spiegel und Armaturen, Haare im Abfluss entfernen.</li>
<li><strong>Oberflächen:</strong> Tische, Türgriffe, Lichtschalter, Fernbedienungen, auch unter dem Bett und in den Schubladen.</li>
<li><strong>Böden:</strong> staubsaugen, dann feucht aufnehmen, von hinten zur Tür.</li>
<li><strong>Betten und Auffüllen:</strong> Betten frisch beziehen, Tücher hinlegen, WC-Papier, Seife, Spülmittel, Kaffee und Abfallsäcke auffüllen.</li>
<li><strong>Schlusskontrolle:</strong> Licht, Heizung, Fenster, Fotos aller Räume für die eigene Ablage.</li>
</ol>
<p>Dazu kommt alle zwei bis drei Monate eine Tiefenreinigung, zum Beispiel Fenster, Schränke innen und alle Geräte.</p>

<h2>Neu seit 20. November 2026: Was Gäste beim Check-out noch tun müssen</h2>
<p>Airbnb hat die Hausregeln vereinheitlicht. Gastgeber wählen seither aus sieben Standardregeln. Arbeiten, die normalerweise eine Reinigungskraft erledigt, dürfen Sie den Gästen in der Regel nicht mehr vorschreiben. Ausnahmen gibt es nur in besonderen Fällen.</p>
<div class="tbl"><table>
<thead><tr><th>Dürfen Sie weiter verlangen</th><th>Dürfen Sie nicht mehr verlangen</th></tr></thead>
<tbody>
<tr><td>Geschirr in die Spüle stellen</td><td>Geschirr spülen</td></tr>
<tr><td>Benutzte Tücher an einem Ort sammeln</td><td>Betten abziehen</td></tr>
<tr><td>Abfall und Recycling trennen</td><td>Abfall hinausbringen</td></tr>
<tr><td>Licht löschen und die Wohnung abschliessen</td><td>Gebühren für etwas, das im Inserat schon enthalten ist, oder eigene Bussen</td></tr>
</tbody></table></div>
<p>Wichtig für Ihren Ablauf: Alle Regeln und Bitten müssen vor der Buchung im dafür vorgesehenen Teil des Inserats stehen. Neue Pflichten per Nachricht oder auf einem Zettel in der Wohnung sind nicht mehr erlaubt. Gäste können bei der Bewertung angeben, dass Regeln unerwartet oder übertrieben waren. Inserate mit wiederholt tiefen Bewertungen aus diesem Grund kann Airbnb entfernen.</p>
<p>Für die Reinigung heisst das: Planen Sie pro Wechsel die Zeit für Geschirr und Abfall fest ein, statt mit Hilfe der Gäste zu rechnen. Prüfen Sie auch Ihre Anreise-Nachricht und die Gästemappe auf alte Check-out-Listen.</p>

<h2>Was ein Wechsel kostet: Rechenbeispiel</h2>
<p>Den grössten Teil der Kosten macht die Arbeitszeit aus. Als Untergrenze für den Stundenlohn hilft der Mindestlohn, den der Bund für Hausangestellte in Privathaushalten festlegt: CHF 20.35 pro Stunde für Ungelernte (Stand 1. Januar 2026). Mit dem Zuschlag für vier Wochen Ferien und einen Feiertag sind es CHF 22.15. Reinigungsfirmen verrechnen mehr, weil Sozialversicherungen, Anfahrt und Material dazukommen.</p>
<p><em>Beispiel</em> für eine Wohnung mit 2,5 Zimmern. Die Stunden sind Annahmen, messen Sie bei Ihren ersten Wechseln die echte Zeit.</p>
<div class="tbl"><table>
<thead><tr><th>Annahme</th><th class="n">Stunden</th><th class="n">Lohn zu CHF 22.15</th></tr></thead>
<tbody>
<tr><td>Wechsel nach einem kurzen Aufenthalt</td><td class="n">3</td><td class="n">CHF 66.45</td></tr>
<tr><td>Wechsel nach einer Woche</td><td class="n">4</td><td class="n">CHF 88.60</td></tr>
<tr><td>Wechsel mit Tiefenreinigung</td><td class="n">6</td><td class="n">CHF 132.90</td></tr>
</tbody></table></div>
<p>Dazu kommen pro Wechsel das Waschen und Trocknen der Wäsche, Reinigungsmittel und Verbrauchsmaterial. Rechnen Sie diese Posten für Ihre Wohnung einmal genau aus, dann kennen Sie Ihre echten Kosten pro Wechsel.</p>

<h2>Die Reinigungsgebühr richtig festlegen</h2>
<p>Auf Airbnb legen Sie die Reinigungsgebühr pro Aufenthalt fest, im Kalender unter Preise und Gebühren. Sie können zusätzlich eine tiefere Gebühr für Aufenthalte von 1 bis 2 Nächten bestimmen. Welche gilt, entscheidet Airbnb bei der Buchung anhand der Aufenthaltsdauer. Bei Sonderangeboten wird die Gebühr nicht automatisch übernommen, Sie müssen sie selbst hinzufügen.</p>
<p>Gäste sehen die Reinigungsgebühr als eigenen Posten im Gesamtpreis. Airbnb ordnet Inserate nach Gesamtpreis und Qualität im Vergleich zu ähnlichen Inseraten in der Nähe. Eine hohe Gebühr kann also Buchungen kosten. Airbnb empfiehlt, mit der Gebühr die Reinigung zu bezahlen und nicht zusätzlich zu verdienen.</p>
<p><em>Beispiel:</em> Eine Reinigungsgebühr von CHF 90 macht bei 2 Nächten CHF 45 pro Nacht aus, bei 7 Nächten CHF 12.86 pro Nacht. Darum wirken hohe Gebühren vor allem bei kurzen Aufenthalten teuer. Drei Wege, damit umzugehen:</p>
<ul>
<li>tiefere Gebühr für 1 bis 2 Nächte</li>
<li>Mindestaufenthalt von zwei oder drei Nächten in ruhigen Zeiten</li>
<li>einen Teil der Reinigung in den Nachtpreis einrechnen</li>
</ul>

<h2>Checkliste vor dem ersten Gast</h2>
<ul>
<li>Mindestens ein Ersatzset Bettwäsche und Tücher pro Bett, sauber im Schrank</li>
<li>Reinigungsmaterial an einem Ort, mit Liste zum Nachfüllen</li>
<li>Schriftlicher Ablauf für die Reinigungskraft, mit Fotos, wie die Wohnung am Schluss aussehen soll</li>
<li>Eine Vertretung, wenn die Reinigungskraft krank ist oder Ferien hat</li>
<li>Check-out-Zeit und Check-in-Zeit mit genug Abstand für die Reinigung</li>
<li>Hausregeln auf Airbnb an die neuen Standardregeln angepasst</li>
<li>Fotos nach jeder Reinigung, damit Sie Schäden belegen können</li>
</ul>
<p>Was die Wohnung an Grundausstattung braucht, steht in der <a href="../ferienwohnung-einrichten-checkliste/">Checkliste zum Einrichten</a>. Wie Gäste ohne Schlüsselübergabe ankommen und abreisen, erklärt der Artikel <a href="../self-check-in-ferienwohnung/">Self-Check-in</a>. Und ob Sie Reinigung und Wäsche selbst organisieren oder abgeben, ist eine der Fragen im Vergleich <a href="../selbst-vermieten-oder-verwaltung/">selbst vermieten oder Verwaltung</a>.</p>
<p>Alpinhost organisiert bei jedem Wechsel Reinigung, Wäsche und Kontrolle mit Fotos. Wie viel Ihre Wohnung nach diesen Kosten einbringt, zeigt der <a href="../../#rechner">Ertragsrechner</a>. Ein Rechenbeispiel und die Kosten, die oft vergessen gehen, stehen im Artikel <a href="../ferienwohnung-vermieten-ertrag/">Was bringt eine Ferienwohnung wirklich ein?</a></p>
""",
 "faq": [("Was muss bei der Reinigung einer Ferienwohnung gemacht werden?", "Bei jedem Wechsel: Wäsche wechseln, Küche und Bad reinigen, Oberflächen und Böden, Verbrauchsmaterial auffüllen und zum Schluss alles kontrollieren. Alle zwei bis drei Monate kommt eine Tiefenreinigung dazu."),
         ("Darf ich Airbnb-Gäste bitten, die Betten abzuziehen?", "Seit dem 20. November 2026 in der Regel nicht mehr. Airbnb erlaubt nur noch angemessene Bitten wie Geschirr in die Spüle stellen, benutzte Tücher sammeln, Abfall trennen, Licht löschen und abschliessen. Alle Regeln müssen vor der Buchung im Inserat stehen."),
         ("Wie hoch sollte die Reinigungsgebühr sein?", "So hoch wie Ihre echten Kosten pro Wechsel, nicht höher. Airbnb zeigt die Gebühr im Gesamtpreis und vergleicht diesen mit ähnlichen Inseraten. Für Aufenthalte von 1 bis 2 Nächten können Sie eine tiefere Gebühr festlegen."),
         ("Wie viel Bettwäsche brauche ich pro Bett?", "Mindestens zwei Sets: eines auf dem Bett und eines sauber im Schrank. So ist ein Wechsel am selben Tag möglich, auch wenn die Wäsche vom letzten Gast noch nicht trocken ist.")],
 "sources": [("Airbnb-Hilfe: Reinigungsgebühren zu Inseraten hinzufügen, abgerufen am 24. November 2026", "https://www.airbnb.com/help/article/58"),
             ("Airbnb Resource Center: Everything you need to know about cleaning fees, 31. März 2026", "https://www.airbnb.com/resources/hosting-homes/a/everything-you-need-to-know-about-cleaning-fees-470"),
             ("Airbnb Resource Center: A clear and simple checkout, 20. Oktober 2026", "https://www.airbnb.com/resources/hosting-homes/a/a-clear-and-simple-checkout-584"),
             ("Airbnb Resource Center: Clean like a pro with these expert tips, 20. August 2024", "https://www.airbnb.com/resources/hosting-homes/a/clean-like-a-pro-with-these-expert-tips-663"),
             ("Associated Press (NY1): Airbnb guests no longer have to wash the dishes or strip the beds at checkout, 22. Oktober 2026", "https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/22/airbnb-guests-no-longer-have-to-wash-the-dishes-or-strip-the-beds-at-checkout"),
             ("Skift: Airbnb’s New Policy for Hosts: Don’t Ask Guests to Wash Dishes or Strip Beds, 21. Oktober 2026", "https://skift.com/2026/10/21/airbnbs-new-policy-for-hosts-dont-ask-guests-to-wash-dishes-or-strip-beds/"),
             ("SECO: Informationen zum NAV Hauswirtschaft, Stand 1. Januar 2026", "https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/wirtschaft-arbeit/erwerbstaetigkeit-von-auslaendern/informationen-zu-einzelnen-branchen/26_01_01%20Informationen%20zum%20NAV%20Hauswirtschaft.pdf"),
             ("Hostfully: Wie viel sollten Sie für die Reinigung Ihrer Ferienunterkunft berechnen?, 10. März 2026", "https://www.hostfully.com/de/blog/wie-viel-sollten-sie-fuer-die-reinigung-ihrer-ferienunterkunft-berechnen/")],
},
{
 "slug": "ferienwohnung-grindelwald-vermieten", "cat": "Vermieten", "mins": 6, "date": "2026-11-27", "stand": "November 2026",
 "h1": "Ferienwohnung in Grindelwald vermieten: Auslastung, Preise und Gäste in Zahlen",
 "title": "Ferienwohnung Grindelwald vermieten: die Zahlen",
 "desc": "Ferienwohnung in Grindelwald vermieten: 72 % Auslastung, CHF 296 pro Nacht, 570 Inserate. Logiernächte, Herkunft der Gäste und Rechenbeispiel.",
 "teaser": "Auslastung, Nachtpreise, Logiernächte und Herkunft der Gäste in Grindelwald, mit Rechenbeispiel für Eigentümer.",
 "lead": "Eine Ferienwohnung in Grindelwald ist im Schnitt an 72 % aller Nächte gebucht, zu durchschnittlich CHF 296 pro Nacht. Das ist deutlich mehr als im Schweizer Schnitt. Doch zwischen guten und schwachen Wohnungen liegen Welten. Hier sind die Zahlen, die für Eigentümer zählen.",
 "photo": ("grindelwald-eiger", "Chalets und Wohnhäuser im Dorf Grindelwald, links der Eiger mit Schnee, rechts ein Zug",
           "Chalets und Wohnhäuser in Grindelwald, links der Eiger. In Grindelwald sind rund 570 Unterkünfte auf Airbnb inseriert."),
 "key": ["Airbnb-Wohnungen in Grindelwald sind im Schnitt zu 72 % ausgelastet, der Schweizer Schnitt liegt bei 59 %.",
         "Der durchschnittliche Nachtpreis beträgt CHF 296, die Hälfte der Inserate verlangt weniger als CHF 206.",
         "Ferienwohnungen in Grindelwald zählten 2025 rund 372'000 einzeln gemeldete Logiernächte, 58 % mehr als 2021.",
         "Fast zwei Drittel der Gäste kommen aus dem Ausland, in Ferienwohnungen vor allem aus Korea, den USA, Deutschland und Grossbritannien."],
 "body": """
<h2>Die Marktzahlen auf einen Blick</h2>
<p>Die Zahlen gelten für alle aktiven Airbnb-Inserate in Grindelwald über zwölf Monate, von November 2025 bis Oktober 2026. Auslastung heisst: Anteil der gebuchten Nächte an allen Nächten, an denen die Wohnung buchbar war.</p>
<div class="tbl"><table>
<thead><tr><th>Kennzahl</th><th class="n">Grindelwald</th><th class="n">Schweiz</th></tr></thead>
<tbody>
<tr><td>Aktive Inserate</td><td class="n">570</td><td class="n">–</td></tr>
<tr><td>Auslastung im Durchschnitt</td><td class="n">72 %</td><td class="n">59 %</td></tr>
<tr><td>Nachtpreis im Durchschnitt</td><td class="n">CHF 296</td><td class="n">CHF 199</td></tr>
<tr><td>Umsatz pro Jahr im Durchschnitt</td><td class="n">CHF 77'548</td><td class="n">–</td></tr>
</tbody></table></div>
<p>Grindelwald gehört damit zu den am besten gebuchten Orten der Schweiz. Im <a href="../airbnb-auslastung-schweiz/">Vergleich von 23 Schweizer Orten</a> liegt nur die Stadt Luzern höher. Am stärksten gebucht sind die Monate Juni und August, am schwächsten November und März.</p>

<h2>Gute und schwache Wohnungen im Vergleich</h2>
<p>Der Durchschnitt verdeckt grosse Unterschiede. Grosse Chalets mit hohen Preisen ziehen ihn nach oben. Aussagekräftiger ist der Median, also der Wert genau in der Mitte: Die Hälfte der Wohnungen liegt darüber, die andere Hälfte darunter.</p>
<div class="tbl"><table>
<thead><tr><th>Gruppe</th><th class="n">Auslastung</th><th class="n">Nachtpreis</th><th class="n">Umsatz pro Jahr</th></tr></thead>
<tbody>
<tr><td>Beste 10 %</td><td class="n">94 %</td><td class="n">CHF 472</td><td class="n">CHF 107'668</td></tr>
<tr><td>Beste 25 %</td><td class="n">81 %</td><td class="n">CHF 312</td><td class="n">CHF 68'762</td></tr>
<tr><td>Median</td><td class="n">62 %</td><td class="n">CHF 206</td><td class="n">–</td></tr>
<tr><td>Schwächste 25 %</td><td class="n">38 %</td><td class="n">CHF 116</td><td class="n">CHF 19'563</td></tr>
</tbody></table></div>
<p>Die Werte jeder Spalte sind einzeln ermittelt. Eine Wohnung mit 94 % Auslastung hat also nicht automatisch auch einen Nachtpreis von CHF 472. Klar ist trotzdem: Zwischen dem schwächsten und dem besten Viertel liegt mehr als das Dreifache an Umsatz. Neben Lage und Grösse spielen Fotos, Preise, Bewertungen und schnelle Antworten eine Rolle.</p>

<h2>Rechenbeispiel: Was 10 Prozentpunkte Auslastung ausmachen</h2>
<p><em>Beispiel</em> mit einer Wohnung zum Median-Preis von CHF 206 pro Nacht:</p>
<div class="tbl"><table>
<thead><tr><th></th><th class="n">Median 62 %</th><th class="n">Durchschnitt 72 %</th></tr></thead>
<tbody>
<tr><td>Gebuchte Nächte pro Jahr</td><td class="n">226</td><td class="n">263</td></tr>
<tr><td>Nachtpreis</td><td class="n">CHF 206</td><td class="n">CHF 206</td></tr>
<tr><td>Umsatz pro Jahr</td><td class="n">CHF 46'556</td><td class="n">CHF 54'178</td></tr>
</tbody></table></div>
<p>37 Nächte mehr bringen beim gleichen Preis rund CHF 7'600 mehr Umsatz im Jahr. Davon gehen noch Plattformgebühr, Reinigung und allenfalls die Verwaltung ab. Wie viel am Schluss bleibt, zeigt der Artikel <a href="../ferienwohnung-vermieten-ertrag/">Was bringt eine Ferienwohnung ein</a>. Für Ihre eigene Wohnung rechnet der <a href="../../#rechner">Ertragsrechner</a> mit den Zahlen von Grindelwald.</p>

<h2>Logiernächte: Ferienwohnungen wachsen langfristig</h2>
<p>Grindelwald Tourismus zählt jede Übernachtung im Dorf. 2025 war mit 1'587'509 Logiernächten das drittbeste Jahr der Geschichte, nach den Rekordjahren 2023 und 2024. Die Ferienwohnungen haben seit 2021 stark zugelegt.</p>
<div class="tbl"><table>
<thead><tr><th>Jahr</th><th class="n">Hotels</th><th class="n">Ferienwohnungen*</th><th class="n">Total Grindelwald</th></tr></thead>
<tbody>
<tr><td>2021</td><td class="n">451'959</td><td class="n">236'008</td><td class="n">1'105'546</td></tr>
<tr><td>2022</td><td class="n">651'411</td><td class="n">331'485</td><td class="n">1'415'607</td></tr>
<tr><td>2023</td><td class="n">802'790</td><td class="n">360'994</td><td class="n">1'616'580</td></tr>
<tr><td>2024</td><td class="n">789'418</td><td class="n">378'444</td><td class="n">1'615'374</td></tr>
<tr><td>2025</td><td class="n">766'031</td><td class="n">372'469</td><td class="n">1'587'509</td></tr>
</tbody></table></div>
<p>* Nur einzeln gemeldete Übernachtungen in Ferienwohnungen. Wohnungen mit Pauschale sind nicht dabei, im Total aber schon. Das Total enthält auch Berghotels, Herbergen und Camping.</p>
<p>2025 gingen die Hotels um 3 % zurück, die Ferienwohnungen nur um 1,6 %. Schweizweit stiegen die Logiernächte in Ferienwohnungen 2025 um 4,3 % auf 7,4 Millionen. Ein Aufenthalt in einer Ferienwohnung dauert im Schweizer Schnitt 5,9 Nächte.</p>

<h2>Woher die Gäste kommen</h2>
<p>Über alle Unterkünfte stammen 35 % der Logiernächte in Grindelwald aus der Schweiz, 23 % aus Asien, 22 % aus dem übrigen Europa, 14 % aus Amerika und 6 % aus den Golfstaaten, Afrika und Ozeanien. In den Ferienwohnungen sieht die Spitze so aus:</p>
<div class="tbl"><table>
<thead><tr><th>Herkunft</th><th class="n">Logiernächte 2025</th><th class="n">Veränderung zu 2024</th></tr></thead>
<tbody>
<tr><td>Schweiz und Liechtenstein</td><td class="n">71'064</td><td class="n">−25,2 %</td></tr>
<tr><td>Korea</td><td class="n">55'086</td><td class="n">−3,7 %</td></tr>
<tr><td>USA und Kanada</td><td class="n">54'907</td><td class="n">+15,4 %</td></tr>
<tr><td>Deutschland</td><td class="n">39'221</td><td class="n">−6,2 %</td></tr>
<tr><td>Grossbritannien und Irland</td><td class="n">23'117</td><td class="n">+22,5 %</td></tr>
</tbody></table></div>
<p>Für Eigentümer heisst das: Das Inserat muss auf Englisch überzeugen, die Hausregeln und die Anreise-Nachricht ebenso. Viele Gäste reisen von weit her an, kommen spät abends mit der Bahn und kennen weder Schnee noch Schweizer Waschmaschinen.</p>

<h2>Checkliste: So holen Sie in Grindelwald mehr heraus</h2>
<ul>
<li><strong>Preise nach Saison:</strong> Im Juni und August höher, im November und März tiefer. Ein fester Preis übers ganze Jahr verschenkt Geld in der Hochsaison und Nächte in der Nebensaison.</li>
<li><strong>Inserat auf Englisch:</strong> Titel, Beschreibung und Fotos für internationale Gäste schreiben, mit Bahnhof, Bahnen und Aussicht auf den Eiger.</li>
<li><strong>Anreise ohne Wartezeit:</strong> Viele Gäste kommen spät an. Ein <a href="../self-check-in-ferienwohnung/">Self-Check-in</a> mit Schlüsselbox oder Smart Lock erspart Ihnen Abende am Telefon.</li>
<li><strong>Winter vorbereiten:</strong> Platz für Skis, ein Ort für nasse Schuhe und eine Heizung, die sich aus der Ferne steuern lässt. Mehr dazu im Artikel <a href="../ferienwohnung-winter-vermieten/">Ferienwohnung im Winter vermieten</a>.</li>
<li><strong>Kalender offen halten:</strong> Wer viele Wochen selbst blockiert, fällt in die Gruppe mit tiefer Auslastung. Eigene Ferien früh eintragen, am besten in der Nebensaison.</li>
</ul>
<p>Rechtliche Fragen wie das <a href="../zweitwohnungsgesetz-ferienwohnung/">Zweitwohnungsgesetz</a> oder die <a href="../kurtaxe-ferienwohnung/">Kurtaxe</a> behandeln wir in eigenen Artikeln.</p>

<h2>Wie Alpinhost hilft</h2>
<p>Wir wohnen in Grindelwald und vermieten Ferienwohnungen auf Airbnb und Booking.com: Inserat, Preise nach Saison, Gäste, Reinigung und Abrechnung. Wie viel Ihre Wohnung einbringen kann, sehen Sie im <a href="../../#rechner">Ertragsrechner</a>. Für eine Einschätzung mit Vergleichswohnungen aus Ihrer Nachbarschaft <a href="../../#kontakt">schreiben Sie uns</a>.</p>
""",
 "faq": [("Wie gut sind Ferienwohnungen in Grindelwald gebucht?", "Airbnb-Wohnungen in Grindelwald sind im Schnitt an 72 % der buchbaren Nächte belegt (November 2025 bis Oktober 2026). Die Hälfte der Wohnungen liegt unter 62 %, das beste Viertel über 81 %."),
         ("Wie viel kostet eine Nacht in einer Ferienwohnung in Grindelwald?", "Im Durchschnitt CHF 296. Die Hälfte der Inserate verlangt weniger als CHF 206, das beste Zehntel CHF 472 und mehr. Der Durchschnitt liegt höher, weil grosse Chalets ihn nach oben ziehen."),
         ("Wann ist in Grindelwald Hochsaison?", "Am stärksten gebucht sind Juni und August. Am schwächsten sind November und März. In diesen Monaten lohnen sich tiefere Preise oder kürzere Mindestaufenthalte."),
         ("Woher kommen die Gäste in Grindelwald?", "2025 stammten 35 % der Logiernächte aus der Schweiz, 23 % aus Asien, 22 % aus dem übrigen Europa und 14 % aus Amerika. In Ferienwohnungen sind nach den Schweizer Gästen Korea, die USA und Kanada, Deutschland und Grossbritannien am stärksten.")],
 "sources": [("GuestFavorites: Airbnb Occupancy Rates in Grindelwald, Zeitraum November 2025 bis Oktober 2026, aktualisiert am 2. November 2026", "https://www.guestfavorites.com/airbnb-occupancy-rates-in-grindelwald-switzerland"),
             ("Grindelwald Tourismus: Geschäftsbericht 2025 (Logiernächte 2021 bis 2025, Herkunft der Gäste)", "https://grindelwald.swiss/files/websites/grindelwald.swiss/Bilder/Footer/%C3%9Cber%20uns/Gesch%C3%A4ftsbericht/Jahresbericht%20GT%202025.pdf?version=037287d307446e6b"),
             ("Plattform J: 2025 war das drittbeste Geschäftsjahr, 24. Juni 2026", "https://www.plattformj.ch/artikel/244277/"),
             ("Bundesamt für Statistik: Steigerung um 4,7 % in der Parahotellerie im Jahr 2025, 29. Mai 2026", "https://www.admin.ch/de/newnsb/DV17RfFkK2dtKmgVs_tYb")],
},
]

# ---------- Datenseite: Auslastung nach Ort (Zahlen aus dem Rechner in src.html)
def _rg_market():
    import re as _re
    rows = []
    for k, name, n, occ, adr in _re.findall(r'(\w+):\{name:"([^"]+)", n:(\d+), occ:([\d.]+), adr:(\d+)\}', open("src.html", encoding="utf-8").read()):
        if int(n) > 0:
            rows.append(dict(key=k, name=name, n=int(n), occ=float(occ), adr=int(adr)))
    assert len(rows) == 23, len(rows)
    return rows

def _chf(x):
    return "CHF " + f"{int(round(x)):,}".replace(",", "'")

def _rg_market_article():
    R = _rg_market()
    by = {r["key"]: r for r in R}
    pct = lambda r: f'{round(r["occ"]*100)} %'
    occs = sorted(R, key=lambda r: (-r["occ"], -r["adr"]))
    t1 = "".join(f'<tr><td class="n">{i+1}</td><td>{r["name"]}</td><td class="n">{pct(r)}</td><td><div class="occbar"><i style="width:{round(r["occ"]*100)}%"></i></div></td><td class="n">CHF {r["adr"]}</td><td class="n">{_chf(r["n"])[4:]}</td></tr>' for i, r in enumerate(occs))
    rev = sorted(R, key=lambda r: -r["occ"]*r["adr"])
    t2 = "".join(f'<tr><td>{r["name"]}</td><td class="n">{round(r["occ"]*365)}</td><td class="n">CHF {r["adr"]}</td><td class="n">{_chf(r["occ"]*365*r["adr"])}</td></tr>' for r in rev)
    cities = [by[k] for k in ("zuerich", "genf", "lausanne", "bern", "basel", "lugano")]
    ski = [by[k] for k in ("zermatt", "verbier", "saasfee", "crans", "stmoritz", "davos", "laax", "arosa")]
    cmin, cmax = min(c["occ"] for c in cities), max(c["occ"] for c in cities)
    smin, smax = min(c["occ"] for c in ski), max(c["occ"] for c in ski)
    above = sum(1 for r in R if r["occ"] > 0.59)
    top, g, last = occs[0], by["grindelwald"], occs[-1]
    assert top["key"] == "luzern"
    dear = sorted(R, key=lambda r: -r["adr"])
    lowest = [r["name"] for r in R if r["occ"] == last["occ"]]
    body = f"""
<h2>Die Rangliste nach Auslastung</h2>
<p>Die Tabelle zeigt alle aktiven Airbnb-Inserate pro Ort über 12 Monate, von November 2025 bis Oktober 2026. Auslastung heisst: Anteil der gebuchten Nächte an allen verfügbaren Nächten.</p>
<p class="swipe">Tabelle seitlich wischen →</p>
<div class="tbl wide"><table>
<thead><tr><th class="n">Rang</th><th>Ort</th><th class="n">Auslastung</th><td></td><th class="n">Ø Nachtpreis</th><th class="n">Inserate</th></tr></thead>
<tbody>{t1}</tbody></table></div>
<p>Zum Vergleich: In der ganzen Schweiz liegt die Auslastung bei 59 % und der Durchschnittspreis bei CHF 199. {above} der 23 Orte liegen über dem Schweizer Schnitt.</p>

<h2>Drei Muster in den Zahlen</h2>
<h3>Städte sind gleichmässig gebucht</h3>
<p>Zürich, Genf, Lausanne, Bern, Basel und Lugano liegen alle zwischen {round(cmin*100)} und {round(cmax*100)} %. Die Nachtpreise sind tiefer als in den Bergen, von CHF {min(c["adr"] for c in cities)} bis CHF {max(c["adr"] for c in cities)}. Die Stadt Luzern sticht heraus: {pct(top)} Auslastung bei CHF {top["adr"]} pro Nacht.</p>
<h3>Die Jungfrau Region verbindet beides</h3>
<p><a href="../ferienwohnung-grindelwald-vermieten/">Grindelwald</a> erreicht {pct(g)} bei CHF {g["adr"]} pro Nacht. Interlaken liegt bei {pct(by["interlaken"])} und CHF {by["interlaken"]["adr"]}, Wengen, Mürren und Lauterbrunnen bei {pct(by["lauterbrunnen"])} und CHF {by["lauterbrunnen"]["adr"]}. Hohe Auslastung und hohe Preise kommen hier zusammen.</p>
<h3>Wintersportorte: weniger Nächte, höhere Preise</h3>
<p>Die grossen Wintersportorte im Wallis und in Graubünden liegen zwischen {round(smin*100)} und {round(smax*100)} %. Dafür sind die Preise oft hoch: {dear[0]["name"]} führt mit CHF {dear[0]["adr"]} pro Nacht, {dear[1]["name"]} folgt mit CHF {dear[1]["adr"]}.</p>

<h2>Was heisst das in Franken?</h2>
<p>Auslastung mal Nachtpreis ergibt den Umsatz. Die Tabelle rechnet das für ein durchschnittliches Inserat auf ein Jahr hoch, vor Plattformgebühr und Kosten.</p>
<div class="tbl"><table>
<thead><tr><th>Ort</th><th class="n">Nächte</th><th class="n">Ø Preis</th><th class="n">Umsatz pro Jahr</th></tr></thead>
<tbody>{t2}</tbody></table></div>
<p class="note">Der Durchschnitt enthält auch grosse Chalets für acht oder zehn Personen. Eine typische Wohnung mit zwei Zimmern liegt deutlich darunter. Der <a href="../../#rechner">Ertragsrechner</a> passt den Preis an die Grösse Ihrer Wohnung an.</p>

<h2>Was die Zahlen nicht zeigen</h2>
<ul>
<li><b>Die Spanne am gleichen Ort.</b> Der Wert ist der Durchschnitt aller Inserate, der guten und der schwachen. Gute Inserate sind oft doppelt so viele Nächte gebucht.</li>
<li><b>Die Saison.</b> Ein Jahreswert sagt nichts darüber, wie stark Sommer und Winter auseinanderliegen.</li>
<li><b>Die Kosten.</b> Reinigung, Wäsche, Plattformgebühr, Kurtaxe und Steuern gehen vom Umsatz ab. Mehr dazu im Artikel <a href="../ferienwohnung-vermieten-ertrag/">Was bringt eine Ferienwohnung wirklich ein?</a></li>
</ul>

<h2>So nutzen Sie die Zahlen</h2>
<p>Vergleichen Sie Ihre Wohnung mit dem Wert Ihres Ortes. Liegen Sie klar darunter, lohnt sich ein Blick auf Fotos, Preise und Mindestaufenthalt. Wir prüfen das kostenlos. <a href="../../#kontakt">Wohnung prüfen lassen</a></p>
"""
    return {
     "slug": "airbnb-auslastung-schweiz", "cat": "Vermieten", "mins": 4,
     "h1": "Airbnb-Auslastung in der Schweiz: 23 Orte im Vergleich",
     "title": "Airbnb-Auslastung Schweiz: 23 Orte im Vergleich",
     "desc": f"Wie gut sind Airbnb-Wohnungen in der Schweiz gebucht? Rangliste mit Auslastung und Nachtpreis für 23 Orte, von Luzern ({pct(top)}) bis {last['name']} ({pct(last)}).",
     "teaser": "Die Rangliste: Auslastung, Nachtpreis und Jahresumsatz für 23 Orte von Luzern bis Zermatt.",
     "lead": "Wo sind Ferienwohnungen am besten gebucht? Die Rangliste zeigt Auslastung, Nachtpreis und Jahresumsatz für 23 Schweizer Orte.",
     "photo": ("luzern-kapellbruecke", "Kapellbrücke und Wasserturm in Luzern an der Reuss",
               f"Die Stadt Luzern hat mit {pct(top)} die höchste Auslastung der 23 Orte."),
     "key": [f"Die Stadt Luzern führt mit {pct(top)} Auslastung, vor Grindelwald mit {pct(g)}.",
             "Im Schweizer Schnitt sind Airbnb-Wohnungen zu 59 % ausgelastet.",
             f"Die Städte liegen zwischen {round(cmin*100)} und {round(cmax*100)} %, die grossen Wintersportorte zwischen {round(smin*100)} und {round(smax*100)} %.",
             f"Die höchsten Nachtpreise haben {dear[0]['name']} (CHF {dear[0]['adr']}) und {dear[1]['name']} (CHF {dear[1]['adr']})."],
     "body": body,
     "faq": [("Wo ist die Airbnb-Auslastung in der Schweiz am höchsten?", f"Von den 23 verglichenen Orten liegt die Stadt Luzern mit {pct(top)} vorne. Es folgen {occs[1]['name']} mit {pct(occs[1])}, {occs[2]['name']} mit {pct(occs[2])} und {occs[3]['name']} mit {pct(occs[3])}."),
             ("Wie hoch ist die durchschnittliche Airbnb-Auslastung in der Schweiz?", "Über alle Inserate in der Schweiz liegt sie bei 59 %. Der durchschnittliche Nachtpreis beträgt CHF 199."),
             ("Wo sind die Nachtpreise am höchsten?", f"In {dear[0]['name']} mit CHF {dear[0]['adr']}, in {dear[1]['name']} mit CHF {dear[1]['adr']} und in {dear[2]['name']} mit CHF {dear[2]['adr']} pro Nacht im Durchschnitt."),
             ("Ist eine hohe Auslastung immer besser?", "Nein. Entscheidend ist der Umsatz, also Auslastung mal Nachtpreis. Ein Ort mit tieferer Auslastung und hohen Preisen kann mehr einbringen als ein gut gebuchter Ort mit tiefen Preisen.")],
     "sources": [("GuestFavorites: Airbnb-Auslastung nach Ort in der Schweiz, Zeitraum November 2025 bis Oktober 2026", "https://www.guestfavorites.com/airbnb-occupancy-rates-by-city-in-switzerland")],
    }

RG_CREDITS.setdefault("luzern-kapellbruecke", {"author": "Leonhard Lenz", "lic": "CC0", "desc": ""})
RG_CREDITS.setdefault("grindelwald-eiger", {"author": "Leonhard Lenz", "lic": "CC0", "desc": ""})
ARTICLES.insert(1, _rg_market_article())

RG_BY_SLUG = {a["slug"]: a for a in ARTICLES}
RG_CATS = ["Vermieten", "Kosten und Steuern", "Wohnung fit machen"]

def rg_credits(names):
    """Bildnachweis, klein, für das Seitenende."""
    seen, out = set(), []
    for n in names:
        if n in seen: continue
        seen.add(n)
        m = RG_CREDITS[n]
        label = RG_LABEL.get(n, n)
        txt = f'{label}: {m["author"]}, {m["lic"]}'
        out.append(f'<a href="{m["desc"]}" rel="noopener nofollow">{txt}</a>' if m.get("desc") else txt)
    return "Fotos: Wikimedia Commons. " + " · ".join(out)

RG_LABEL = {a["photo"][0]: a["photo"][1].split(",")[0] for a in ARTICLES}
RG_LABEL["wengen-dorf-sommer"] = "Wengen"

def rg_card(a, root, sizes="(max-width: 620px) 100vw, (max-width: 1060px) 50vw, 33vw"):
    url = f'{root}ratgeber/{a["slug"]}/'
    return f"""<article class="region rg-card">
  <a class="cover" href="{url}" aria-label="{a['h1']}"><div class="img">{img(a['photo'][0], a['photo'][1], sizes=sizes, root=root)}</div></a>
  <div class="txt">
    <span class="pill alt">{a['cat']}</span>
    <h3><a href="{url}" style="text-decoration:none;color:inherit">{a['h1']}</a></h3>
    <p>{a['teaser']}</p>
    <a class="more" href="{url}">Artikel lesen · {a['mins']} Min. →</a>
  </div>
</article>"""

RG_HOME = ("ferienwohnung-vermieten-ertrag", "airbnb-einnahmen-versteuern", "airbnb-oder-booking")
RG_HOME_CREDITS = rg_credits([RG_BY_SLUG[s]["photo"][0] for s in RG_HOME])

def rg_cat_id(c):
    import re as _re
    t = c.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
    return "thema-" + _re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def rg_home_teaser():
    picks = [RG_BY_SLUG[s] for s in RG_HOME]
    return f"""<section class="block" id="ratgeber" style="padding-top:0" data-de-only>
  <div class="wrap">
    <div class="head"><div><p class="eyebrow">Ratgeber</p><h2 style="margin-top:12px">Wissen für Eigentümer.</h2></div>
    <p class="lead">Erträge, Steuern, Kurtaxe und Regeln: gründlich recherchiert und ohne Fachchinesisch.</p></div>
    <div class="rg-grid">{''.join(rg_card(a, '') for a in picks)}</div>
    <p style="margin-top:22px"><a class="btn btn-ghost" href="ratgeber/">Alle Artikel im Ratgeber</a></p>
  </div>
</section>
"""

RG_REGION = {
 "grindelwald": ("kurtaxe-ferienwohnung", "airbnb-oder-booking", "ferienwohnung-vermieten-ertrag"),
 "interlaken": ("kurtaxe-ferienwohnung", "airbnb-regeln-bewilligung-schweiz", "airbnb-auslastung-schweiz"),
 "lauterbrunnen": ("ferienwohnung-vermieten-ertrag", "kurtaxe-ferienwohnung", "ferienwohnung-einrichten-checkliste"),
 "luzern": ("airbnb-auslastung-schweiz", "airbnb-regeln-bewilligung-schweiz", "airbnb-einnahmen-versteuern"),
 "bern": ("airbnb-regeln-bewilligung-schweiz", "airbnb-einnahmen-versteuern", "airbnb-auslastung-schweiz"),
 "schweiz": ("airbnb-auslastung-schweiz", "ferienwohnung-vermieten-ertrag", "selbst-vermieten-oder-verwaltung"),
}

def rg_region_block(key, root):
    """Ratgeber-Karten für eine Regionsseite. Gibt (HTML, Bildnachweis) zurück."""
    picks = [RG_BY_SLUG[s] for s in RG_REGION[key]]
    html = f"""<section class="block" style="padding-top:0" data-de-only>
  <div class="wrap">
    <h2 class="rg-cat" style="margin-top:0">Aus dem Ratgeber</h2>
    <div class="rg-grid">{''.join(rg_card(a, root) for a in picks)}</div>
    <p style="margin-top:22px"><a class="btn btn-ghost" href="{root}ratgeber/">Alle Artikel im Ratgeber</a></p>
  </div>
</section>
"""
    return html, rg_credits([a["photo"][0] for a in picks])

RG_FEED = '<link rel="alternate" type="application/rss+xml" title="Alpinhost Ratgeber" href="' + DOMAIN + '/ratgeber/feed.xml">\n'
RG_ROBOTS = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">\n'

def build_ratgeber():
    urls = ["ratgeber/"]
    # ---- Übersicht
    root = "../"
    groups = ""
    for c in RG_CATS:
        arts = [a for a in ARTICLES if a["cat"] == c]
        groups += f'<h2 class="rg-cat" id="{rg_cat_id(c)}">{c}</h2><div class="rg-grid">{"".join(rg_card(a, root) for a in arts)}</div>'
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Alpinhost","item":DOMAIN+"/"},
        {"@type":"ListItem","position":2,"name":"Ratgeber","item":DOMAIN+"/ratgeber/"}]}
    coll = {"@context":"https://schema.org","@type":"CollectionPage","name":"Ratgeber für Eigentümer von Ferienwohnungen","url":DOMAIN+"/ratgeber/","inLanguage":"de-CH",
            "publisher":{"@id":DOMAIN+"/#org"},
            "mainEntity":{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{DOMAIN}/ratgeber/{a["slug"]}/',"name":a["h1"]} for i, a in enumerate(ARTICLES)]}}
    b = f"""<main>
<div class="wrap crumbs"><a href="{root}">Alpinhost</a> › Ratgeber</div>
<section class="local-hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Ratgeber · {len(ARTICLES)} Artikel</p>
      <h1 style="margin-top:14px">Ratgeber für Eigentümer von Ferienwohnungen</h1>
      <p class="lead" style="margin-top:18px">Vom Chalet in Wengen bis zur Stadtwohnung in Luzern: Hier steht, was die Vermietung einbringt, was sie kostet und welche Regeln gelten.</p>
      <div class="cta-row"><a class="btn btn-primary" href="{root}#rechner">Ertrag berechnen</a><a class="btn btn-ghost" href="{root}#kontakt">Wohnung prüfen lassen</a></div>
    </div>
    <figure class="photo" style="margin:0">{img("wengen-dorf-sommer", "Blick auf das Dorf Wengen im Sommer mit Chalets, Wiesen und Wald", root=root, eager=True)}<figcaption>Wengen, Berner Oberland</figcaption></figure>
  </div>
</section>
<section class="block" style="padding-top:30px">
  <div class="wrap">{groups}</div>
</section>
</main>"""
    hub_cred = rg_credits(["wengen-dorf-sommer"] + [a["photo"][0] for a in ARTICLES])
    h = head("Ratgeber: Ferienwohnung vermieten in der Schweiz | Alpinhost",
        "Ratgeber für Eigentümer von Ferienwohnungen: Ertrag, Auslastung, Airbnb oder Booking.com, Steuern, Kurtaxe, Regeln, Einrichtung und Versicherung.",
        "ratgeber/", root, [ORG, crumbs, coll], ogimg="img/og-wengen-dorf-sommer.jpg", ogalt="Blick auf das Dorf Wengen im Sommer mit Chalets, Wiesen und Wald")
    write("ratgeber/index.html", page_shell(RG_ROBOTS + RG_FEED + h, b, root, credits=hub_cred))

    # ---- Artikel
    root = "../../"
    for a in ARTICLES:
        url = f'ratgeber/{a["slug"]}/'
        urls.append(url)
        full = DOMAIN + "/" + url
        crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Alpinhost","item":DOMAIN+"/"},
            {"@type":"ListItem","position":2,"name":"Ratgeber","item":DOMAIN+"/ratgeber/"},
            {"@type":"ListItem","position":3,"name":a["h1"],"item":full}]}
        art = {"@context":"https://schema.org","@type":"Article","headline":a["h1"],"description":a["desc"],"inLanguage":"de-CH",
               "image":[f'{DOMAIN}/img/og-{a["photo"][0]}.jpg', f'{DOMAIN}/img/{a["photo"][0]}-1600.webp'],"datePublished":a.get("date",RG_DATE),"dateModified":a.get("updated",a.get("date",RG_DATE)),
               "author":{"@type":"Organization","@id":DOMAIN+"/#org","name":"Alpinhost","url":DOMAIN+"/"},"publisher":{"@id":DOMAIN+"/#org"},
               "mainEntityOfPage":full,"articleSection":a["cat"],"isAccessibleForFree":True}
        faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":t}} for q, t in a["faq"]]}
        keys = "".join(f"<li>{k}</li>" for k in a["key"])
        faqs = "".join(f"<h3>{q}</h3><p>{t}</p>" for q, t in a["faq"])
        srcs = "".join(f'<li><a href="{u}" rel="noopener nofollow">{l}</a></li>' if u and "alpinhost.ch" not in u else (f'<li><a href="{u}">{l}</a></li>' if u else f"<li>{l}</li>") for l, u in a["sources"])
        related = [x for x in ARTICLES if x["slug"] != a["slug"] and x["cat"] == a["cat"]] + [x for x in ARTICLES if x["cat"] != a["cat"]]
        rel = "".join(rg_card(x, root) for x in related[:3])
        cred = rg_credits([a["photo"][0]] + [x["photo"][0] for x in related[:3]])
        b = f"""<main class="article">
<div class="wrap crumbs"><a href="{root}">Alpinhost</a> › <a href="{root}ratgeber/">Ratgeber</a> › {a['h1']}</div>
<article>
<header class="wrap art-head">
  <p class="eyebrow">{a['cat']} · {a['mins']} Min. Lesezeit</p>
  <h1>{a['h1']}</h1>
  <p class="lead" style="margin-top:18px">{a['lead']}</p>
  <p class="art-meta">Stand: {a.get("stand",RG_STAND)} · Alpinhost Redaktion</p>
  <figure class="photo art-hero">{img(a['photo'][0], a['photo'][1], sizes="(max-width: 1180px) 100vw, 1180px", root=root, eager=True)}</figure>
  <p class="art-credit">{a['photo'][2]}</p>
</header>
<section class="block" style="padding-top:34px">
  <div class="wrap twocol">
    <div class="prose">
      <div class="keybox"><b>Das Wichtigste in Kürze</b><ul>{keys}</ul></div>
      {a['body']}
      <h2>Häufige Fragen</h2>
      {faqs}
    </div>
    <div class="sidecard">
      <p class="eyebrow">Ihre Wohnung</p>
      <p style="font-family:var(--display,inherit);font-weight:700;font-size:22px;line-height:1.2">Was bringt Ihre Ferienwohnung?</p>
      <p style="color:var(--muted);font-size:15px">Der Rechner nutzt echte Marktdaten von 24 Schweizer Orten.</p>
      <a class="btn btn-primary" href="{root}#rechner">Ertrag berechnen</a>
      <a class="btn btn-ghost" href="{root}#kontakt">Wohnung kostenlos prüfen lassen</a>
      <div class="price-mini"><span>Basis</span><b>18 %</b></div>
      <div class="price-mini"><span>Komplett, inkl. Reinigung</span><b>21 %</b></div>
      <p style="font-size:14px;color:var(--muted)">WhatsApp und Telefon: <b style="white-space:nowrap">{PHONE}</b><br>E-Mail: <a href="mailto:info@alpinhost.ch" style="color:inherit;font-weight:600">info@alpinhost.ch</a></p>
    </div>
  </div>
</section>
</article>
<section class="block" style="padding-top:0">
  <div class="wrap">
    <h2 class="rg-cat" style="margin-top:0">Weiterlesen</h2>
    <div class="rg-grid">{rel}</div>
  </div>
</section>
<section class="wrap srcs" aria-label="Quellen">
  <p class="srcs-h">Quellen</p>
  <ol>{srcs}</ol>
  <p>Alle Angaben wurden im {a.get("stand",RG_STAND)} geprüft. Sie ersetzen keine Rechts- oder Steuerberatung.</p>
</section>
</main>"""
        h = head(a["title"] + " | Alpinhost", a["desc"], url, root, [ORG, crumbs, art, faq], ogimg=f'img/og-{a["photo"][0]}.jpg', ogalt=a["photo"][1]).replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
        write(url + "index.html", page_shell(RG_ROBOTS + RG_FEED + h, b, root, credits=cred))

    # ---- RSS-Feed
    from email.utils import format_datetime
    import datetime as _dt
    rfc = lambda d: format_datetime(_dt.datetime.strptime(d, "%Y-%m-%d").replace(hour=8, tzinfo=_dt.timezone.utc))
    pub = rfc(max(a.get("date", RG_DATE) for a in ARTICLES))
    esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    items = "".join(f'<item><title>{esc(a["h1"])}</title><link>{DOMAIN}/ratgeber/{a["slug"]}/</link><guid isPermaLink="true">{DOMAIN}/ratgeber/{a["slug"]}/</guid><description>{esc(a["desc"])}</description><category>{esc(a["cat"])}</category><pubDate>{rfc(a.get("date", RG_DATE))}</pubDate></item>\n' for a in ARTICLES)
    write("ratgeber/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Alpinhost Ratgeber</title><link>{DOMAIN}/ratgeber/</link><atom:link href="{DOMAIN}/ratgeber/feed.xml" rel="self" type="application/rss+xml"/><description>Ratgeber für Eigentümer von Ferienwohnungen in der Schweiz</description><language>de-CH</language><lastBuildDate>{pub}</lastBuildDate>\n{items}</channel></rss>\n')
    json.dump(urls, open("i18n/ratgeber_urls.json", "w"))
    return urls
