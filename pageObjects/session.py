import time

from selenium import webdriver

class session:
    #locators
    row_perPage_xpath = "//p[text()='Rows per page:']"
    browserver_xpath = "(//button[@tabindex='0'])[5]"
    testname_xpath = "(//button[@tabindex='0'])[6]"
    status_xpath = "(//button[@tabindex='0'])[7]"
    duration_xpath = "(//button[@tabindex='0'])[8]"
    createdat_xpath = "(//div[text()='Created At']//following-sibling::div)[2]"
    menu_button_xpath = "(//button[@id='long-button'])[1]"
    viewVNC_xpath = "//a[text()='View VNC']"
    session_testName_xpath = "(//div[text()='Test Name']//following-sibling::div)[2]"
    session_menu = "//button[@id='long-button']"
    terminate_xpath = "//li[text()='Terminate']"
    click_yes_xpath = "//button[text()='Yes']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver

    #action methods

    def checkRowPerPage(self):
        row_per_page = self.driver.find_element_by_xpath(self.row_perPage_xpath).is_displayed()
        time.sleep(1)
        return row_per_page

    def checkBrowserVersion(self):
        browser = self.driver.find_element_by_xpath(self.browserver_xpath).is_displayed()
        time.sleep(1)
        return browser

    def clickTestName(self):
        test = self.driver.find_element_by_xpath(self.testname_xpath).is_displayed()
        time.sleep(1)
        return test

    def checkStatus(self):
        status = self.driver.find_element_by_xpath(self.status_xpath).is_displayed()
        time.sleep(1)
        return status

    def checkDuration(self):
        duration = self.driver.find_element_by_xpath(self.duration_xpath).is_displayed()
        time.sleep(1)
        return duration

    def checkCreatedat(self):
        created = self.driver.find_element_by_xpath(self.createdat_xpath).is_displayed()
        time.sleep(1)
        return created

    def click_on_session_Terminate(self):
        self.driver.find_element_by_xpath(self.session_menu).click()
        self.driver.find_element_by_xpath(self.terminate_xpath).click()
        self.driver.find_element_by_xpath(self.click_yes_xpath).click()
        time.sleep(3)

