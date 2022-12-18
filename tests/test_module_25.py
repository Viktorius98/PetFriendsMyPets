import time
from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('c:/skillfactory/chromedriver.exe')

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, "email").send_keys('vasya@mail.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, "pass").send_keys('12345')

    time.sleep(5)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(5)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    time.sleep(5)
    # Нажимаем на кнопку "Мои Питомцы"
    pytest.driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()

    time.sleep(10)
    WebDriverWait(testing, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    #
    pytest.driver.find_element(By.CSS_SELECTOR, '#all_my_pets table tbody tr')
    all_my_pets_number = pytest.driver.find_element((By.XPATH, '//div[contains(@class, ".col-sm-4 left")]/text()[2]'))

    images = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located(By.CSS_SELECTOR, ".card-deck .card-img-top"))
    names = WebDriverWait(pytest.driver, 10).until(
       EC.presence_of_all_elements_located(By.CSS_SELECTOR, ".card-deck .card-title"))
    descriptions = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located(By.CSS_SELECTOR, ".card-deck .card-text"))

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0