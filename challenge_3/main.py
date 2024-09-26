import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test(driver):
    driver.get("https://demoblaze.com/index.html")

    samsung_s6: WebElement = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Samsung galaxy s6')))
    samsung_s6.click()
    button_add_to_cart: WebElement = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')))
    for _ in range(2):
        button_add_to_cart.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    button_cart: WebElement = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'cartur')))
    button_cart.click()
    delete_button: WebElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Delete')))
    delete_button.click()
