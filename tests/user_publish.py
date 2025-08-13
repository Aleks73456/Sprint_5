import time
from locators import Locators

class TestPublishPage:
    def test_unauthorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.post_button).click()
        time.sleep(5)
        assert driver.find_element(*Locators.authorization_popup).is_displayed() and 'Чтобы разместить объявление, авторизуйтесь' in driver.find_element(*Locators.test_error_post).text

    
    def test_authorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*Locators.login_button).click()
        time.sleep(1)
        driver.find_element(*Locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*Locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*Locators.login).click()
        time.sleep(1)
        driver.find_element(*Locators.post_button).click()
        time.sleep(5)
        driver.find_element(*Locators.name).send_keys("название")
        time.sleep(1)
        driver.find_element(*Locators.description).send_keys("описание")
        time.sleep(1)
        driver.find_element(*Locators.price).send_keys("2345")
        time.sleep(1)
        driver.find_element(*Locators.list_of_categories).click() 
        driver.find_element(*Locators.books).click()
        time.sleep(1)
        driver.find_element(*Locators.list_of_cities).click()
        driver.find_element(*Locators.saint_petersburg).click()
        time.sleep(1)
        driver.find_element(*Locators.radiobutton).click()
        time.sleep(1)
        driver.find_element(*Locators.publish).click()
        time.sleep(1)
        driver.find_element(*Locators.user_avatar).click()
        time.sleep(3)
        assert driver.find_element(*Locators.card).is_displayed() and "название" in driver.find_element(*Locators.card).text


