from selenium import webdriver
import time
class signup:
    #locators
    textbox_username_xpath = " (//input[@name='username'])[1]"
    name_xpath = "(//input[@name='requiredAttributes[name]'])[1]"
    email_xpath = "(//input[@name='requiredAttributes[email]'])[1]"
    textbox_password_xpath = " (//input[@name='password'])[1]"
    button_signup_xpath = "(//button[text()='Sign up'])[1]"
    signin_xpath = "// a[text() = 'Sign in']"
    otp_xpath = "//input[@id='verification_code']"
    confirm_button_xpath = "//button[text()='Confirm account']"
    error_msg_text = "//p[text()='An error was encountered with the requested page.']"

    # driver constructor capture driver from test case pass for the rest of the file
    def __init__(self, driver):
        self.driver = driver
    #action methods
    def signup(self, newUser, name, email, newPassword):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(newUser)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.name_xpath).send_keys(name)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(newPassword)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_signup_xpath).click()
        time.sleep(30)
        self.driver.find_element_by_xpath(self.confirm_button_xpath).click()
        time.sleep(2)


    def errorMsg(self):
        errormsg = self.driver.find_element_by_xpath(self.error_msg_text).is_displayed()
        time.sleep(1)
        return errormsg


    def signin(self):
        self.driver.find_element_by_xpath(self.signin_xpath).click()
        time.sleep(2)

