import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def browser_size():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    # Setting the window size to 1200 * 800
    driver.set_window_size(200, 800)
