from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest


from PagesObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_One(BaseClass):


    def test_e2e(self):

        log = self.get_Logger()
        home = HomePage(self.driver)
        time.sleep(3)
        home.shopItem().click()
        time.sleep(3)
        log.info("Getting all cards info")
        time.sleep(3)
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        time.sleep(3)
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text

            if productName == "Blackberry":
                # Add item into cart

                product.find_element_by_xpath("div/button").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        time.sleep(3)
        self.driver.find_element_by_id("country").send_keys("ind")
        time.sleep(3)
        self.verifylinkPresence("India")
        time.sleep(3)
        self.driver.find_element_by_link_text("India").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(3)
        successText = self.driver.find_element_by_class_name("alert-success").text
        time.sleep(3)

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")




