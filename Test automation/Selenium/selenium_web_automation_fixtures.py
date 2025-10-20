
"""
Web-Automatisierung eines Logins mit Selenium
Part 2: Parametrisierung und Fixtures

- Login-Skript erweitern, um Parametrisierung für verschiedene Benutzer zu nutzen
- Driver-Fixture erstellen, um den Webdriver wiederzuverwenden
- Alle auf https://www.saucedemo.com verfügbaren Benutzernamen testen
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# -----------------------------
# webdriver fixture
# -----------------------------
#setup the webdriver, open Chrome and the webpage
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


# -----------------------------
# password fixture
# -----------------------------
@pytest.fixture
def password(driver):
    # select container via XPath
    password_node = driver.find_element(By.XPATH, "//input[@data-test='password']")
    password_text = password_node.text.splitlines()[-1]
    return password_text


# -----------------------------
# get usernames
# -----------------------------
def get_users():
    driver.get("https://www.saucedemo.com/")
    credentials_box = driver.find_element(By.ID, "login_credentials")
    lines = credentials_box.text.splitlines()
    users = [line.strip() for line in lines if line.strip().endswith("user")]
    return users


# -----------------------------
# parametrized login function
# -----------------------------
@pytest.mark.parametrize("user", get_users())
def test_login(driver, user, password):
    login_box_username = driver.find_element(By.ID, "user-name")
    login_box_password = driver.find_element(By.ID, "password")

    login_box_username.send_keys(user)
    login_box_password.send_keys(password)

    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url.endswith("inventory.html"), f"Login für {user} nicht erfolgreich!"