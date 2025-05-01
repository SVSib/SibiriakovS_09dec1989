import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.fullscreen_window()
    yield browser
    browser.quit()
