import time

from selenium import webdriver

class History_Session:
    #locators
    test_name_xpath = "(//div[text()='Test Name']//following-sibling::div//span)[2]"              #find ele usrnm by xpath
    status_timeout_xpath = "(//div[text()='Status']//following-sibling::div)[2]"              #find ele pswrd by xpath
    duration_xpath = "(//div[text()='Duration']//following-sibling::div)[2]"
    createdAt_xpath = "(//div[text()='Created At']//following-sibling::div)[2]"
    menu_xpath = "(//button[@id='long-button'])[1]"
    viewVideo_xpath = "//li[text()='View Video...']"
    row_perPage_xpath = "//p[text()='Rows per page:']"
    browser_viewcolumn_xpath = "//span[text()='Browser']"
    browser_version_on_history_xpath = "//div[text()='Browser']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods
    def checkTestName(self):
        test = self.driver.find_element_by_xpath(self.test_name_xpath).is_displayed()
        time.sleep(2)
        return test

    def checkStatus(self):
        status = self.driver.find_element_by_xpath(self.status_timeout_xpath).is_displayed()
        time.sleep(2)
        return status

    def checkDuration(self):
        duration = self.driver.find_element_by_xpath(self.duration_xpath).is_displayed()
        time.sleep(2)
        return duration

    def checkCreatedAt(self):
        createdat = self.driver.find_element_by_xpath(self.createdAt_xpath).is_displayed()
        time.sleep(2)
        return createdat

    def clickViewVideo(self):
        self.driver.find_element_by_xpath(self.menu_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.viewVideo_xpath).click()

    def selectBrowserInsideViewColumn(self):
        if self.driver.find_element_by_xpath(self.browser_viewcolumn_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.browser_viewcolumn_xpath).click()

    def deselectBrowserInsideViewColumn(self):
        # if self.driver.find_element_by_xpath(self.browser_viewcolumn_xpath).is_selected():
        self.driver.find_element_by_xpath(self.browser_viewcolumn_xpath).click()
        # else:
        #     assert True
        time.sleep(3)

    def checkBrowserColumnOnHistorySessionPage(self):
        assert self.driver.find_element_by_xpath(self.browser_version_on_history_xpath).is_displayed() == False

