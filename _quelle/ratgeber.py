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
<p>«Typische Wohnung» ist der Median: Die Hälfte der Inserate am Ort verlangt mehr, die andere Hälfte weniger. In der ganzen Schweiz liegt die Auslastung bei 59 % und der Durchschnittspreis bei CHF 199, gerechnet über 36'276 Inserate.</p>

<h2>Warum der Durchschnitt täuscht</h2>
<p>In Grindelwald kostet eine Nacht im Durchschnitt CHF 296. Die typische Wohnung verlangt aber nur CHF 206. Der Grund sind grosse Chalets für acht oder zehn Personen, die den Durchschnitt nach oben ziehen. In Verbier ist der Abstand noch grösser: CHF 401 im Durchschnitt, CHF 150 im Median.</p>
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
<tr><td>Plattformgebühr 15,5 %</td><td class="n">− CHF 8'357</td></tr>
<tr><td><b>Bleibt nach Plattformgebühr</b></td><td class="n"><b>CHF 45'558</b></td></tr>
</tbody></table></div>
<p>Wer selbst vermietet, behält diesen Betrag und macht die Arbeit selbst. Mit unserem Komplett-Paket (21 %) bleiben CHF 35'991 pro Jahr, also rund CHF 3'000 pro Monat. Die Reinigung deckt die Reinigungsgebühr, die der Gast zusätzlich bezahlt.</p>

<h2>Was Sie vom Ertrag noch abziehen müssen</h2>
<ul>
<li>Nebenkosten: Heizung, Strom, Wasser, Internet</li>
<li>Versicherungen und Unterhalt der Wohnung</li>
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
<thead><tr><th></th><th>Airbnb</th><th>Booking.com</th></tr></thead>
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
<thead><tr><th></th><th class="n">Airbnb</th><th class="n">Booking.com</th></tr></thead>
<tbody>
<tr><td>Übernachtungsumsatz</td><td class="n">CHF 615.00</td><td class="n">CHF 615.00</td></tr>
<tr><td>Gebühr</td><td class="n">− 95.33 (15,5 %)</td><td class="n">− 92.25 (15 %)</td></tr>
<tr><td>Zahlungsgebühr</td><td class="n">inbegriffen</td><td class="n">− 6.77 bis − 19.07</td></tr>
<tr><td><b>Bleibt bei Ihnen</b></td><td class="n"><b>CHF 519.67</b></td><td class="n"><b>CHF 504 bis 516</b></td></tr>
</tbody></table></div>
<p>Unter dem Strich ist der Unterschied klein. Wichtiger ist, auf welcher Plattform Ihre Wohnung mehr Nächte füllt.</p>

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
<li>Anreise erklären: Weg, Parkplatz, Schlüssel, Hausordnung</li>
<li>Erreichbar sein, wenn der Gast den Schlüssel nicht findet oder die Heizung streikt</li>
<li>Nach der Abreise reinigen, Betten frisch beziehen, Wäsche waschen</li>
<li>Wohnung kontrollieren und Schäden festhalten</li>
<li>Verbrauchsmaterial nachfüllen</li>
<li>Gast bewerten, Kurtaxe abrechnen, Einnahmen für die Steuern festhalten</li>
</ul>
<p>Dazu kommt die Arbeit im Hintergrund: Preise an Saison und Nachfrage anpassen, Kalender pflegen, Inserat und Fotos aktuell halten.</p>

<h2>Der Aufwand, ehrlich gerechnet</h2>
<p>Nehmen wir eine Wohnung in Grindelwald mit der durchschnittlichen Auslastung von 72 %. Das sind 263 gebuchte Nächte pro Jahr. Bleiben die Gäste im Schnitt drei Nächte, ergibt das rund 88 Gästewechsel. Die drei Nächte sind eine Annahme, in den Bergen sind kurze Aufenthalte häufig.</p>
<p>88 Wechsel heissen 88 Reinigungen und 88 Anreisen, verteilt über das ganze Jahr, auch an Weihnachten und in Ihren eigenen Ferien.</p>

<h2>Was eine Verwaltung kostet</h2>
<p>Marktüblich sind in der Schweiz 15 bis 25 Prozent. Die Zahl allein sagt wenig. Fragen Sie immer nach der Berechnungsgrundlage: Wird der Prozentsatz vor oder nach Abzug der Plattformgebühr gerechnet? Zählt die Reinigungsgebühr dazu?</p>
<p>Ein Beispiel mit unseren Konditionen: Nach der Plattformgebühr bleiben in Grindelwald rund CHF 45'558 pro Jahr. Davon gehen im Komplett-Paket 21 % an uns, also CHF 9'567. Bei Ihnen bleiben CHF 35'991. Reinigung, Wäsche, Anreise und Kontrolle sind darin organisiert.</p>

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
<li>Wer bezahlt die Reinigung, und zu welchem Preis?</li>
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
<p>In Gemeinden mit mehr als 20 % Zweitwohnungen dürfen keine neuen Zweitwohnungen mehr bewilligt werden. Das betrifft die meisten Ferienorte in den Bergen. Für Eigentümer ist wichtig, wann die Wohnung entstanden ist:</p>
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
<li>Zwei Sätze Bettwäsche pro Bett, damit immer ein Satz bereit ist</li>
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
<li>Heizung, die Gäste selbst bedienen können, mit kurzer Anleitung</li>
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
<p>Mit einer Schlüsselbox oder einem elektronischen Schloss reisen Gäste selbständig an, auch spät am Abend. Sie müssen nicht vor Ort sein. Ändern Sie den Code regelmässig und schicken Sie ihn erst kurz vor der Anreise.</p>

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
<thead><tr><th class="n">Rang</th><th>Ort</th><th class="n">Auslastung</th><th></th><th class="n">Ø Nachtpreis</th><th class="n">Inserate</th></tr></thead>
<tbody>{t1}</tbody></table></div>
<p>Zum Vergleich: In der ganzen Schweiz liegt die Auslastung bei 59 % und der Durchschnittspreis bei CHF 199. {above} der 23 Orte liegen über dem Schweizer Schnitt.</p>

<h2>Drei Muster in den Zahlen</h2>
<h3>Städte sind gleichmässig gebucht</h3>
<p>Zürich, Genf, Lausanne, Bern, Basel und Lugano liegen alle zwischen {round(cmin*100)} und {round(cmax*100)} %. Die Nachtpreise sind tiefer als in den Bergen, von CHF {min(c["adr"] for c in cities)} bis CHF {max(c["adr"] for c in cities)}. Die Stadt Luzern sticht heraus: {pct(top)} Auslastung bei CHF {top["adr"]} pro Nacht.</p>
<h3>Die Jungfrau Region verbindet beides</h3>
<p>Grindelwald erreicht {pct(g)} bei CHF {g["adr"]} pro Nacht. Interlaken liegt bei {pct(by["interlaken"])} und CHF {by["interlaken"]["adr"]}, Wengen, Mürren und Lauterbrunnen bei {pct(by["lauterbrunnen"])} und CHF {by["lauterbrunnen"]["adr"]}. Hohe Auslastung und hohe Preise kommen hier zusammen.</p>
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
        "ratgeber/", root, [ORG, crumbs, coll], ogimg="img/og-wengen-dorf-sommer.jpg")
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
               "author":{"@type":"Organization","name":"Alpinhost","url":DOMAIN+"/"},"publisher":{"@id":DOMAIN+"/#org"},
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
    <aside class="sidecard">
      <p class="eyebrow">Ihre Wohnung</p>
      <p style="font-family:var(--display,inherit);font-weight:700;font-size:22px;line-height:1.2">Was bringt Ihre Ferienwohnung?</p>
      <p style="color:var(--muted);font-size:15px">Der Rechner nutzt echte Marktdaten von 24 Schweizer Orten.</p>
      <a class="btn btn-primary" href="{root}#rechner">Ertrag berechnen</a>
      <a class="btn btn-ghost" href="{root}#kontakt">Wohnung kostenlos prüfen lassen</a>
      <div class="price-mini"><span>Basis</span><b>18 %</b></div>
      <div class="price-mini"><span>Komplett, inkl. Reinigung</span><b>21 %</b></div>
      <p style="font-size:14px;color:var(--muted)">WhatsApp und Telefon: <b style="white-space:nowrap">{PHONE}</b><br>E-Mail: <a href="mailto:info@alpinhost.ch" style="color:inherit;font-weight:600">info@alpinhost.ch</a></p>
    </aside>
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
        h = head(a["title"] + " | Alpinhost", a["desc"], url, root, [ORG, crumbs, art, faq], ogimg=f'img/og-{a["photo"][0]}.jpg').replace('<meta property="og:type" content="website">', '<meta property="og:type" content="article">')
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
