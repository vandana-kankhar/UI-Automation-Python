from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR,"input[name='name']")
    email = (By.NAME,"email")
    examplecheck1 = (By.ID,"exampleCheck1")
    checkbox_sel = (By.ID,"exampleFormControlSelect1")
    submit = (By.XPATH,"//input[@type='submit']")
    alert = (By.CLASS_NAME,"alert-success")


    def alert_message(self):
        return self.driver.find_element(*HomePage.alert)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def checkbox(self):
        return self.driver.find_element(*HomePage.checkbox_sel)

    def get_examplecheck(self):
        return self.driver.find_element(*HomePage.examplecheck1)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)


