import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkoutPage import checkoutPage
from pageObjects.homePage import homePage
from pageObjects.productsPage import productsPage
from utilities.BaseClass import BaseClass


class Test_Cart(BaseClass):

    def test_prod(self):

        hmpage = homePage(self.driver)

        prPage = hmpage.shop_link()
        item_names = prPage.products()
        for item in item_names:
            if item.find_element(*prPage.item_name_loc).text.__contains__("iphone"):
                item.find_element(*prPage.item_cart_loc).click()
                break

        prPage.checkout_link().click()

        chkoutPage = prPage.checkout_button()
        chkoutPage.country().send_keys("ind")
        self.exp_wait(self.driver, chkoutPage.india_loc)
        chkoutPage.india().click()
        time.sleep(2)
        chkoutPage.checkbox().click()
        chkoutPage.purchase().click()
        message = chkoutPage.success_msg().text
        assert message.__contains__("Success#")
