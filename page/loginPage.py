from LearnSelenium.page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    """description of class"""
    # page element identifier
    usename = (By.ID, 'useraccount')
    password = (By.ID, 'password')
    okButton = (By.XPATH, '//*[@id="formlogin"]/p[4]/button')

    # Get username textbox and input username
    def set_username(self, username):
        name = self.driver.find_element(*LoginPage.usename)
        name.send_keys(username)

        # Get password textbox and input password, then hit return

    def set_password(self, password):
        pwd = self.driver.find_element(*LoginPage.password)
        pwd.send_keys(password + Keys.RETURN)

        # Get pop up dialog title

    def get_DiaglogTitle(self):
        digTitle = self.driver.find_element(*LoginPage.dialogTitle)
        return digTitle.text

        # Get "cancel" button and then click

    def click_cancel(self):
        cancelbtn = self.driver.find_element(*LoginPage.cancelButton)
        cancelbtn.click()

        # click Sign in

    def click_SignIn(self):
        okbtn = self.driver.find_element(*LoginPage.okButton)
        okbtn.click()