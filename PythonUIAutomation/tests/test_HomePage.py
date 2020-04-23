from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PagesObject.HomePage import HomePage
from tests.Home_PageData import Home_PageData
from utilities.BaseClass import BaseClass


class Test_HomePage(BaseClass):

    def test_formsubmission(self,getData):
        log = self.get_Logger()
        homepage = HomePage(self.driver)
        sleep(4)
        homepage.getName().send_keys(getData["firstname"])
        #sleep(4)
        homepage.get_email().send_keys(getData["lastname"])
        #sleep(4)
        homepage.get_examplecheck().click()
        #sleep(4)
        log.info("Enter gender")
        self.selectoptionsbyText(homepage.checkbox(),getData["gender"])
        #sleep(4)
        homepage.submit_form().click()

        message = homepage.alert_message().text

        assert ("Sueeeeeeeeeeeeeccess" in message)
        self.driver.refresh()

    # dropdown = Select(homepage.checkbox())
    # dropdown.select_by_visible_text("Female")
    @pytest.fixture(params=Home_PageData.test_Home_Page_Data)
    def getData(self,request):
        return request.param

