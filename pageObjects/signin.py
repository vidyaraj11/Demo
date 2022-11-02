import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    #locators
    textbox_username_xpath = "(//input[@id='signInFormUsername'])[2]"
    username_text_xpath = "(//label[text()='Username'])[2]"
    textbox_password_xpath = "(//input[@id='signInFormPassword'])[2]"
    password_text_xpath = "(//label[text()='Password'])[2]"
    button_signin_xpath = "(//input[@name='signInSubmitButton'])[2]"
    signup_xpath = "(//span[text()='Need an account?']//following-sibling::a)[2]"
    forgot_password_xpath = "(//a[text()='Forgot your password?'])[2]"
    signin_as_differentUser_xpath = "(//a[text()='Sign in as a different user?'])[2]"
    invalid_msg_xpath = "(//p[text()='Incorrect username or password.'])[2]"
    site_cannot_reach_xpath = "//button[text()='Reload']"
    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(4)
    #action methods

    def setLogin(self, username, password):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()             #self in find element bcz vars are rltd to class
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)             #self in find element bcz vars are rltd to class
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()
        time.sleep(4)

    def signinAsDifferentUser(self):
        self.driver.find_element_by_xpath(self.signin_as_differentUser_xpath).click()
        time.sleep(2)

    def checksigninAsDifferentUserText(self):
        diffuser = self.driver.find_element_by_xpath(self.signin_as_differentUser_xpath).is_displayed()
        time.sleep(1)
        return diffuser

    def checkInvalidMsgText(self):
        msg = self.driver.find_element_by_xpath(self.invalid_msg_xpath).is_displayed()
        time.sleep(3)
        return msg

    def checkUsernameText(self):
        user = self.driver.find_element_by_xpath(self.textbox_username_xpath).is_displayed()
        time.sleep(1)
        print("username")
        return user

    def checkPasswordText(self):
        password = self.driver.find_element_by_xpath(self.textbox_password_xpath).is_displayed()
        time.sleep(1)
        print("password is present")
        return password

    def checkForgotPasswordText(self):
        forgotpassword = self.driver.find_element_by_xpath(self.forgot_password_xpath).is_displayed()
        time.sleep(1)
        return forgotpassword

    def checkSigninButton(self):
        signin = self.driver.find_element_by_xpath(self.button_signin_xpath).is_displayed()
        time.sleep(1)
        return signin

    def checkSignupLinkOnSignin(self):
        signup = self.driver.find_element_by_xpath(self.signup_xpath).is_displayed()
        time.sleep(1)
        print("signup is present")
        return signup

    def checkWrongSigninUrl(self):
        msg = self.driver.find_element_by_xpath(self.site_cannot_reach_xpath).is_displayed()
        return msg







