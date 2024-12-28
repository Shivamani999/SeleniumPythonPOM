import time

import pytest

from pageObjects.homePage import homePage
from testdata.homepageData import homepageData
from utilities.BaseClass import BaseClass


class Test_home(BaseClass):

    def test_home(self, multi):
        homepage = homePage(self.driver)

        homepage.name(multi["firstname"])
        homepage.email(multi["lastname"])
        homepage.password("123456")

        self.select(homepage.dropdown(), multi["gender"])
        homepage.submit()
        time.sleep(2)
        msg = homepage.successMsg()
        assert ("Success" in msg)
        homepage.relaod()

    @pytest.fixture(params=homepageData.user_creds)
    def multi(self, request):
        return request.param
