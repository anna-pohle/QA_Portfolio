from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

"""
Part 3: Benutzer mit Selenium registrieren
"""
URL = "http://automationexercise.com"

#1. Browser starten
driver = webdriver.Chrome()


#2. Zur URL navigieren:
driver.get(URL)


#2a. ggf. Cookie-Alert handlen
try:
    consent_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button")))
    consent_button.click()
    print("Cookie-Banner geschlossen.")

except:
    print("Kein Cookie-Banner gefunden.")


#3. Überprüfen, dass die Startseite erfolgreich sichtbar ist
body_element = driver.find_element(By.TAG_NAME, "body")
assert body_element.text.strip() != "", "Body not displayed correctly!"


#4. Auf die Schaltfläche „Signup / Login“ klicken
signup_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
signup_button.click()


#5. Überprüfen, dass „New User Signup!“ sichtbar ist
try:
    signup_form = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))
    print("Signup-Formular ist sichtbar.")

except:
    print("Signup-Formular NICHT gefunden.")


#6. Namen und E-Mail-Adresse eingeben
signup_name = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
signup_name.send_keys("Test User")


signup_mail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
signup_mail.send_keys("test.user@whatever.de")


#7. Auf die Schaltfläche „Signup“ klicken
signup_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
signup_button.click()


#8. Überprüfen, dass „ENTER ACCOUNT INFORMATION“ sichtbar ist
account_creation_header = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.title.text-center")))
print("Account Creation Header ist sichtbar.")


#9. Details ausfüllen: Titel, Name, E-Mail, Passwort, Geburtsdatum
#10. Kontrollkästchen „Sign up for our newsletter!“ auswählen
#11. Kontrollkästchen „Receive special offers from our partners!“ auswählen
#12. Details ausfüllen: Vorname, Nachname, Firma, Adresse, Adresse2, Land, Bundesstaat, Stadt, Postleitzahl, Handynummer
#13. Auf die Schaltfläche „Create Account“ klicken
#14. Überprüfen, dass „ACCOUNT CREATED!“ sichtbar ist
#15. Auf die Schaltfläche „Continue“ klicken
#16. Überprüfen, dass „Logged in as username“ sichtbar ist
#17. Auf die Schaltfläche „Delete Account“ klicken
#18. Überprüfen, dass „ACCOUNT DELETED!“ sichtbar ist und auf „Continue“ klicken


"""

#1. Launch the browser
#2. Navigate to the URL: [https://automationexercise.com](http://automationexercise.com)
#3. Verify that the homepage is displayed successfully
#4. Click on the “Signup / Login” button
#5. Verify that “New User Signup!” is visible
#6. Enter name and email address
#7. Click the “Signup” button
#8. Verify that “ENTER ACCOUNT INFORMATION” is visible
#9. Fill in details: title, name, email, password, date of birth
#10. Check the box “Sign up for our newsletter!”
#11. Check the box “Receive special offers from our partners!”
#12. Fill in details: first name, last name, company, address, address2, country, state, city, zip code, mobile number
#13. Click the “Create Account” button
#14. Verify that “ACCOUNT CREATED!” is visible
#15. Click the “Continue” button
#16. Verify that “Logged in as username” is visible
#17. Click the “Delete Account” button
#18. Verify that “ACCOUNT DELETED!” is visible and click “Continue”
"""
