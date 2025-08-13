
import time
import random
from locators import Locators

class TestRegistrationPage:

    def generate_email(self):
       random_num = random.randint(1000, 9999)
       return f"test{random_num}@test.com"
    
    def test_user_valid_registration(self, driver):
        email = TestRegistrationPage.generate_email(self)
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_email).send_keys(email)
        time.sleep(1)
        driver.find_element(*Locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.confirm_password).send_keys("2846")
        time.sleep(5)
        driver.find_element(*Locators.create_account_button).click()
        time.sleep(5)
        assert driver.find_element(*Locators.user_avatar).is_displayed() and "User." in driver.find_element(*Locators.user_name).text
    
    def test_user_not_valid_email_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_email).send_keys("aser5mail.ru")
        time.sleep(1)
        driver.find_element(*Locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.confirm_password).send_keys("2846")
        time.sleep(5)
        driver.find_element(*Locators.create_account_button).click()
        time.sleep(5)
        assert "Ошибка" in  driver.find_element(*Locators.text_error_email).text and driver.find_element(*Locators.red_fields).is_displayed()
    
    def test_user_not_valid_password_registration(self, driver):
        email = TestRegistrationPage.generate_email(self) 
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_email).send_keys(email)
        time.sleep(1)
        driver.find_element(*Locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.confirm_password).send_keys("28467")
        time.sleep(5)
        driver.find_element(*Locators.create_account_button).click()
        time.sleep(5)
        assert "Пароли не совпадают" in  driver.find_element(*Locators.text_error_password).text and driver.find_element(*Locators.red_fields).is_displayed()
 