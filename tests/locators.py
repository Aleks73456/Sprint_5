from selenium.webdriver.common.by import By

class Locators:
#test_user_valid_registration
    login_button = (By.XPATH, "//div/div[1]/div/button")
    no_account_button = (By.XPATH, "//div/div[2]/div[5]/form/div[3]/button[2]")
    imput_email = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[1]/div/div/input")
    imput_password = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[2]/div/div/input")
    confirm_password = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[3]/div/div/input")
    create_account_button = (By.XPATH, "//div/div[2]/div[5]/form/div[3]/button[1]")
    user_avatar = (By.CLASS_NAME, "circleSmall")
    user_name = (By.CLASS_NAME, "columnSmall")

#test_user_not_valid_email_registration
    text_error_email = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[1]/span")
    red_fields = (By.XPATH, "//div[contains(@class, 'input_inputError__fLUP9')]")

#test_user_not_valid_password_registration
    text_error_password = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[1]/span")

#test_user_login
    imput_login_email = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[1]/div/div/input")
    imput_login_password = (By.XPATH, "//div/div[2]/div[5]/form/div[2]/div[2]/div/div/input")
    login = (By.XPATH, "//div/div[2]/div[5]/form/div[3]/button[1]")

#test_user_logout
    exit_button = (By.CSS_SELECTOR, ".spanGlobal.btnSmall")

#test_unauthorized_announcement
    post_button = (By.CSS_SELECTOR, ".buttonPrimary.inButtonText.undefined")
    authorization_popup = (By.CSS_SELECTOR, ".popUp_shell__LuyqR")
    test_error_post = (By.XPATH, "//div/div[2]/div[5]/form/div[1]/h1")

#test_authorized_announcement
    name = (By.XPATH, "//div/div[2]/div/form/div[2]/div[1]/div/div/input")
    description = (By.XPATH, "//div/div[2]/div/form/div[4]/div/textarea")
    price = (By.XPATH, "//div/div[2]/div/form/div[5]/div/div/input")
    list_of_categories = (By.XPATH, "//div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    books = (By.XPATH, "//div/div[2]/div/form/div[2]/div[2]/div[2]/button[2]")
    list_of_cities = (By.XPATH, "//div/div[2]/div/form/div[3]/div[1]/button")
    saint_petersburg = (By.XPATH, "//div/div[2]/div/form/div[3]/div[2]/button[2]")
    radiobutton = (By.XPATH, "//div/div[2]/div/form/fieldset/div/div[2]/div")
    publish = (By.XPATH, "//div/div[2]/div/form/button")
    card = (By.CSS_SELECTOR, ".card")
