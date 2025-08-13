from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import time

class TestPublishPage:
    def test_unauthorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.post_button).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(Locators.authorization_popup))
        assert driver.find_element(*Locators.authorization_popup).is_displayed() and 'Чтобы разместить объявление, авторизуйтесь' in driver.find_element(*Locators.test_error_post).text

    
    def test_authorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_login_email))
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_login_password))
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.login))
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.post_button))
        time.sleep(1)
        driver.find_element(*Locators.post_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.name))
        driver.find_element(*Locators.name).send_keys("название")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.description))
        driver.find_element(*Locators.description).send_keys("описание")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.price))
        driver.find_element(*Locators.price).send_keys("2345")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.list_of_categories))
        driver.find_element(*Locators.list_of_categories).click() 
        driver.find_element(*Locators.books).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.list_of_cities))
        driver.find_element(*Locators.list_of_cities).click()
        driver.find_element(*Locators.saint_petersburg).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.radiobutton))
        driver.find_element(*Locators.radiobutton).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.publish))
        time.sleep(1)
        driver.find_element(*Locators.publish).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.user_avatar))
        time.sleep(1)
        driver.find_element(*Locators.user_avatar).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.card))
        assert driver.find_element(*Locators.card).is_displayed() and "название" in driver.find_element(*Locators.card).text


