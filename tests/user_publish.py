import time
import locators

class TestPublishPage:
    def test_unauthorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.post_button).click()
        time.sleep(5)
        assert driver.find_element(*locators.authorization_popup).is_displayed() and 'Чтобы разместить объявление, авторизуйтесь' in driver.find_element(*locators.test_error_post).text

    
    def test_authorized_announcement(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru")
        driver.find_element(*locators.login_button).click()
        time.sleep(1)
        driver.find_element(*locators.imput_login_email).send_keys("aser@mail.ru")
        time.sleep(1)
        driver.find_element(*locators.imput_login_password).send_keys("2846")
        time.sleep(1)
        driver.find_element(*locators.login).click()
        time.sleep(1)
        driver.find_element(*locators.post_button).click()
        time.sleep(5)
        driver.find_element(*locators.name).send_keys("название")
        time.sleep(1)
        driver.find_element(*locators.description).send_keys("описание")
        time.sleep(1)
        driver.find_element(*locators.price).send_keys("2345")
        time.sleep(1)
        driver.find_element(*locators.list_of_categories).click() 
        driver.find_element(*locators.books).click()
        time.sleep(1)
        driver.find_element(*locators.list_of_cities).click()
        driver.find_element(*locators.saint_petersburg).click()
        time.sleep(1)
        driver.find_element(*locators.radiobutton).click()
        time.sleep(1)
        driver.find_element(*locators.publish).click()
        time.sleep(1)
        driver.find_element(*locators.user_avatar).click()
        time.sleep(3)
        assert driver.find_element(*locators.card).is_displayed() and "название" in driver.find_element(*locators.card).text


