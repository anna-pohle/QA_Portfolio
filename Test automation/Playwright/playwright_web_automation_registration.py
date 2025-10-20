from playwright.sync_api import sync_playwright

"""
Benutzer mit Playwright registrieren
"""
URL = "http://automationexercise.com"


def main():
    with sync_playwright() as playwright:
        # 1. Browser starten & neue Seite öffnen
        browser = playwright.chromium.launch(headless=False, slow_mo=30000)
        page = browser.new_page()

        open_webpage_handle_cookies(page)
        verify_landing_page(page)
        (name_input_value, email_input_value) = signup_user(page)
        enter_signup_data(page, name_input_value, email_input_value)
        submit_signup_data(page)
        verify_account_creation(page)
        verify_logged_in_account_details(page, name_input_value)
        delete_account(page)
        verify_account_deletion(page)


def open_webpage_handle_cookies(page):
    #2. Zur URL navigieren:
    page.goto(URL)

    #2a. ggf. Cookie-Alert handlen
    try:
        consent_button = page.locator('button.fc-button.fc-cta-consent.fc-primary-button[aria-label="Einwilligen"]')
        consent_button.click()
        print("Cookie-Banner geschlossen.")
    except:
        print("Kein Cookie-Banner gefunden.")


def verify_landing_page(page):
    #3. Überprüfen, dass die Startseite erfolgreich sichtbar ist
    body_element = driver.find_element(By.TAG_NAME, "body")
    assert body_element.text.strip() != "", "Body not displayed correctly!"


def signup_user(page):
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

    return (name_input_value, email_input_value)


def enter_signup_data(page, name_input_value, email_input_value):
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


def submit_signup_data(page):
    #13. Auf die Schaltfläche „Create Account“ klicken

    create_account_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    create_account_button.click()
    time.sleep(2)


def verify_account_creation(page):
    #14. Überprüfen, dass „ACCOUNT CREATED!“ sichtbar ist
    account_creation_msg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-created']")))
    assert account_creation_msg.is_displayed(), "Account-Erstellung fehlgeschlagen!"
    print("Account-Erstellung erfolgreich!")

    #15. Auf die Schaltfläche „Continue“ klicken
    continue_button = WebDriverWait(driver, 5). until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
    continue_button.click()


def verify_logged_in_account_details(page, name_input_value):
    #16. Überprüfen, dass „Logged in as username“ sichtbar ist
    logged_in_as = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li a:has(b)")))
    logged_in_as_who = logged_in_as.text.strip()
    assert name_input_value in logged_in_as_who, "Als falscher Nutzer eingeloggt!"


def delete_account(page):
    #17. Auf die Schaltfläche „Delete Account“ klicken
    trash_button = driver.find_element(By.CSS_SELECTOR, "i[class='fa fa-trash-o']")
    trash_button.click()


def verify_account_deletion(page):
    #18. Überprüfen, dass „ACCOUNT DELETED!“ sichtbar ist und auf „Continue“ klicken
    account_deletion_msg = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-deleted']" )))
    assert account_deletion_msg.is_displayed(), "Account-Löschung fehlgeschlagen!"
    print("Account-Löschung erfolgreich!")

    continue_button = WebDriverWait(driver, 5). until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-qa='continue-button']")))
    continue_button.click()


if __name__ == "__main__":
    main()
