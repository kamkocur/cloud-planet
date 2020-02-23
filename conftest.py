import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.invoice import InvoiceFeature


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://ingksiegowosc.pl/')
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.invoice_feature = InvoiceFeature(driver)
    yield
    driver.quit()
