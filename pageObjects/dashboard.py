import time

from selenium import webdriver

class Dashboard:
    #locators
    totalNo_session_xpath = "(//span[text()='Total']//following-sibling::span)[2]"              #find ele usrnm by xpath
    totalNo_running_xpath = "(//span[text()='Running']//following-sibling::span)[2]"              #find ele pswrd by xpath
    total_pendingSession_xpath = "(//span[text()='Pending']//following-sibling::span)[2]"
    charts_text_xpath = "//span[text()='Charts']"
    start_date_xpath = "(//div//input)[1]"
    start_date_text_xpath = "//label[text()='Start Date']"
    end_date_xpath = "(//div//input)[2]"
    end_date_text_xpath = "//label[text()='End Date']"
    save_button_xpath = "//button[text()='SAVE']"
    recent_activity_text_xpath = "//div[text()='Recent Activities']"
    viewAll_xpath = "//div[text()='View all']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods
    def TotalNoOfSessions(self):
        totalsessions = self.driver.find_element_by_xpath(self.totalNo_session_xpath).get_attribute()
        time.sleep(1)
        return totalsessions

    def RunningSessions(self):
        runningsessions = self.driver.find_element_by_xpath(self.totalNo_running_xpath).get_attribute()
        time.sleep(1)
        return runningsessions

    def PendingSessions(self):
        pendingsessions = self.driver.find_element_by_xpath(self.total_pendingSession_xpath).get_attribute()
        time.sleep(1)
        return pendingsessions

    def checkChartsText(self):
        charts = self.driver.find_element_by_xpath(self.charts_text_xpath).is_displayed()
        time.sleep(1)
        return charts

    def setStartDate(self, date1):
        self.driver.find_element_by_xpath(self.start_date_xpath).send_keys(date1)
        time.sleep(1)

    def checkStartDate(self):
        start_date = self.driver.find_element_by_xpath(self.start_date_text_xpath).is_displayed()
        time.sleep(1)
        return start_date

    def setEndDate(self, date2):
        self.driver.find_element_by_xpath(self.end_date_xpath).send_keys(date2)
        time.sleep(1)

    def checkEndDate(self):
        end_date = self.driver.find_element_by_xpath(self.end_date_text_xpath).is_displayed()
        time.sleep(1)
        return end_date

    def checkSaveButton(self):
        save = self.driver.find_element_by_xpath(self.save_button_xpath).is_displayed()
        time.sleep(1)
        return save

    def clickSave(self, date2):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        time.sleep(1)

    def checkRecentActivityText(self):
        recentactivity = self.driver.find_element_by_xpath(self.recent_activity_text_xpath).is_displayed()
        time.sleep(1)
        return recentactivity

    def checkViewAll(self):
        viewAll = self.driver.find_element_by_xpath(self.viewAll_xpath).is_displayed()
        time.sleep(1)
        return viewAll

    def clickViewAll(self):
        self.driver.find_element_by_xpath(self.viewAll_xpath).click()