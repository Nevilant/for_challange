import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_collecting_prices(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    collecting_prices: list[WebElement] = driver.find_elements(By.CSS_SELECTOR, 'span[data-price-type="finalPrice"]')

    price_list = [price.text[1:] for price in collecting_prices]

    print(price_list)

    assert len(price_list) > 0, "Цены не были найдены на странице"
