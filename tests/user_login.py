import time
import locators

class TestLoginPage:
    
    def test_user_login(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.login).click()
        time.sleep(5)
        assert driver.find_element(*locators.user_avatar).is_displayed() and "User." in driver.find_element(*locators.user_name).text

    
    def test_user_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.login).click()
        time.sleep(5)
        driver.find_element(*locators.exit_button).click()
        time.sleep(5)
        assert driver.find_element(*locators.login_button).is_displayed() and not driver.find_elements(*locators.user_avatar) and not driver.find_elements(*locators.user_name)

    
    