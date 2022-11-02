import time
from selenium import webdriver

class ManagePlan:
    #locators
    plan_text_xpath = "/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/div[text()='Parallel Sessions']"
    upgrate_plan_button_xpath = "//button[text()='Upgrate Plan']"
    parallel_session_text_xpath = "//div[text()='Parallel Sessions']"
    totalNoOfSession_number_xpath = "(//div[@class='large_box'])[2]//div//div"
    totalNoOfSession_text_xpath = "//div[text()='Total No. of Sessions']"
    retention_period_xpath = "//div[text()='Retention Period']"
    retentionPeriod_epiryDate_xpath = "(//div[@class='large_box'])[3]//div//div"
    retentionPeriod_epiryDateText_xpath = "(//div[text()='Expiry Date'])[1]"
    plan_duration_xpath = "//div[text()='Plan Duration']"
    planDuration_expiryDate_xpath = "(//div[@class='large_box'])[4]//div//div"
    planDuration_expiryDateText_xpath = "(//div[text()='Expiry Date'])[2]"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
    #action methods
    def checkPlanText(self):
        plan_text = self.driver.find_element_by_xpath(self.plan_text_xpath).is_displayed()
        time.sleep(3)
        return plan_text

    def checkUpgratePlanButton(self):
        upgrate_plan = self.driver.find_element_by_xpath(self.upgrate_plan_button_xpath).is_displayed()
        time.sleep(3)
        return upgrate_plan

    def checkParallelSessionText(self):
        parallel_session = self.driver.find_element_by_xpath(self.parallel_session_text_xpath).is_displayed()
        time.sleep(3)
        return parallel_session

    def checkTotalNumberSessionNo(self):
        total_session_no = self.driver.find_element_by_xpath(self.totalNoOfSession_number_xpath).text
        time.sleep(3)
        return total_session_no

    def checkTotalNoSessionText(self):
        total_session_text = self.driver.find_element_by_xpath(self.totalNoOfSession_text_xpath).is_displayed()
        time.sleep(3)
        return total_session_text

    def retentionPeriodText(self):
        time.sleep(5)
        retention_period_text = self.driver.find_element_by_xpath(self.retention_period_xpath).is_displayed()
        return retention_period_text

    def checkRetentionPeriodExpiryNo(self):
        time.sleep(5)
        retention_expiry_no = self.driver.find_element_by_xpath(self.retentionPeriod_epiryDate_xpath).text

        return retention_expiry_no

    def retentionPeriodExpiryText(self):
        retention_period_expiry_text = self.driver.find_element_by_xpath(self.retentionPeriod_epiryDateText_xpath).is_displayed()
        time.sleep(3)
        return retention_period_expiry_text

    def checkPlanDurationText(self):
        plan_duration_text = self.driver.find_element_by_xpath(self.plan_duration_xpath).is_displayed()
        time.sleep(3)
        return plan_duration_text

    def checkPlanDurationExpiryNo(self):
        plan_duration_expiry_no = self.driver.find_element_by_xpath(self.planDuration_expiryDate_xpath).text
        time.sleep(3)
        return plan_duration_expiry_no

    def checkPlanDurationExpiryText(self):
        plan_duration_expiry_text = self.driver.find_element_by_xpath(self.planDuration_expiryDateText_xpath).is_displayed()
        time.sleep(3)
        return plan_duration_expiry_text

