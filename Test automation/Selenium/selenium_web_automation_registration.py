from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

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
name_input_value = "Test User"
email_input_value = "test.user@whatever1.de"

signup_name = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
signup_name.send_keys(name_input_value)


signup_mail = driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
signup_mail.send_keys(email_input_value)


#7. Auf die Schaltfläche „Signup“ klicken
signup_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
signup_button.click()


#8. Überprüfen, dass „ENTER ACCOUNT INFORMATION“ sichtbar ist
account_creation_header = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.title.text-center")))
print("Account Creation Header ist sichtbar.")


#9. Details ausfüllen: Titel, Name, E-Mail, Passwort, Geburtsdatum

account_creation_title = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='id_gender2']")))
account_creation_title.click()

#9a. Für Name und Email überprüfen, ob die eingegebenen Werte korrekt übernommen wurden.
expected_values = {}
expected_values["name"] = name_input_value
expected_values["email"] = email_input_value
print(expected_values)

for element in expected_values:
    current_value = driver.find_element(By.ID, element).get_attribute("value")
    assert current_value == expected_values[element], f"Feld {element} wurde nicht korrekt übernommen!"
    print(f"Feld '{element}' wurde korrekt übernommen: {current_value}")

account_creation_password = driver.find_element(By.ID, "password")
password_value = "Test_Password"
account_creation_password.send_keys(password_value)

#9b. Geburtsdatum aus dropdown-Menü(s) auswählen.
date_of_birth_values = {"days": "20", "months": "2", "years":"2002"}

for select_id, date_of_birth_value in date_of_birth_values.items():
    dropdown_element = driver.find_element(By.ID, select_id)
    select = Select(dropdown_element)
    select.select_by_value(date_of_birth_value)

    selected_value = select.first_selected_option.get_attribute("value")
    assert selected_value == date_of_birth_value, f"Dropdown {select_id} stimmt nicht: {selected_value}"
    print(f"{select_id} korrekt gesetzt auf {selected_value}")


#10. Kontrollkästchen „Sign up for our newsletter!“ auswählen
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()


#11. Kontrollkästchen „Receive special offers from our partners!“ auswählen
partner_optin_checkbox = driver.find_element(By.ID, "optin")
partner_optin_checkbox.click()


#12. Details ausfüllen: Vorname, Nachname, Firma, Adresse, Adresse2, Land, Bundesstaat, Stadt, Postleitzahl, Handynummer
user_details = {
    "first_name": "Test",
    "last_name": "User",
    "company": "Automation GmbH",
    "address1": "Samplestreet 12",
    "address2": "1st floor",
    "country": "Australia",
    "state": "Bavaria",
    "city": "Sampletown",
    "zipcode": "12345",
    "mobile_number": "+4915112345678"
}

for user_detail, user_detail_value in user_details.items():
    detail = driver.find_element(By.ID, user_detail)
    detail.send_keys(user_detail_value)


#13. Auf die Schaltfläche „Create Account“ klicken

create_account_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
create_account_button.click()
time.sleep(200)

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
