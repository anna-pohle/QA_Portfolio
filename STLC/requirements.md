### **Die Software: MarketMate**

URL: https://grocerymate.masterschool.com/

Online-Shopping-Plattform mit den folgenden Funktionalitäten:

- Online Lebensmittel & Haushaltswaren kaufen & liefern lassen
- altersbedingte Filterung der Artikel (Alkohol erst ab 18)
- Nutzerprofile erstellen und Favoriten verwalten
- Customer Support kontaktieren
- Firma auf Social Media kontaktieren

### **Neue Funktionen (Features)**

### 1. Produktbewertungssystem

**Unklare Anforderung:**

Nutzer sollten in der Lage sein, Waren mit einem 5-Sterne-System zu bewerten und die Option haben, schriftliches Feedback zu hinterlassen

**Fragen zur Anforderungsklärung:**

1. Muss man eingeloggt sein, um Sterne-Bewertungen oder schriftliche Bewertungen zu hinterlassen?
2. Können Null Sterne vergeben werden?
3. Gibt es eine Moderation oder einen Schimpfwortfilter für die schriftlichen Bewertungen?
4. Gibt es eine Zeichenbegrenzung für die schriftliche Bewertung? Wenn ja: Wie& wann wird der Nutzer darüber informiert?
5. Können Bilder/Markdown/Emojis in die schriftlichen Bewertungen eingefügt werden?
6. Kann ein user das gleiche Produkt mehrfach bewerten?

**Detaillierte Anforderung:**

Nicht eingeloggte User können keine Produkte bewerten.
Nur eingeloggte Nutzer, die ein Produkt gekauft haben sollten in der Lage sein, Waren mit einem 5-Sterne-System zu bewerten und die Option haben, schriftliches Feedback ohne Moderation oder Schimpfwortfilter zu hinterlassen.

Es ist möglich zwischen 1 und 5 Sterne auszuwählen, in dem man nach der erfolgten Lieferung zum Produkt navigiert, in dieser unter dem erworbenen Produkt die gewünschte Sternezahl anklickt darunter auf ‘Send’ klickt. 
Ebenfalls innerhalb dieses Bewertungsfeldes gibt es die Möglichkeit vor dem Absenden der Sternebewertung, ein Textfeld mit einer schriftlichen Bewertung von maximal 500 Zeichen auszufüllen. Unterhalb des Eingabefeldes gibt es einen counter im Stil von “35/500” Zeichen, der in Echtzeit anzeigt, wie viele Zeichen dem Nutzer noch bleiben. Sobald 500 Zeichen erreicht sind, wird der counter rot und lautet “You cannot tell us more about this product.”. Es können nicht mehr als 500 Zeichen eingegeben werden.
Eingegebener Text mit Markdown und Emojis werden später als leerer Text  angezeigt, können aber eingegeben werden; die eingegebene Sternebewertung wird in diesem Fall ganz normal angezeigt.

Ein User kann pro Produkt nur einmal eine Bewertung abgeben, ungeachtet dessen, ob er:sie den Artikel ein weiteres Mal gekauft hat. In diesem Fall erscheint unter dem Produkt der Hinweis “You have already reviewed this product.”

### **2. Altersbeschränkung für Alkoholische Produkte**

**Unklare Anforderung:**

Alkoholische Produkte benötigen eine Altersprüfung. Ein Eingabefeld soll erscheinen, wenn der Nutzer zu den alkoholischen Produkten navigiert, mit dem überprüft wird, ob der User 18+ ist. User müssen ihr Alter eingeben, bevor sie auf die alkoholischen Produkte zugreifen können.

**Fragen zur Anforderungsklärung:**

1. Wie soll die Altersverifikation umgesetzt werden? (z. B. Eingabe des Geburtsdatums)
2. In welchem Format soll das Geburtsdatum eingegeben werden? (z. B. TT/MM/JJJJ)
3. Welche Fehlermeldung soll angezeigt werden, wenn der Nutzer unter 18 ist?
4. Was soll das Verhalten der Website sein, wenn der User genau 18 ist?
5. Welche Waren genau dürfen ohne Altersverifikation nicht angezeigt werden? (Zählt zB die Kategorie ‘Alkoholisches’ oder der tatsächliche Alkoholgehalt [z.B. bei 0,0%-Bier])
6. Dürfen die Waren für U18-User nicht *angezeigt* oder nicht *auswählbar* sein?

**Detaillierte Anforderung:**

Bereits nach dem Öffnen der Website muss der Nutzer sein Geburtsdatum in der Form DD-MM-YYYY angeben. Das System validiert, ob der Nutzer am Tag der Kontoerstellung auf den Tag genau mindestens 18 Jahre alt (oder älter) ist. Falls der Nutzer (auch nur einen Tag) unter 18 ist oder ein invalides Datum eingibt (zB eines, das Buchstaben beinhaltet oder im falschen Format eingegeben wird), wird eine Meldung angezeigt, dass der Nutzer minderjährig ist und nur ein eingeschränktes Sortiment sehen kann.

In diesem Falle wird die gesamte Warengruppe “Alcohol”  nicht mehr angezeigt, der tatsächliche Alkoholgehalt des Produktes spielt dabei keine Rolle. Stattdessen erscheint eine freundliche Grafik, dass keine Produkte gefunden wurden sowie die folgende Meldung: “Underage Notice: You are underage and cannot view alcohol products. Please wait until you are 18 or older to access these products.”

### **3. veränderte Versandkosten**

**Unklare Anforderung:**

Oberhalb eines bestimmen Betrages ist der Versand kostenfrei. Für Bestellungen unterhalb des Schwellwertes fallen Versandkosten an.

**Fragen zur Anforderungsklärung:**

1. Was genau ist der Schwellwert für kostenlosen Versand?
2. Gib es andere Bedingungen, die für kostenlosen Versand erfüllt sein müssen? (zB Maße, Maximalgewicht, Zielland)
3. Wie genau wird die Bestellsumme berechnet (werden zB Rabatte vorher schon abgezogen)?
4. Sind die Versandkosten unterhalb des Schwellwertes einheitlich? Wenn nein: nach welchen Parametern ändern diese sich? (zB Maße, Gewicht, Versandart, Versandanbieter, Zielland)
5. Was passiert, wenn ein Kunde einen Artikel zurückgibt & die ursprüngliche Bestellung damit unter den Schwellwert fällt? Muss er den Versand dann nachzahlen?

**Detaillierte Anforderung:**

**Oberhalb** eines Betrages von 20€ (also ab 20,01€) ist der Versand kostenfrei; hierbei gibt es keinerlei Beschränkungen, was Maße, Zusammensetzung oder Gewicht der Lieferung angeht. 
Für Bestellungen **unterhalb** des Schwellwertes fallen 5€ Versandkosten an.

Sollte ein Kunde einen Artikel zurückgeben & die ursprüngliche Bestellung damit unter den Schwellwert fallen, muss er lediglich das Retourenetikett zahlen.

Sollte ein Kunde einen Artikel zurückgeben & die ursprüngliche Bestellung damit NICHT unter den Schwellwert fallen, ist das Retourenetikett kostenlos.
