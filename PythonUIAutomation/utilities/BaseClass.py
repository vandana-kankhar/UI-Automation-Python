import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def get_Logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        formater = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # formater = logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        filehandler.setFormatter(formater)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        logger.debug("a debug statements is executed")
        logger.info("Information statements")
        logger.debug("a debug statements is executed")
        logger.warning("something is in warning mode")
        logger.error("A major error has happened")
        logger.critical("critical issue")
        return logger

    def verifylinkPresence(self,text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionsbyText(self,locater,text):
        dropdown = Select(locater)
        dropdown.select_by_visible_text(text)





