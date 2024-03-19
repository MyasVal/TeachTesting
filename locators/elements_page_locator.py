from selenium.webdriver.common.by import By


class TextBoxPageLocator:

    # from fields

    FULL_NAME= (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "input[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "input[id='submit']")

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "input[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "input[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "input[id='permanentAddress']")
