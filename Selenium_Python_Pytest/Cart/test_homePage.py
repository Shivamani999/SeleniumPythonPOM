import time

import pytest

from pageObjects.homePage import homePage
from testdata.homepageData import homepageData
from utilities.BaseClass import BaseClass


class Test_home(BaseClass):

    def test_home(self, multi):
        logger = self.test_logging()

        homepage = homePage(self.driver)
        logger.info("Homepage appeared")
        homepage.name(multi["firstname"])
        homepage.email(multi["lastname"])
        homepage.password("123456")

        self.select(homepage.dropdown(), multi["gender"])
        homepage.submit()
        time.sleep(2)
        msg = homepage.successMsg()
        logger.info(msg)
        assert ("Success" in msg)
        logger.info("Assert Successfull")
        homepage.relaod()

    @pytest.fixture(params=homepageData.getTestData("Rahul"))
    def multi(self, request):
        return request.param
