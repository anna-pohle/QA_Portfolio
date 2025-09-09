
"""
Web-Automatisierung eines Logins mit Selenium
Part 2: Parametrisierung und Fixtures

- Login-Skript erweitern, um Parametrisierung für verschiedene Benutzer zu nutzen
- Driver-Fixture erstellen, um den Webdriver wiederzuverwenden
- Alle auf https://www.saucedemo.com verfügbaren Benutzernamen testen
"""

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time


#setup the webdriver, open Chrome and the webpage
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# -----------------------------
# get usernames
# -----------------------------
# get container by ID
credentials_box = driver.find_element(By.ID, "login_credentials")

# extract & trim the usernames supplied in the container
lines = credentials_box.text.splitlines()
users = [line.strip() for line in lines if line.strip().endswith("user")]

# -----------------------------
# get password
# -----------------------------
# select container via CSS-Selector
password_node = driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2)")
password = password_node.text


"""
#find login fields
login_box_username = driver.find_element(By.ID, "user-name")
login_box_password = driver.find_element(By.ID, "password")

#login with the provided credentials
login_box_username.send_keys(USERNAME)
login_box_password.send_keys(PASSWORD)

#click Login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(2)

#assert successful login
webpage = driver.current_url
assert webpage == "https://www.saucedemo.com/inventory.html", "Login not successful!"


"""
"""
2. Produktprüfung:
   - Nach Login das Produkt "Sauce Labs Backpack" auf der Seite suchen
   - Assert, dass der Produktname angezeigt wird
"""
"""
#find the desired article
sauce_lab_backpack = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

#assert the desired article is displayed
assert sauce_lab_backpack != NoSuchElementException, "Article not found!"

#close the browser
driver.quit()



"""