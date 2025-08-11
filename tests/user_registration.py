
import time
import random
import locators

class TestRegistrationPage:

    def generate_email(self):
       random_num = random.randint(1000, 9999)
       return f"test{random_num}@test.com"
    
    def test_user_valid_registration(self, driver):
        email = TestRegistrationPage.generate_email(self)
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_email).send_keys(email)
        time.sleep(1)
        driver.find_element(*locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.confirm_password).send_keys("2846")
        time.sleep(5)
        driver.find_element(*locators.create_account_button).click()
        time.sleep(5)
        assert driver.find_element(*locators.user_avatar).is_displayed() and "User." in driver.find_element(*locators.user_name).text
    
    def test_user_not_valid_email_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_email).send_keys("aser5mail.ru")
        time.sleep(1)
        driver.find_element(*locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.confirm_password).send_keys("2846")
        time.sleep(5)
        driver.find_element(*locators.create_account_button).click()
        time.sleep(5)
        assert "Ошибка" in  driver.find_element(*locators.text_error_email).text and driver.find_element(*locators.red_fields).is_displayed()
    
    def test_user_not_valid_password_registration(self, driver):
        email = TestRegistrationPage.generate_email(self) 
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.no_account_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_email).send_keys(email)
        time.sleep(1)
        driver.find_element(*locators.imput_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.confirm_password).send_keys("28467")
        time.sleep(5)
        driver.find_element(*locators.create_account_button).click()
        time.sleep(5)
        assert "Пароли не совпадают" in  driver.find_element(*locators.text_error_password).text and driver.find_element(*locators.red_fields).is_displayed()
 