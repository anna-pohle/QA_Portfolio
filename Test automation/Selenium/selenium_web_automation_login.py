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
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

PASSWORD = "secret_sauce"
USERNAME = "standard_user"

#setup the webdriver, open Chrome
driver = webdriver.Chrome()

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

time.sleep(2)

#assert successful login
webpage = driver.current_url
assert webpage == "https://www.saucedemo.com/inventory.html", "Login not successful!"


"""
2. Produktprüfung:
   - Nach Login das Produkt "Sauce Labs Backpack" auf der Seite suchen
   - Assert, dass der Produktname angezeigt wird
"""

#find the desired article
sauce_lab_backpack = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")

#assert the desired article is displayed
assert sauce_lab_backpack != NoSuchElementException, "Article not found!"

#close the browser
driver.quit()
