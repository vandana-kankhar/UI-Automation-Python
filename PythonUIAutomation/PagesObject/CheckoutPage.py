from selenium.webdriver.common.by import By

#products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    Products = (By.XPATH,"//div[@class='card h-100']")

    def get_products(self):
        return self.driver.find_element(CheckoutPage.Products)