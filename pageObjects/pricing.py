import time

from selenium import webdriver


class PricingPage:
    #locators

    pricing_text_xpath = "//div[text()='Pricing']"
    org_name_xpath = "//div[@class='org_name']"
    parallelSession_text_xpath = "//div[text()='Parallel Sessions']"
    total_parallelSession_xpath = "//div[text()='Total Parallel Sessions']"
    total_parallelSession_info_xpath = "(//div[text()='Total Parallel Sessions']//following-sibling::button)"
    retention_period_xpath = "//div[text()='Retention period']"
    retention_period_icon_xpath = "(//div[text()='Retention period']//following-sibling::button)"
    plan_period_xpath = "//div[text()='Plan period']"
    free_session_xpath = "//div[text()='Free Sessions:']"
    freeSession_checkbox_xpath = "(//div[text()='Free Sessions:']//following-sibling::div//input)"
    totalPrice_xpath = "//div[text()='Total Price:']"
    totalPrice_textbox_xpath = "(//div[text()='Total Price:']//following-sibling::div)"
    confirm_button_xpath = "//button[text()='Confirm']"
    input_parallel_session_xpath = "//input[@type='text']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods

    def Check_pricing_text(self):
        pricing_text = self.driver.find_element_by_xpath(self.pricing_text_xpath).is_displayed()
        time.sleep(1)
        return pricing_text

    def Check_orgName_text(self):
        org_name = self.driver.find_element_by_xpath(self.org_name_xpath).is_displayed()
        time.sleep(1)
        return org_name

    def CheckParallelSession_text(self):
        parallelsession_text = self.driver.find_element_by_xpath(self.parallelSession_text_xpath).is_displayed()
        time.sleep(1)
        return parallelsession_text

    def CheckTotalParallelSession_text(self):
        total_parallelsession_text = self.driver.find_element_by_xpath(self.total_parallelSession_xpath).is_displayed()
        time.sleep(1)
        return total_parallelsession_text

    def TotalParallelSession_info(self):
        total_parallelsession_info = self.driver.find_element_by_xpath(self.total_parallelSession_info_xpath).is_displayed()
        time.sleep(1)
        return total_parallelsession_info

    def CheckRetentionPeriod_text(self):
        retentionperiod_text = self.driver.find_element_by_xpath(self.retention_period_xpath).is_displayed()
        time.sleep(1)
        return retentionperiod_text

    def CheckRetentionPeriod_info(self):
        retentionperiod_info = self.driver.find_element_by_xpath(self.retention_period_icon_xpath).is_displayed()
        time.sleep(1)
        return retentionperiod_info

    def CheckPlanPeriod_text(self):
        retentionperiod_text = self.driver.find_element_by_xpath(self.plan_period_xpath).is_displayed()
        time.sleep(1)
        return retentionperiod_text

    def CheckFreeSessions_text(self):
        freesession_text = self.driver.find_element_by_xpath(self.free_session_xpath).is_displayed()
        time.sleep(1)
        return freesession_text

    def FreeSession_checkbox(self):
        self.driver.find_element_by_xpath(self.freeSession_checkbox_xpath).click()
        time.sleep(2)

    def TotalPrice_text(self):
        totalprice_text = self.driver.find_element_by_xpath(self.totalPrice_xpath).is_displayed()
        time.sleep(1)
        return totalprice_text

    def TotalPrice(self):
        totalprice = self.driver.find_element_by_xpath(self.totalPrice_textbox_xpath).is_displayed()
        time.sleep(1)
        # print(totalprice)
        return totalprice

    def check_Confirm_button(self):
        confirm_button = self.driver.find_element_by_xpath(self.confirm_button_xpath).is_displayed()
        time.sleep(2)
        return confirm_button

    def Confirm_button(self):
        self.driver.find_element_by_xpath(self.confirm_button_xpath).click()
        time.sleep(10)

    def inputParallelSession(self, sessionNumber):
        self.driver.find_element_by_xpath(self.input_parallel_session_xpath).send_keys(sessionNumber)
        time.sleep(1)

