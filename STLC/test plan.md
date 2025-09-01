## **1. Produktanalyse**

**1.1. Zielsetzung**

- Online-Einkauf von Lebensmitteln leicht zugänglich machen

**1.2. Benutzerbasis - Wer wird die Software benutzen?**

- allgemeine Öffentlichkeit
- demographische Hauptgruppe wahrscheinlich zwischen 13 Jahre (alt genug, um Lebensmittel einkaufen zu dürfen) und 70 Jahre alt (jung genug, um mit der allgemeinen Nutzung des Internets und genereller Website-Interaktion vertraut zu sein)

**1.3. Hardware- und Software-Spezifikationen**

- **Hardware-Anforderungen:**
    - Geräte: PCs, Laptops, Smartphones, Tablets
    - Spezifikationen: Standardkonfigurationen für Android- und iOS-Geräte, Desktops mit mindestens 4GB RAM, 2GHz Prozessor
- **Software-Anforderungen:**
    - Betriebssysteme: Windows, macOS, Android, iOS
    - Browsers: Chrome, Firefox, Safari, Edge, Brave
    - Abhängigkeiten:
        - Backend-Dienste (Server, Datenbanken, APIs)
        - Werbedienste von Drittanbietern (GoogleAds etc)
        - Zahlungsgateways (auf Marketmate vorhanden: AMEX, Apple Pay, Google Pay, MasterCard, FacebookPay(?), VISA; 
        ansonsten ggf noch relevant: PayPal, Klarna, Sofortüberweisung, Überweisung, Bitcoin)

**1.4. Produktfunktionalität - Bestehende und neu hinzukommende Funktionen**

**existent:**

- Anzeige aller Produkte, ihres Namens und Preises
- Produkte nach Kategorie sortiert anzeigen
- Anzeige der Produkte nach Preis geordnet
- Suche nach Produkten nach Namen
- Online-Einkauf von Lebensmitteln in unterschiedlichen Mengen
- Online-Zahlung(en)
- Ermöglichung der Erstellung von personalisierten Benutzerprofilen
- Ermöglichung der Markierung von Produkten als Favoriten und Speicherung dieser Produkte im Benutzerprofil
- Ermöglichung des Empfangs von (personalisierten?) Newslettern
- Kontaktaufnahme mit dem Kundensupport (per Telefon und E-Mail)
- dem Unternehmen in den sozialen Medien zu folgen (fb, insta, twitter, tiktok)
- Lieferung der gekauften Waren

**neu:**

- Einschränkung des Zugangs zu (zB alkoholischen) Produkten nach Alter des Kunden
- Möglichkeit zur Produktbewertung mittels Sternesystem & Freitexteingabe
- Versandkostenanpassung je nach Bestellsumme

## **2. Teststrategie entwerfen**

**2.1. Umfang der Tests**

- **Umfang: Welche Funktionalitäten sind im Testumfang enthalten?**
    - Anzeige aller Produkte, ihres Namens, Preises und ihrer Bewertung
    - Anzeige der Produkte geordnet nach Kategorie
    - Anzeige der Produkte nach Preis geordnet
    - Suche nach Produkten nach Namen
    - Einschränkung des Zugriffs auf Produkte aufgrund des Alters des Kunden
    - Produkte bewerten (mit Sternesystem bzw Sternesystem & Freitext)
    - kostenloser Versand bei Bestellwert > 20€
    - Online-Einkauf von Lebensmitteln in unterschiedlichen Mengen durch Hinzufügen zu einem digitalen Einkaufswagen
    - Ermöglichung der Erstellung von personalisierten Benutzerprofilen
    - das Markieren von Produkten als Favoriten und das Speichern dieser Produkte im eigenen Benutzerprofil ermöglichen
    - den Empfang von (personalisierten?) Newslettern ein- und ausschalten
    - dem Unternehmen in den sozialen Medien folgen (fb, insta, twitter, tiktok)
    
- **Außerhalb des Geltungsbereichs: Was fällt nicht in den Bereich der Prüfung?**
    - die tatsächliche Lieferung der gekauften Waren
    - Kontaktaufnahme mit dem Kundensupport (per Telefon und E-Mail)
    - Online-Zahlung(en)
    - Leistungstests
    - Lasttests
    - Sicherheitstests

**2.2. Geplante Testarten**💡

*Welche Testarten werden für die neuen Funktionen benötigt?*

**tatsächlich**:

- Funktionstests
- Usability-Tests/  Akzeptanztests

**theoretisch aber auch:**

- Regressionstests
- Lasttests
- Sicherheitstests
- explorative Tests

**2.3. Risiken und Gegenmaßnahmen**

- **Entwicklungsverzögerungen**
    
    → Gegenmaßnahme: Zeitpuffer im Zeitplan einplanen
    
- **Fehlende Testdaten**
    
    → Gegenmaßnahme: Erstellen von Testdaten (Mock-Daten)
    
- **Ressourcenengpässe**
    
    → Gegenmaßnahme: Ersatzpersonen identifizieren und einplanen, Ggf. Crowdtesting implementieren
    
- **Testverzerrung durch Software-Abhängigkeiten**
    
    → Gegenmaßnahme: alle Testgeräte vor dem Testen aktualisieren
    
- **Fehler in den out-of-scope Bereichen**
    
    → Roll-out-Phase mit kleinerer Nutzergruppe vor dem großen Livegang(?)
    

**2.4. Testlogistik (Testverantwortlichkeiten)**

- **Testmanager** – Jane Smith
- **QA Engineer (Funktion & Regression)** – John Doe
- **QA Engineer (Performance & Sicherheit)** – Alice Johnson
- **QA Engineer (Usability)** – Robert Brown
- **Endanwender für UAT (User Acceptance Test)** – Maria Garcia

---

## **3. Testziele definieren**

**3.1. Ziele**

- **Funktionalität:** Sicherstellen, dass neue und bestehende Funktionen wie vorgesehen arbeiten
- **Benutzeroberfläche (GUI):** Überprüfung auf Bedienbarkeit, Konsistenz und Fehlerfreiheit
- **Leistung (Performance):** Bestätigung, dass das System die erwartete Last bewältigt
- **Sicherheit:** Identifikation und Absicherung potenzieller Schwachstellen
- **Benutzbarkeit (Usability):** Bewertung der Nutzerfreundlichkeit und Zugänglichkeit

**3.2. Erwartete Ergebnisse**

- Alle Funktionen verhalten sich gemäß Spezifikation
- Die Oberfläche ist intuitiv, responsiv und fehlerfrei
- Performanzkennzahlen werden unter Last eingehalten
- Es bestehen keine sicherheitsrelevanten Schwachstellen
- Die Anwendung ist leicht bedienbar für Endnutzer

---

## **4. Testkriterien definieren**

**4.1. Aussetzungskriterien (Suspension Criteria)**

- Kritische Fehler blockieren die Fortsetzung der Tests
- Fehlende Ressourcen oder Ausfall der Testumgebung
- Insolvenz des Kunden/ Vertragsbruch etc.
- signifikante Abweichung von den Requirements
- externe Dependencies nicht erreichbar (zB Netzwerkprobleme)
- wiederholte Abstürze während der Tests/ Software läuft instabil

**4.2. Abnahmekriterien (Exit Criteria)**

- Alle geplanten Tests wurden ausgeführt
- **Ausführungsrate:** Mindestens 95 % aller Testfälle wurden ausgeführt
- **Bestehensquote:** Mindestens 90 % der ausgeführten Testfälle bestanden
- Alle kritischen und hochpriorisierten Defekte sind geschlossen
- Es bestehen keine offenen Fehler der Schweregrade 1 oder 2
- Performanzanforderungen wurden erfüllt
- Sicherheitslücken wurden behoben
- Der Abnahmetest (UAT) wurde abgeschlossen und freigegeben
- Abgabe-Deadline
- entsprechende, übereinstimmende Meinung der Stakeholder

---

## **5. Ressourcenplanung**

- **Personelle Ressourcen:** QA-Team, Entwicklerteam, Endanwender für UAT
- **Hardware:** PCs, Laptops, Smartphones, Tablets
- **Software:** Aktuelle Browser (Chrome, Firefox, Safari, Edge), Betriebssysteme (Windows, macOS, Android, iOS)
- **Infrastruktur:** Testumgebungen, Automatisierungs-Tools, Performanztest-Werkzeuge, Testcase-Management-Software, Ticketsystem

## **6. Testumgebung planen**

- **Testgeräte:** Echte Endgeräte mit real installierten Betriebssystemen und Browsern zur realitätsnahen Simulation
- **Umgebungen:**
    - Entwicklung (DEV)
    - Test (TEST)
    - Abnahme (ACC – Acceptance)
    - Produktion (PROD)

## **7. Zeitplan und Aufwandsschätzung**

| **Aktivität** | **Startdatum** | **Enddatum** | **Umgebung** | **Verantwortlich** | **Geplanter Aufwand** |
| --- | --- | --- | --- | --- | --- |
| **Testplanung** | 01.08.2024 | 05.08.2024 | Alle | Testmanager | 20 Stunden |
| **Testfalldesign** | 06.08.2024 | 15.08.2024 | Alle | QA-Team | 40 Stunden |
| **Unittest** | 16.08.2024 | 25.08.2024 | DEV | Entwickler-Team | 60 Stunden |
| **Integrationstest** | 26.08.2024 | 30.08.2024 | TEST | QA-Team | 30 Stunden |
| **Systemtest** | 01.09.2024 | 10.09.2024 | TEST | QA-Team | 80 Stunden |
| **Regressions-Test** | 11.09.2024 | 15.09.2024 | TEST | QA-Team | 40 Stunden |
| **Performanztest** | 16.09.2024 | 18.09.2024 | TEST | QA-Team | 20 Stunden |
| **Sicherheitstest** | 19.09.2024 | 21.09.2024 | TEST | QA-Team | 20 Stunden |
| **Abnahmetest (UAT)** | 22.09.2024 | 30.09.2024 | ACC | Endanwender | 50 Stunden |
| **Produktivfreigabe** | 01.10.2024 | 01.10.2024 | PROD | DevOps-Team | 10 Stunden |

---

## **8. Testartefakte (Test-Deliverables)**

Folgende Dokumente und Werkzeuge werden im Rahmen des Testprozesses erstellt und bereitgestellt:

- Testplandokument
- Testfälle und Testskripte
- Testdaten
- Testberichte
- Fehlerberichte (Defect Reports)
- UAT-Freigabedokumentation (Sign-off)
