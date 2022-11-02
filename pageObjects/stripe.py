import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Stripe_Page:
    #locators
    # price_xpath = "(//span[text()='Subscribe to org_cfg']//following-sibling::div//span)[2]"
    change_option_xpath = "//div[text()='Change']"
    cardnumber_xpath = "//input[@name='cardNumber']"
    cardexpiry_xpath = "//input[@name='cardExpiry']"
    cardcvc_xpath = "//input[@name='cardCvc']"
    nameoncard_xpath = "//input[@id='billingName']"
    billingadd1_xpath = "//input[@id='billingAddressLine1']"
    subscription_xpath = "//button[@type='submit']"

    # session_xpath = "//span[text()='Sessions']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods
    def clickOnChange(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.change_option_xpath).click()

    def fillCardNumber(self, cardnumber):
        time.sleep(3)
        cardno = self.driver.find_element_by_xpath(self.cardnumber_xpath)
        cardno.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        cardno.send_keys(cardnumber)

    def fillCardExpiry(self, cardexpiry):
        time.sleep(3)
        cardexp = self.driver.find_element_by_xpath(self.cardexpiry_xpath)
        cardexp.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        cardexp.send_keys(cardexpiry)

    def fillCardCvc(self, cardcvc):
        time.sleep(3)
        card_cvc = self.driver.find_element_by_xpath(self.cardcvc_xpath)
        card_cvc.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        card_cvc.send_keys(cardcvc)

    def fillCardName(self, cardname):
        time.sleep(3)
        card_name = self.driver.find_element_by_xpath(self.nameoncard_xpath)
        card_name.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        card_name.send_keys(cardname)

    def fillBillingAddress(self, address):
        time.sleep(3)
        billing_add = self.driver.find_element_by_xpath(self.billingadd1_xpath)
        billing_add.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        billing_add.send_keys(address)

    def clickOnSubscriptionButton(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.subscription_xpath).click()
        time.sleep(18)