from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import checkoutPage


class productsPage:

    def __init__(self, driver):
        self.driver = driver

    products_loc = (By.XPATH, "//div[@class='card h-100']")
    checkout_link_loc = (By.XPATH, "//a[contains(text(),'Checkout')]")
    checkout_button_loc = (By.XPATH, "//button[contains(text(),'Checkout')]")
    item_name_loc = (By.XPATH, "div/h4/a")
    item_cart_loc = (By.XPATH, "div/button")

    def products(self):
        return self.driver.find_elements(*productsPage.products_loc)

    def checkout_link(self):
        return self.driver.find_element(*productsPage.checkout_link_loc)

    def checkout_button(self):
        self.driver.find_element(*productsPage.checkout_button_loc).click()
        return checkoutPage(self.driver)
