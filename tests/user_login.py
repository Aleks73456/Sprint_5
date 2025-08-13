import time
from locators import Locators

class TestLoginPage:
    
    def test_user_login(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.login).click()
        time.sleep(5)
        assert driver.find_element(*Locators.user_avatar).is_displayed() and "User." in driver.find_element(*Locators.user_name).text

    
    def test_user_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.login).click()
        time.sleep(5)
        driver.find_element(*Locators.exit_button).click()
        time.sleep(5)
        assert driver.find_element(*Locators.login_button).is_displayed() and not driver.find_elements(*Locators.user_avatar) and not driver.find_elements(*Locators.user_name)

    
    