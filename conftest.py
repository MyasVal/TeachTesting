import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Инициализация драйвера
    yield driver  # Передача драйвера в тест
    driver.quit()  # Завершение работы с драйвером после завершения теста
