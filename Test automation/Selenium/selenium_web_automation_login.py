"""
Web-Automatisierung eines Logins mit Selenium

1. Login-Automatisierung:
   - URL: https://www.saucedemo.com/
   - Benutzername: standard_user
   - Passwort: secret_sauce
   - Login-Button klicken
   - Erfolgreichen Login prüfen (z. B. Seitentitel oder Produktseite)
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


PASSWORD = "secret_sauce"
USERNAME = "standard_user"

def main():
    #set up the webdriver, open Chrome
    with webdriver.Chrome() as driver:
        login_user(driver, PASSWORD, USERNAME)
        verify_login_success(driver)
        verify_item_displayed(driver)


def login_user(driver, PASSWORD, USERNAME):

    #open the webpage
    driver.get("https://www.saucedemo.com/")

    #find login fields
    login_box_username = driver.find_element(By.ID, "user-name")
    login_box_password = driver.find_element(By.ID, "password")

    #login with the provided credentials
    login_box_username.send_keys(USERNAME)
    login_box_password.send_keys(PASSWORD)

    #click Login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    WebDriverWait(driver, 4).until(EC.url_contains("/inventory.html"))


def verify_login_success(driver):
    #assert successful login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login not successful!"
    print("Login Successful!")


"""
2. Produktprüfung:
   - Nach Login das Produkt "Sauce Labs Backpack" auf der Seite suchen
   - Assert, dass der Produktname angezeigt wird
"""

def verify_item_displayed(driver):
    #find the desired article
    sauce_lab_backpack = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

    #assert the desired article is displayed
    assert sauce_lab_backpack.is_displayed(), "Article not found!"
    print("Item displayed!")


if __name__ == "__main__":
    main()
