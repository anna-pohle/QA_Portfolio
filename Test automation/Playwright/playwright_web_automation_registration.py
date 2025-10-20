from playwright.sync_api import sync_playwright, expect

URL = "http://automationexercise.com"
SHORT_WAIT = 2000  # ms
DEFAULT_WAIT = 5000
EXTENDED_WAIT = 15000


def main():
    with sync_playwright() as playwright:
        # 1. Browser starten & neue Seite öffnen
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()

        open_webpage_handle_cookies(page)
        verify_landing_page(page)
        name_input_value, email_input_value = signup_user(page)
        enter_signup_data(page, name_input_value, email_input_value)
        submit_signup_data(page)
        verify_account_creation(page)
        verify_logged_in_account_details(page, name_input_value)
        delete_account(page)
        verify_account_deletion(page)
        browser.close()


def open_webpage_handle_cookies(page):
    page.goto(URL)
    try:
        consent_button = page.locator('button.fc-button.fc-cta-consent.fc-primary-button[aria-label="Einwilligen"]')
        consent_button.click(timeout=SHORT_WAIT)
        print("Cookie-Banner geschlossen.")
    except:
        print("Kein Cookie-Banner gefunden.")


def verify_landing_page(page):
    assert "Automation Exercise" in page.title(), "Falsche Startseite geladen!"


def signup_user(page):
    # 4. Auf die Schaltfläche „Signup / Login“ klicken
    signup_button = page.locator("text='Signup / Login'")
    signup_button.click()

    # 5. Überprüfen, dass „New User Signup!“ sichtbar ist
    signup_form = page.locator("//h2[text()='New User Signup!']")
    expect(signup_form).to_be_visible(timeout=DEFAULT_WAIT)
    print("Signup-Formular ist sichtbar.")

    # 6. Namen und E-Mail-Adresse eingeben
    name_input_value = "Test User"
    email_input_value = "test.user@whatever1.de"

    page.locator("input[data-qa='signup-name']").fill(name_input_value)
    page.locator("input[data-qa='signup-email']").fill(email_input_value)

    # 7. Auf die Schaltfläche „Signup“ klicken
    page.locator("button[data-qa='signup-button']").click()

    return name_input_value, email_input_value


def enter_signup_data(page, name_input_value, email_input_value):
    # 8. Überprüfen, dass „ENTER ACCOUNT INFORMATION“ sichtbar ist
    account_creation_header = page.locator("h2.title.text-center >> text='Enter Account Information'")
    expect(account_creation_header).to_be_visible(timeout=SHORT_WAIT)
    print("Account Creation Header ist sichtbar.")

    # 9. Details ausfüllen: Titel auswählen
    page.locator("input[id='id_gender2']").click()

    # Name und Email überprüfen
    expected_values = {"name": name_input_value, "email": email_input_value}
    for field_id, expected in expected_values.items():
        current_value = page.locator(f"#{field_id}").input_value()
        assert current_value == expected, f"Feld {field_id} wurde nicht korrekt übernommen!"
        print(f"Feld '{field_id}' korrekt: {current_value}")

    # Passwort
    password_value = "Test_Password"
    page.locator("#password").fill(password_value)

    # Geburtsdatum über Dropdowns
    date_of_birth_values = {"days": "20", "months": "2", "years": "2002"}
    for select_id, value in date_of_birth_values.items():
        page.locator(f"#{select_id}").select_option(value)
        selected = page.locator(f"#{select_id}").input_value()
        assert selected == value, f"Dropdown {select_id} stimmt nicht: {selected}"
        print(f"{select_id} korrekt gesetzt: {selected}")

    # Newsletter & Partner-Optin
    page.locator("#newsletter").check()
    page.locator("#optin").check()

    # User Details
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
    dropdown_ids = ["country"]

    for field_id, value in user_details.items():
            if field_id in dropdown_ids:
                page.locator(f'#{field_id}').select_option(value)
            else:
                page.locator(f"#{field_id}").fill(value)


def submit_signup_data(page):
    page.locator("button[data-qa='create-account']").click()
    page.wait_for_timeout(2000)  # optional, kurze Pause


def verify_account_creation(page):
    account_creation_msg = page.locator("h2[data-qa='account-created']")
    expect(account_creation_msg).to_be_visible(timeout=DEFAULT_WAIT)
    print("Account-Erstellung erfolgreich!")

    page.locator("a[data-qa='continue-button']").click()


def verify_logged_in_account_details(page, name_input_value):
    logged_in_as = page.locator("li a:has(b)")
    expect(logged_in_as).to_be_visible(timeout=EXTENDED_WAIT)
    logged_in_as_who = logged_in_as.inner_text().strip()
    assert name_input_value in logged_in_as_who, "Als falscher Nutzer eingeloggt!"


def delete_account(page):
    page.locator("i[class='fa fa-trash-o']").click()


def verify_account_deletion(page):
    account_deletion_msg = page.locator("h2[data-qa='account-deleted']")
    expect(account_deletion_msg).to_be_visible(timeout=DEFAULT_WAIT)
    print("Account-Löschung erfolgreich!")

    page.locator("a[data-qa='continue-button']").click()


if __name__ == "__main__":
    main()
