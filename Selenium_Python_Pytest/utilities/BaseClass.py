import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.homePage import homePage

@pytest.mark.usefixtures("setup")
class BaseClass:

    def select(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def exp_wait(self, driver, locator):
        wait = WebDriverWait(driver, 15)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def test_logging(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        logger.debug("A Debug statement")
        logger.info("A Info logger")
        # logger.warning("A warning logger")
        # logger.error("A error logger")
        # logger.critical("A critical error logger")
        return logger

