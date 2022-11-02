import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Capabilities_Page:
    #locators
    capbilities_text_xpath = "//div[text()='Capabilities']"
    java_text_xpath = "//li[text()='Java']"
    python_text_xpath = "//li[text()='Python']"
    ruby_text_xpath = "//li[text()='Ruby']"
    curl_text_xpath = "//li[text()='Curl']"
    test_name_xpath = "//input[@id='standard-basic']"
    chrome_xpath = "//span[text()='Chrome']"
    firefox_xpath = "//span[text()='Firefox']"
    opera_xpath = "//span[text()='Opera']"
    edge_xpath = "//span[text()='Edge']"
    safari_xpath = "//span[text()='Safari']"
    selected_browser_xpath = "(//li[@class='selected_browser'])[1]"
    browser_version_xpath = "//label[text()='Browser Version']//following-sibling::div//div"
    screen_resolution_xpath = "(//li[@class='selected_browser'])[2]"
    selectedmanual_session_timeout = "//div//label[text()='Manual Session Timeout']//following-sibling::div//input"
    save_logs_capabilities_xpath = "//div[text()='Save Logs']//following-sibling::span//span"
    save_video_capabilities_xpath = "//div[text()='Save Video']//following-sibling::span//span"
    run_manually_xpath = "//div[text()='Run Manually']"
    browserver_xpath = "//div[@id='version-simple-select-standard']"
    selectVersion_xpath = "//li[text()='102.0']"


    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods
    def checkCapabilitiesText(self):
        capabilities = self.driver.find_element_by_xpath(self.capbilities_text_xpath).is_displayed()
        return capabilities

    def checkJava(self):
        java= self.driver.find_element_by_xpath(self.java_text_xpath).is_displayed()
        return java

    def checkPython(self):
        python = self.driver.find_element_by_xpath(self.python_text_xpath).is_displayed()
        return python

    def checkRuby(self):
        ruby = self.driver.find_element_by_xpath(self.ruby_text_xpath).is_displayed()
        return ruby

    def checkCurl(self):
        curl = self.driver.find_element_by_xpath(self.curl_text_xpath).is_displayed()
        return curl

    def setTestName(self, name):
        self.driver.find_element_by_xpath(self.test_name_xpath).send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        self.driver.find_element_by_xpath(self.test_name_xpath).send_keys(name)

    def clickBrowser(self):
        if self.driver.find_element_by_xpath(self.selected_browser_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.selected_browser_xpath).click()
        time.sleep(1)
    def selectedBrowser(self):
        selected_browser = self.driver.find_element_by_xpath(self.selected_browser_xpath)
        return selected_browser

    def clickVersion(self):
        self.driver.find_element_by_xpath(self.browserver_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.selectVersion_xpath).click()

    def selectedVersion(self):
        selected_version = self.driver.find_element_by_xpath(self.browser_version_xpath)
        return selected_version

    def clickScreenResolution(self):
        if self.driver.find_element_by_xpath(self.screen_resolution_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.screen_resolution_xpath).click()

    def selectedScreenResolution(self):
        selected_resolution = self.driver.find_element_by_xpath(self.screen_resolution_xpath)
        return selected_resolution

    def selectManualSessionTimeout(self, manualsessiontime):
        manual_session_timeout = self.driver.find_element_by_xpath(self.selectedmanual_session_timeout)
        manual_session_timeout.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        manual_session_timeout.send_keys(manualsessiontime)
        time.sleep(1)

    def selectedTimeout(self):
        selected_timeout = self.driver.find_element_by_xpath(self.selectedmanual_session_timeout)
        return selected_timeout

    def clickSaveLogs(self):
        if self.driver.find_element_by_xpath(self.save_logs_capabilities_xpath).is_selected():
            assert True
            print("Save Logs Already Selected")
        else:
            self.driver.find_element_by_xpath(self.save_logs_capabilities_xpath).click()

    def clickSaveVideos(self):
        if self.driver.find_element_by_xpath(self.save_video_capabilities_xpath).is_selected():
            assert True
            print("Save Videos Already Selected")
        else:
            self.driver.find_element_by_xpath(self.save_video_capabilities_xpath).click()

    def clickRunManually(self):
        self.driver.find_element_by_xpath(self.run_manually_xpath).click()
        time.sleep(13)

    def selectedLogs(self):
        selected_timeout = self.driver.find_element_by_xpath(self.save_logs_capabilities_xpath)
        return selected_timeout

    def selectedVideos(self):
        selected_timeout = self.driver.find_element_by_xpath(self.save_video_capabilities_xpath)
        return selected_timeout