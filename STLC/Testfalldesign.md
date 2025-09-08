URL: https://grocerymate.masterschool.com/

## Feature 1: Einschränkung des Zugangs zu (zB alkoholischen) Produkten nach Alter des Kunden

**Verwendete Testentwurfsverfahren:** Grenzwertanalyse, Äquivalenzklassenbildung, Fehlererwartungsmethode, Anwendungsfalltests 

**Testfälle**: 

1. **Grenzwertanalyse**:
    - **Testfall**: Verifiziere die Seitennutzung mit einem Nutzer, der auf den Tag genau 18 Jahre alt ist
    - **Eingabe**: [heutiges Datum] - 18 Jahre
    - **Erwartetes Ergebnis**: Der Nutzer kann das ganze Sortiment sehen.
2. **Grenzwertanalyse**:
    - **Testfall**: Verifiziere die Seitennutzung mit einem Nutzer, der erst am kommenden Tag 18 Jahre alt wird
    - **Eingabe**: [heutiges Datum] - 18 Jahre + 1 Tag
    - **Erwartetes Ergebnis:** Der Nutzer kann nur ein eingeschränktes Sortiment sehen (keine alkoholischen Getränke)
3. **Äquivalenzklassenbildung**:
    - **Testfall**: Verifiziere die Seitennutzung mit einem Nutzer, der volljährig ist
    - **Eingabe**: “30-03-2000”
    - **Erwartetes Ergebnis:** Der Nutzer kann das ganze Sortiment sehen.
4. **Fehlererwartungsmethode**:
    - **Testfall**: Nutzer gibt das Datum im falschen Format ein
    - **Eingabe**: “30.03.2000”
    - **Erwartetes** Ergebnis: Fehlermeldung “Bitte geben Sie das Datum im Format DD-MM-YYYY ein”
5. **Fehlererwartungsmethode**:
    - **Testfall**: Nutzer gibt kein Datum ein
    - **Eingabe**: “”
    - **Erwartetes** **Ergebnis**: Fehlermeldung “Bitte geben Sie Ihr Geburtsdatum im Format DD-MM-YYYY ein” oder inaktiver ‘Bestätigen’-Button
6. **Anwendungsfalltest**:
    - **Testfall**: ein:e volljährige Nutzer:in hat sich vertippt & will sich durch erneute Eingabe doch noch Zugang zum alkoholischen Sortiment verschaffen; Nutzer:in lädt die Seite neu
    - **Eingabe**: “30-03-2000”, dann reload der Seite
    - **Erwartetes** **Ergebnis**: Nutzer:in kann erneut Geburtsdatum eingeben

## Feature 2: Möglichkeit zur Produktbewertung mittels Sternesystem & Freitexteingabe

**Verwendete Testentwurfsverfahren:**  Grenzwertanalyse, Äquivalenzklassenbildung, Fehlererwartungsmethode, Anwendungsfalltests

**Testfälle:**

1. **Grenzwertanalyse**:
    - **Testfall**: Nutzer:in gibt Freitext-Bewertung von genau 500 Zeichen ein
    - **Eingabe**: “Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et e”
    - **Erwartetes** **Ergebnis**: Nutzer:in kann Bewertung komplett eingeben & abschicken
2. **Äquivalenzklassenbildung**:
    - **Testfall**: Nutzer:in gibt Freitext-Bewertung von 350 Zeichen ein
    - **Eingabe**: “Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elit”
    - **Erwartetes** **Ergebnis**: Nutzer:in kann Bewertung komplett eingeben & abschicken
3. **Grenzwertanalyse**:
    - **Testfall**: Nutzer:in gibt Freitext-Bewertung von 501 Zeichen ein
    - **Eingabe**: “Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea”
    - **Erwartetes** **Ergebnis**: Nutzer:in erhält Fehlermeldung & muss Eingabe zum Abschicken kürzen
4. **Anwendungsfalltest**:
    - **Testfall**: Nutzer:in will 0 Sterne vergeben
    - **Eingabe**: keine Auswahl bei der Sterneskala, nur Freitextbewertung mit 350 Zeichen: “Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elit”
    - **Erwartetes Ergebnis**: Fehlermeldung, dass mindestens ein Stern vergeben werden muss (vgl. Requirements)
5. **Anwendungsfalltest**:
    - **Testfall**: Nutzer:in will nach erneutem Kauf eines Produktes eine weitere Bewertung abgeben  (z.B. wenn diesmal die Qualität besser/schlechter als beim ersten Kauf war)
    - **Eingabe**: 
    a) Kauf von 10 Äpfeln; Bewertung von 2 Sternen
    b) Kauf von 10 Äpfeln; Bewertung(sversuch) von 5 Sternen
    - **Erwartetes** **Ergebnis**: Der Nutzer kann eine weitere Bewertung für das gleiche Produkt abgeben
6. **Fehlererwartungsmethode**:
    - **Testfall**: Nutzer:in will nur einen Emoji als Freitextbewertung eingeben
    - **Eingabe**: 🤩
    - **Erwartetes Ergebnis**: Emoji wird als Bewertung angezeigt

## Feature 3: Versandkostenanpassung je nach Bestellsumme

**Verwendete Testentwurfsverfahren:** Grenzwertanalyse, Äquivalenzklassenbildung, Fehlererwartungsmethode, Anwendungsfalltests

Testfälle:

1. **Grenzwertanalyse**:
    - **Testfall**: Bestellwert ist exakt 20,00€
    - **Eingabe**: Waren im Wert von 20,00€
    - **Erwartetes Ergebnis**: Die Versandkosten belaufen sich auf 5€
2. **Äquivalenzklassenbildung**:
    - **Testfall**: Der Bestellwert liegt bei 15€
    - **Eingabe**: Waren im Wert von 15,00€
    - **Erwartetes** **Ergebnis**: Die Versandkosten belaufen sich auf 5€
3. **Grenzwertanalyse**:
    - **Testfall**: Bestellwert ist knapp höher als der Schwellwert
    - **Eingabe**: Waren im Wert von 20,01€
    - **Erwartetes** **Ergebnis**: Der Versand ist kostenlos
4. **Äquivalenzklassenbildung**:
    - **Testfall**: Der Bestellwert liegt bei 100€
    - **Eingabe**: Waren im Wert von 100,00€
    - **Erwartetes** **Ergebnis**: Der Versand ist kostenlos
5. **Fehlererwartungsmethode**:
    - **Testfall**: Der Bestellwert ist unwahrscheinlich groß.
    - **Eingabe**: 100.000€ Warenwert im Einkaufskorb beim checkout
        - **Erwartetes** **Ergebnis**: Fehlermeldung “Sie können maximal Waren im Wert von 2000€ erwerben. Bitte reduzieren Sie den Bestellwert.”
6. **Fehlererwartungsmethode**:
    - **Testfall**: Die Bestellmenge eines bestimmten Artikels ist unwahrscheinlich groß.
    - **Eingabe**: 100.000 Äpfel im Einkaufskorb beim checkout
        - **Erwartetes** **Ergebnis**: “Sie können jeden Artikel maximal 100 mal im Warenkorb haben. Bitte reduzieren Sie die Bestellmenge.”
7. **Anwendungsfalltest**:
    - **Testfall**: Der Schwellwert f.d. kostenlosen Versand wird erst über- und dann unterschritten.
    - **Eingabe**: Bestellwert 25,00€, dann werden Waren aus dem Einkaufswagen entfernt, bis der Bestellwert unter 20€ fällt.
    - **Erwartetes** **Ergebnis**: Der Versand sollte nach dem Entfernen der Waren wieder 5€ betragen.
8. Fehlererwartungsmethode:
    - **Testfall**: Nutzer:in gibt negative Anzahl Produkte ein, um Geld zu erhalten, statt zu bezahlen.
    - **Eingabe**: “-50 Äpfel”
    - **Erwartetes** **Ergebnis**: Eingabe negativer Werte nicht möglich
