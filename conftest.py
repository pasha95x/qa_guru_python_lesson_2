import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_size():
    # Setting the window size to 1920 * 1080
    browser.config.window_height = 1080
    browser.config.window_width = 1920

