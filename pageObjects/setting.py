import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Setting_Page:
    #locators
    chrome_xpath = "//span[text()='Chrome']"              #find ele usrnm by xpath
    firefox_xpath = "//span[text()='Firefox']"              #find ele pswrd by xpath
    opera_xpath = "//span[text()='Opera']"
    edge_xpath = "//span[text()='Edge']"
    safari_xpath = "//span[text()='Safari']"
    browserver_xpath = "//div[@id='version-simple-select-standard']"
    selectVersion_xpath = "//li[text()='102.0']"
    manualSession_timeout_xpath = "//input[@type='number']"
    session_timeout_xpath = "//input[@name='session_timeout']"
    screen_resolution_xpath = "//div[text()='Screen Resolutions']"
    click_1980x1080_xpath = "//li[text()='1920x1080']"
    save_logs_xpath = "//input[@name='save_logs']"
    save_videos_xpath = "//input[@name='save_videos']"
    save_button_xpath = "//button[text()='SAVE']"
    automation_token_xpath = "//label[text()='Automation Token']//following-sibling::div//input"
    regenerate_xpath = "//div[text()='Regenerate']"
    variables_changed_xpath = "//div[text()='variables changed']"

    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver
        time.sleep(8)

    #action methods
    def checkChrome(self):
        chrome = self.driver.find_element_by_xpath(self.chrome_xpath).is_displayed()
        time.sleep(1)
        return chrome

    def checkFirefox(self):
        firefox = self.driver.find_element_by_xpath(self.firefox_xpath).is_displayed()
        time.sleep(1)
        return firefox

    def checkOpera(self):
        opera = self.driver.find_element_by_xpath(self.opera_xpath).is_displayed()
        time.sleep(1)
        return opera

    def checkEdge(self):
        edge = self.driver.find_element_by_xpath(self.edge_xpath).is_displayed()
        time.sleep(1)
        return edge

    def checkSafari(self):
        safari = self.driver.find_element_by_xpath(self.safari_xpath).is_displayed()
        time.sleep(1)
        return safari

    def selectChrome(self):
        self.driver.find_element_by_xpath(self.chrome_xpath).click()
        time.sleep(1)

    def selectBrowserVersion(self):
        self.driver.find_element_by_xpath(self.browserver_xpath).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.selectVersion_xpath).click()

    def selectManualSessionTimeout(self, manualsessiontime):
        manual_session_timeout = self.driver.find_element_by_xpath(self.manualSession_timeout_xpath)
        manual_session_timeout.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        manual_session_timeout.send_keys(manualsessiontime)
        time.sleep(1)

    def selectSessionTimeout(self, sessiontime):
        session_timeout = self.driver.find_element_by_xpath(self.session_timeout_xpath)
        session_timeout.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        session_timeout.send_keys(sessiontime)
        time.sleep(1)

    def checkScreen_resolution(self):
        resolution = self.driver.find_element_by_xpath(self.screen_resolution_xpath).is_displayed()
        time.sleep(1)
        return resolution

    def clickScreen_resolution(self):
        self.driver.find_element_by_xpath(self.click_1980x1080_xpath).click()
        time.sleep(1)

    def clickSaveLogs(self):
        if self.driver.find_element_by_xpath(self.save_logs_xpath).is_selected():
            assert True
            print("Save Logs Already Selected")
        else:
            self.driver.find_element_by_xpath(self.save_logs_xpath).click()
            logs = self.driver.find_element_by_xpath(self.save_logs_xpath)
    def clickSaveVideos(self):
        if self.driver.find_element_by_xpath(self.save_videos_xpath).is_selected():
            assert True
            print("Save Videos Already Selected")
        else:
            self.driver.find_element_by_xpath(self.save_videos_xpath).click()

    def checkAutomationToken(self):
        token = self.driver.find_element_by_xpath(self.automation_token_xpath).get_attribute("value")
        time.sleep(1)
        print("token:", token)
        return token


    def checkAutomationToken2(self):
        token2 = self.driver.find_element_by_xpath(self.automation_token_xpath).get_attribute("value")
        time.sleep(1)
        print("token changed:", token2)
        return token2

    def checkSave_button(self):
        time.sleep(1)
        save = self.driver.find_element_by_xpath(self.save_button_xpath).is_displayed()
        return save

    def clickSave_button(self):
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        time.sleep(1)

    def checkVariablesChanged(self):
        changed = self.driver.find_element_by_xpath(self.variables_changed_xpath).is_displayed()
        time.sleep(1)
        return changed

    def clickRegenate_button(self):
        self.driver.find_element_by_xpath(self.regenerate_xpath).click()
        time.sleep(1)


