from selenium.webdriver.common.by import By


class checkoutPage:

    def __init__(self, driver):
        self.driver = driver

    country_loc = (By.ID, "country")
    india_loc = (By.XPATH, "//a[text()='India']")
    checkbox_loc = (By.XPATH, "//label[@for='checkbox2']")
    purchase_loc = (By.XPATH, "//input[@value='Purchase']")
    success_loc = (By.XPATH, "//strong[text()='Success!']")

    def country(self):
        return self.driver.find_element(*checkoutPage.country_loc)

    def india(self):
        return self.driver.find_element(*checkoutPage.india_loc)

    def checkbox(self):
        return self.driver.find_element(*checkoutPage.checkbox_loc)

    def purchase(self):
        return self.driver.find_element(*checkoutPage.purchase_loc)

    def success_msg(self):
        return self.driver.find_element(*checkoutPage.success_loc)