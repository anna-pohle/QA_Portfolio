# **Testdurchführung**

## **Tests zum neuen Feature 1:  “Einschränkung des Zugangs zu (zB alkoholischen) Produkten nach Alter des Kunden”**

| Testfall-ID | Testfall-Beschreibung | Vorbedingungen | Testschritte | Testdaten | SOLL | IST | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | knapp minderjährige:r User:in greift auf die Seite zu | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’<br>4) Klick auf Produktgruppe “Alcohol”&nbsp;&nbsp;&nbsp; | “02-09-2007”<br>(Geburtstag morgen vor 18 Jahren) | Fehlermeldung “Es wird nur ein eingeschränktes Sortiment angezeigt”<br>+<br>alkoholische Produkte nicht sichtbar&nbsp;&nbsp;&nbsp; | = SOLL | PASS |
| 2 | knapp volljährige:r User:in greift auf die Seite zu | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’<br>4) Klick auf Produktgruppe “Alcohol”&nbsp;&nbsp;&nbsp; | “01-09-2007”<br>(Geburtstag heute vor 18 Jahren) | keine Fehlermeldung, alle Produktgruppen sichtbar&nbsp;&nbsp;&nbsp; | = SOLL | PASS |
| 3 | volljährige:r Nutzer:in greift auf die Seite zu | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’<br>4) Klick auf Produktgruppe “Alcohol”&nbsp;&nbsp;&nbsp; | “30-03-2000” | keine Fehlermeldung, alle Produktgruppen sichtbar&nbsp;&nbsp;&nbsp; | = SOLL | PASS |
| 4 | Datumseingabe im falschen Format | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’&nbsp;&nbsp;&nbsp; | “30.03.2000” | Fehlermeldung “Bitte geben Sie das Datum im Format DD-MM-YYYY ein”&nbsp;&nbsp;&nbsp; | Nutzer:in wird als minderjährig eingestuft, Fehlermeldung “Es wird nur ein eingeschränktes Sortiment angezeigt”<br>+<br>alkoholische Produkte nicht sichtbar&nbsp;&nbsp;&nbsp; | FAIL |
| 5 | Nutzer:in gibt kein Geburtsdatum ein | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’&nbsp;&nbsp;&nbsp; | “” | Fehlermeldung “Bitte geben Sie Ihr Geburtsdatum im Format DD-MM-YYYY ein” oder inaktiver ‘Confirm’-Button&nbsp;&nbsp;&nbsp; | Nutzer:in wird als minderjährig eingestuft, Fehlermeldung “Es wird nur ein eingeschränktes Sortiment angezeigt”<br>+<br>alkoholische Produkte nicht sichtbar&nbsp;&nbsp;&nbsp; | FAIL |
| 6 | volljährige:r Nutzer:in will Datumseingabe nach Reload korrigieren | [Link](https://grocerymate.masterschool.com/store) | 1) Navigation zur URL<br>2) Eingabe Geburtsdatum<br>3) Klick auf ‘Confirm’<br>4) Reload der Seite&nbsp;&nbsp;&nbsp; | “30-03-2000” | Erneutes Erscheinen des Feldes zur Datumseingabe&nbsp;&nbsp;&nbsp; | Nutzer:in wird weiterhin als minderjährig eingestuft,<br>alkoholische Produkte nicht sichtbar&nbsp;&nbsp;&nbsp; | FAIL |


## Tests zum neuen Feature 2:  “Möglichkeit zur Produktbewertung mittels Sternesystem & Freitexteingabe”

| Testfall-ID | Testfall-Beschreibung | Vorbedingungen | Testschritte | Testdaten | SOLL | IST | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Nutzer:in gibt Freitext-Bewertung von genau 500 Zeichen ein | 1) Login<br>2) erfolgter Kauf des zu bewertenden Artikels | 1) Navigation zur Produktseite<br>2) Auswahl Sternbewertung (z. B. 3 Sterne)<br>3) Eingabe Freitext mit 500 Zeichen<br>4) Klick auf Absenden | Lorem ipsum… (500 Zeichen) | Nutzer:in kann Bewertung komplett eingeben & abschicken |  |  |
| 8 | Nutzer:in gibt Freitext-Bewertung von 350 Zeichen ein | 1) Login<br>2) erfolgter Kauf des zu bewertenden Artikels | 1) Navigation zur Produktseite<br>2) Auswahl Sternbewertung (z. B. 4 Sterne)<br>3) Eingabe Freitext mit 350 Zeichen<br>4) Klick auf Absenden | Lorem ipsum… (350 Zeichen) | Nutzer:in kann Bewertung komplett eingeben & abschicken |  |  |
| 9 | Nutzer:in gibt Freitext-Bewertung von 501 Zeichen ein | 1) Login<br>2) erfolgter Kauf des zu bewertenden Artikels | 1) Navigation zur Produktseite<br>2) Auswahl Sternbewertung (z. B. 5 Sterne)<br>3) Eingabe Freitext mit 501 Zeichen<br>4) Klick auf Absenden | Lorem ipsum… (501 Zeichen) | Nutzer:in erhält Fehlermeldung & muss Eingabe zum Abschicken kürzen |  |  |
| 10 | Nutzer:in will 0 Sterne vergeben (nur Freitext) | 1) Login<br>2) erfolgter Kauf des zu bewertenden Artikels | 1) Navigation zur Produktseite<br>2) Keine Auswahl bei Sterneskala<br>3) Eingabe Freitext mit 350 Zeichen<br>4) Klick auf Absenden | Keine Sterne; Freitext 350 Zeichen | Fehlermeldung, dass mindestens ein Stern vergeben werden muss |  |  |
| 11 | Nutzer:in will nach erneutem Kauf eine weitere Bewertung abgeben | 1) Login<br>2) erfolgter Kauf & Bewertung des zu bewertenden Artikels<br>3) erneuter Kauf des zu bewertenden Artikels | 1) Kauf von 10 Äpfeln<br>2) Abgabe Bewertung: 2 Sterne<br>3) Erneuter Kauf von 10 Äpfeln<br>4) Abgabe Bewertung: 5 Sterne | a) 2 Sterne<br>b) 5 Sterne | Nutzer:in kann eine weitere Bewertung für das gleiche Produkt abgeben |  |  |
| 12 | Nutzer:in gibt nur einen Emoji als Freitext ein | 1) Login<br>2) erfolgter Kauf des zu bewertenden Artikels | 1) Navigation zur Produktseite<br>2) Auswahl Sternbewertung (z. B. 4 Sterne)<br>3) Eingabe Freitext<br>4) Klick auf Absenden | 🤩 | Emoji wird als Bewertung angezeigt |  |  |


## Tests zur neuen Funktion “Versandkostenanpassung je nach Bestellsumme”

| Testfall-ID | Testfall-Beschreibung | Vorbedingungen | Testschritte | Testdaten | SOLL | IST | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | Bestellwert ist exakt 20,00€ | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 20,00€ in den Warenkorb legen<br>2) Checkout starten | 20,00€ Warenwert | Versandkosten 5€ |  |  |
| 14 | Bestellwert liegt bei 15€ | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 15,00€ in den Warenkorb legen<br>2) Checkout starten | 15,00€ Warenwert | Versandkosten 5€ |  |  |
| 15 | Bestellwert knapp über Schwellwert | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 20,01€ in den Warenkorb legen<br>2) Checkout starten | 20,01€ Warenwert | Versand kostenlos |  |  |
| 16 | Bestellwert liegt bei 100€ | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 100,00€ in den Warenkorb legen<br>2) Checkout starten | 100,00€ Warenwert | Versand kostenlos |  |  |
| 17 | Bestellwert ist unwahrscheinlich groß | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 100.000€ in den Warenkorb legen<br>2) Checkout starten | 100.000€ Warenwert | Fehlermeldung / Aufforderung B2B-account |  |  |
| 18 | Bestellmenge eines Artikels ist unwahrscheinlich groß | 1) Login<br>2) Warenkorb kann befüllt werden | 1) 100.000 Äpfel in den Warenkorb legen<br>2) Checkout starten | 100.000 Äpfel | Fehlermeldung / Aufforderung B2B-account |  |  |
| 19 | Schwellwert für kostenlosen Versand wird über- und unterschritten | 1) Login<br>2) Warenkorb kann befüllt werden | 1) Waren im Wert von 25,00€ in den Warenkorb legen<br>2) Waren entfernen bis unter 20€<br>3) Checkout prüfen | 25,00€ → <20,00€ | Versandkosten passen nach Anpassung |  |  |
| 20 | Nutzer:in gibt ungültige Kartendaten ein | 1) Login<br>2) Warenkorb kann befüllt werden<br>3) Checkout kann gestartet werden | 1) Eingabe Kartendaten: Nummer 1234567891234563; Name Erika Test; Ablauf 09/2026; CVV 456<br>2) Zahlung absenden | Ungültige Kartendaten | Zahlung wird abgelehnt |  |  |

