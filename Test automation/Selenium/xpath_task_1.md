#1. Schreibe das XPath, um das Haupt-**h1**Element zu finden.
//h1

#2. Schreibe das XPath, um den Navigationslink **About Us** auszuwählen.
//a[@href="#about"]

#3. Schreibe das XPath, um den Dropdown-Link **Graphic Design** auszuwählen.
//a[@href="#graphicdesign"]

#4. Schreibe das XPath, um den Namen des Teammitglieds **Jane Smith** auszuwählen.
//h4[contains(text(), 'Jane Smith')]

#5. Schreibe das XPath, um die Beschreibung (die sich im Absatz befindet) der **SEO Services** auszuwählen.
//p[contains(text(), 'Improving search engine rankings.')]

#6. Schreibe einen XPath-Ausdruck, um alle Service-Elemente im Abschnitt "**Our Services**" auszuwählen.#
//div[@class='service-list']/descendant::*

#7. Wie lautet das XPath, um das **E-Mail-Eingabefeld** im Kontaktformular auszuwählen?
//input[@id='email']

#8. Wie würdest du ein XPath schreiben, um das **gesamte Kontaktformular** auszuwählen?
//form[@id='contactForm']

#9. Gib das XPath an, um das **Footer-Absatz-Element** auszuwählen.
//footer/p

#10. Was ist das XPath, um den Namen (`<h4>`) des **ersten Teammitglieds** auszuwählen?
//li/h4[contains(text(), 'John Doe')]

#11. Wie kannst du mit XPath die Beschreibung des **zweiten Service-Elements** auswählen?
//div[@class='service-item'][2]/p

#12. Was ist das XPath, um die Überschrift der Sektion **"Contact Us"** (`<h2>`Element) auszuwählen?
//section/h2[@class='sectionTitle' and contains(text(), 'Contact Us')]

#13. Schreibe einen XPath-Ausdruck, um alle Links innerhalb des Dropdowns unter dem Navigationspunkt **"Services"** auszuwählen.
//ul[@class='dropdown']/li/a

#14. Was ist das XPath, um das erste `<li>` im Abschnitt **"Our Team"** auszuwählen?
//div[@class='team']/ul/li[1]

#15. Gib das XPath an, um die Schaltfläche **"Send Message"** im Kontaktformular zu finden.
//input[@type='submit']
