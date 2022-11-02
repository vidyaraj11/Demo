import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class organisationList:
    #locators

    organisation_text_xpath = "//div[text()='Organisations']"
    name_text_xpath = "//span[text()='Name']"
    create_button_xpath = "//button[text()='CREATE']"
    button_explore_cloudify_xpath = "(//span[text()='vidya-cloudify8']//following-sibling::div//button)[2]"
    button_info_cloudify_xpath = "(//span[text()='vidya-cloudify8']//following-sibling::div//button)[1]"
    pricing_text_xpath = "//div[text()='Pricing']"
    session_xpath = "//span[text()='Sessions']"
    profile_xpath = "(//button[@tabindex='0'])[1]"
    vieworg_xpath = "(//li[@tabindex='-1'])[1]"


    # driver constructor capture driver from test case pass for the rest of the file
    def __init__(self, driver):
        self.driver = driver
    #action methods

    def checkOrganisation_text(self):
        text = self.driver.find_element_by_xpath(self.organisation_text_xpath).is_displayed()
        time.sleep(2)
        return text

    def enter_organisation_text(self):
        text1 = self.driver.find_element_by_xpath(self.organisation_text_xpath).is_displayed()
        time.sleep(2)
        return text1

    def name_text(self):
        name = self.driver.find_element_by_xpath(self.name_text_xpath).is_displayed()
        time.sleep(2)
        return name

    def clickOnCreate(self):
        self.driver.find_element_by_xpath(self.create_button_xpath).click()
        time.sleep(2)

    def info_button(self):
        info = self.driver.find_element_by_xpath(self.button_info_cloudify_xpath).is_displayed()
        time.sleep(2)
        return info

    def explore_button(self):
        explore = self.driver.find_element_by_xpath(self.button_explore_cloudify_xpath).is_displayed()
        time.sleep(2)
        return explore

    def clickExplore(self):
        self.driver.find_element_by_xpath(self.button_explore_cloudify_xpath).click()
        time.sleep(2)

    def ExploreAll(self):
        organisation_list = ["vidya-cloudify8", "vidya-testing2"]

        for x in organisation_list:
            # (//button[text()='Explore'])[1]
            xpath = "(//span[text()='"+x+"']//following-sibling::div//button)[2]"
            self.driver.find_element(By.XPATH, xpath).click()
            time.sleep(2)
            try:
                if self.driver.find_element_by_xpath(self.pricing_text_xpath).text == "Pricing":
                    print(x, "Pricing")
                    time.sleep(3)
                    self.driver.back()
                    time.sleep(3)
            except:
                if self.driver.find_element_by_xpath(self.session_xpath).text == "Sessions":
                    time.sleep(2)
                    print(x, "Routed on Session page:")
                    self.driver.find_element_by_xpath(self.profile_xpath).click()
                    self.driver.find_element_by_xpath(self.vieworg_xpath).click()
                    time.sleep(2)


