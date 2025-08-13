
import time
import random
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistrationPage:

    def generate_email(self):
       random_num = random.randint(1000, 9999)
       return f"test{random_num}@test.com"
    
    def test_user_valid_registration(self, driver):
        email = TestRegistrationPage.generate_email(self)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.no_account_button))
        driver.find_element(*Locators.no_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_email))
        driver.find_element(*Locators.imput_email).send_keys(email)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_password))
        driver.find_element(*Locators.imput_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.confirm_password))
        driver.find_element(*Locators.confirm_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.create_account_button))
        driver.find_element(*Locators.create_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.user_avatar))
        assert driver.find_element(*Locators.user_avatar).is_displayed() and "User." in driver.find_element(*Locators.user_name).text
    
    def test_user_not_valid_email_registration(self, driver):
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.no_account_button))
        driver.find_element(*Locators.no_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_email))
        driver.find_element(*Locators.imput_email).send_keys("aser5mail.ru")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_password))
        driver.find_element(*Locators.imput_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.confirm_password))
        driver.find_element(*Locators.confirm_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.create_account_button))
        driver.find_element(*Locators.create_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.text_error_email))
        assert "Ошибка" in  driver.find_element(*Locators.text_error_email).text and driver.find_element(*Locators.red_fields).is_displayed()
    
    def test_user_not_valid_password_registration(self, driver):
        email = TestRegistrationPage.generate_email(self) 
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.no_account_button))
        driver.find_element(*Locators.no_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_email))
        driver.find_element(*Locators.imput_email).send_keys(email)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.imput_password))
        driver.find_element(*Locators.imput_password).send_keys("2846")
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.confirm_password))
        driver.find_element(*Locators.confirm_password).send_keys("28467")
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.create_account_button))
        driver.find_element(*Locators.create_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.text_error_password))
        assert "Пароли не совпадают" in  driver.find_element(*Locators.text_error_password).text and driver.find_element(*Locators.red_fields).is_displayed()
 