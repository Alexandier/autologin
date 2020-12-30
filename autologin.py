from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def kirjaudu(username, password):
    driver = webdriver.Chrome(executable_path='../driver/chromedriver')
    path = "https://www.instagram.com/"
    driver.get(path)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ' // button[contains(text(), "Hyväksy")]'))).click()
    usrn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    usrn.clear()
    usrn.send_keys(username)
    psw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    psw.clear()
    psw.send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    sleep(3)
    if (driver.current_url != path):
        f = open("tunnukset.txt", "a")
        f.write(username + " : " + password + "\n")
        f.close()
    driver.close()
