from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture()
def headless_setup():
    global driver
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    driver.get("https://www.opencart.com/")
    driver.maximize_window()
    yield
    driver.close()

def test_feature_menu(headless_setup):
    feature=driver.find_element(By.LINK_TEXT,"Features")
    feature.click()
    actual_title="OpenCart - Features"
    expected=driver.title
    assert actual_title. __eq__(expected)

def test_landing_page(headless_setup):
    Actual=driver.title
    expected = "OpenCart - Open Source Shopping Cart Solution"
    if Actual == expected:
        print("test is passed")
    else:
        print("test is failed")
