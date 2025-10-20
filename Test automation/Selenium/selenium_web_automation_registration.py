from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

"""
Part 3: Benutzer mit Selenium registrieren
"""

#0. Konstanten und Hilfsfunktionen

URL = "http://automationexercise.com"
SHORT_WAIT = 2
DEFAULT_WAIT = 5
EXTENDED_WAIT = 15

def wait_for_visible(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

#1. Browser starten
def main():
    with webdriver.Chrome() as driver:
        open_webpage_handle_cookies(driver)
        verify_landing_page(driver)
        (name_input_value, email_input_value) = signup_user(driver)
        enter_signup_data(driver, name_input_value, email_input_value)
        submit_signup_data(driver)
        verify_account_creation(driver)
        verify_logged_in_account_details(driver, name_input_value)
        delete_account(driver)
        verify_account_deletion(driver)

def open_webpage_handle_cookies(driver):
    #2. Zur URL navigieren:
    driver.get(URL)

    #2a. ggf. Cookie-Alert handlen
    try:
        consent_button = wait_for_clickable(driver, (By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button"), DEFAULT_WAIT)
        consent_button.click()
        print("Cookie-Banner geschlossen.")

    except TimeoutException:
        print("Kein Cookie-Banner gefunden (Timeout).")


def verify_landing_page(driver):
    #3. Überprüfen, dass die Startseite sichtbar ist
    assert "Automation Exercise" in driver.title, "Falsche Startseite geladen!"


def signup_user(driver):
    #4. Auf die Schaltfläche „Signup / Login“ klicken
    signup_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
    signup_button.click()

    #5. Überprüfen, dass „New User Signup!“ sichtbar ist
    try:
        signup_form = wait_for_visible(driver, (By.XPATH, "//h2[text()='New User Signup!']"), DEFAULT_WAIT)
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

    return (name_input_value, email_input_value)


def enter_signup_data(driver, name_input_value, email_input_value):
    #8. Überprüfen, dass „ENTER ACCOUNT INFORMATION“ sichtbar ist
    account_creation_header = wait_for_visible(driver, (By.CSS_SELECTOR, "h2.title.text-center"), SHORT_WAIT)
    print("Account Creation Header ist sichtbar.")

    #9. Details ausfüllen: Titel, Name, E-Mail, Passwort, Geburtsdatum
    account_creation_title = wait_for_clickable(driver, (By.CSS_SELECTOR, "input[id='id_gender2']"), DEFAULT_WAIT)
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


def submit_signup_data(driver):
    #13. Auf die Schaltfläche „Create Account“ klicken

    create_account_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    create_account_button.click()


def verify_account_creation(driver):
    #14. Überprüfen, dass „ACCOUNT CREATED!“ sichtbar ist
    account_creation_msg = wait_for_visible(driver, (By.CSS_SELECTOR, "h2[data-qa='account-created']"), DEFAULT_WAIT)
    assert account_creation_msg.is_displayed(), "Account-Erstellung fehlgeschlagen!"
    print("Account-Erstellung erfolgreich!")

    #15. Auf die Schaltfläche „Continue“ klicken
    continue_button = wait_for_visible(driver, (By.CSS_SELECTOR, "a[data-qa='continue-button']"), DEFAULT_WAIT)
    continue_button.click()


def verify_logged_in_account_details(driver, name_input_value):
    #16. Überprüfen, dass „Logged in as username“ sichtbar ist
    logged_in_as = wait_for_visible(driver, (By.CSS_SELECTOR, "li a:has(b)"), DEFAULT_WAIT)
    logged_in_as_who = logged_in_as.text.strip()
    assert name_input_value in logged_in_as_who, "Als falscher Nutzer eingeloggt!"


def delete_account(driver):
    #17. Auf die Schaltfläche „Delete Account“ klicken
    trash_button = driver.find_element(By.CSS_SELECTOR, "i[class='fa fa-trash-o']")
    trash_button.click()


def verify_account_deletion(driver):
    #18. Überprüfen, dass „ACCOUNT DELETED!“ sichtbar ist und auf „Continue“ klicken
    account_deletion_msg = wait_for_visible(driver, (By.CSS_SELECTOR, "h2[data-qa='account-deleted']" ), DEFAULT_WAIT)
    assert account_deletion_msg.is_displayed(), "Account-Löschung fehlgeschlagen!"
    print("Account-Löschung erfolgreich!")

    continue_button = wait_for_visible(driver, (By.CSS_SELECTOR, "a[data-qa='continue-button']"), DEFAULT_WAIT)
    continue_button.click()

if __name__ == "__main__":
    main()
