from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLoginPage:
    def test_user_login(self, driver):
        driver.find_element(*Locators.login_button).click()   
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(Locators.imput_login_email))
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.imput_login_password))
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.login))
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.user_avatar))
        assert driver.find_element(*Locators.user_avatar).is_displayed() and "User." in driver.find_element(*Locators.user_name).text

    
    def test_user_logout(self, driver):
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located(Locators.imput_login_email))
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.imput_login_password))
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.login))
        driver.find_element(*Locators.login).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.exit_button))
        driver.find_element(*Locators.exit_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.user_avatar))
        assert driver.find_element(*Locators.login_button).is_displayed() and not driver.find_elements(*Locators.user_avatar) and not driver.find_elements(*Locators.user_name)

    
    