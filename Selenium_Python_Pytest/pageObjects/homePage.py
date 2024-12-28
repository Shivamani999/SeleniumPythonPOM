from selenium.webdriver.common.by import By

from pageObjects.productsPage import productsPage


class homePage:

    def __init__(self, driver):
        self.driver = driver

    shop_link_loc = (By.XPATH, "//a[text()='Shop']")
    name_loc = (By.NAME, "name")
    email_loc = (By.NAME, "email")
    password_loc = (By.ID, "exampleInputPassword1")
    dropdown_loc = (By.XPATH, "//Select[@id='exampleFormControlSelect1']")
    submit_loc = (By.XPATH, "//input[@value='Submit']")
    successMsg_loc = (By.XPATH, "//strong[text()='Success!']")

    def shop_link(self):
        self.driver.find_element(*homePage.shop_link_loc).click()
        return productsPage(self.driver)

    def name(self, name):
        self.driver.find_element(*homePage.name_loc).send_keys(name)

    def email(self, email):
        self.driver.find_element(*homePage.email_loc).send_keys(email)

    def password(self, password):
        self.driver.find_element(*homePage.password_loc).send_keys(password)

    def submit(self):
        self.driver.find_element(*homePage.submit_loc).click()

    def dropdown(self):
        return self.driver.find_element(*homePage.dropdown_loc)

    def relaod(self):
        self.driver.refresh()

    def successMsg(self):
        return self.driver.find_element(*homePage.successMsg_loc).text
