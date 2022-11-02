from selenium import webdriver
import time

class Create_org_page:
    #locators
    create_org_text_xpath = "//div[text()='Create Organisation']"
    enter_org_text_xpath = "//label[text()='Enter Organisation Name']//following-sibling::div//input"
    cloudifytests_xpath = "//p[text()='.cloudifytests.io']"
    button_create_xpath = "//button[text()='Create']"
    new_org_xpath = "//input[@id='mui-1']"
    profile_icon_xpath = "(//button[@type='button'])[1]"
    logout_button_xpath = "//li[@tabindex='0']"
    error_msg_text = "//p[text()='An error was encountered with the requested page.']"
    # driver constructor capture driver from test case pass for the rest of the file
    def __init__(self, driver):
        self.driver = driver
    #action methods
    def checkCreate_org_text(self):
        create_org_text = self.driver.find_element_by_xpath(self.create_org_text_xpath).is_displayed()
        return create_org_text

    def Create_org(self):
        create_org = self.driver.find_element_by_xpath(self.enter_org_text_xpath).is_displayed()
        return create_org

    def clickEnter_organisation_text(self, orgname):
        self.driver.find_element_by_xpath(self.enter_org_text_xpath).click()
        self.driver.find_element_by_xpath(self.enter_org_text_xpath).send_keys(orgname)

    # def New_orgname(self, orgname):
    #     self.driver.find_element_by_xpath(self.new_org_xpath).clear()
    #     self.driver.find_element_by_xpath(self.new_org_xpath).send_keys(orgname)

    def Cloudifytests(self):
        cloudify = self.driver.find_element_by_xpath(self.cloudifytests_xpath).is_displayed()
        return cloudify

    def Create_button(self):
        self.driver.find_element_by_xpath(self.button_create_xpath).click()

    def clickProfile(self):
        self.driver.find_element_by_xpath(self.profile_icon_xpath).click()
        time.sleep(2)

    def checkLogout(self):
        logout = self.driver.find_element_by_xpath(self.logout_button_xpath).is_displayed()
        time.sleep(2)
        return logout