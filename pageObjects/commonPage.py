import string
import time
import random

class CommonPage:
    total_session_xpath = "//span[text()='Total']//following-sibling::span"
    running_session_xpath = "//span[text()='Running']//following-sibling::span"
    pending_session_xpath = "//span[text()='Pending']//following-sibling::span"
    dashboard_xpath = "//span[text()='Dashboard']"
    session_xpath = "//span[text()='Sessions']"
    history_session_xpath = "//span[text()='History-Sessions']"
    webdriver_url_xpath = "//div[@class='webdriver_url']//following-sibling::span"
    webdriver_url_copyButton_xpath = "//div[@class='webdriver_url_btn']"
    icon_onOrganisation_xpath = "(//a//img)[1]"
    platform_name_xpath = "//span[text()='Cloudify']"
    profile_icon_onOrg_xpath = "(//button[@type='button'])[1]"
    logout_onOrg_xpath = "//li[@tabindex='0']"
    profile_xpath = "(//button[@tabindex='0'])[1]"
    logout_xpath = "(//li[@tabindex='-1'])[4]"
    profile_username_xpath = "//li[@tabindex='0']"
    vieworg_xpath = "(//li[@tabindex='-1'])[1]"
    manage_plans_xpath = "(//li[@tabindex='-1'])[2]"
    setting_xpath = "(//li[@tabindex='-1'])[3]"
    search_icon_xpath = "(//button[@tabindex='0'])[2]"
    view_column_xpath = "(//button[@tabindex='0'])[3]"
    saveVideo_inViewColumn_xpath = "//span[text()='Save Video']"
    saveLogs_inViewColumn_xpath = "//span[text()='Save Logs']"
    filter_table_xpath="(//button[@tabindex='0'])[4]"
    status_text_filtertable_xpath = "//label[text()='Status']"
    save_videoText_onFilterTable = "//label[text()='Save Video']"
    capabilities_xpath = "//span[text()='Capabilities']"
    browserVersionOnFilterTable_xpath = "//label[text()='Browser Version']"
    sessionIdOnViewcolumn_xpath = "//span[text()='Session ID']"
    sessionIdTextInColumn_xpath = "//div[text()='Session ID']"
    screenResolutionTextInFilterTable_xpath = "//label[text()='Screen Resolution']"
    saveLogsTextInFilterTable_xpath = "//label[text()='Save Logs']"
    resetTextInfilter_xpath = "//button[text()='RESET']"
    no_data_found_xpath = "//div[text()='no data found']"
    saveVideo_enable_onHistorySession_xpath = "(//div[text()='Save Video']//following-sibling::div)[2]"
    saveLogs_enable_onHistorySession_xpath = "(//div[text()='Save Logs']//following-sibling::div)[2]"
    increase_number_session_xpath = "(//p)[2]"


    def __init__(self, driver):         #constructor to initialise driver, so that we can invoke driver in object creation in testcases
        self.driver = driver                        #self.driver is class driver store local driver

    #action methods
    def checkTotalSesion(self):
        total_session = self.driver.find_element_by_xpath(self.total_session_xpath).is_displayed()
        time.sleep(1)
        return total_session

    def checkRunningSession(self):
        running_session = self.driver.find_element_by_xpath(self.running_session_xpath).is_displayed()
        time.sleep(1)
        return running_session

    def checkPendingSession(self):
        pending_session = self.driver.find_element_by_xpath(self.pending_session_xpath).is_displayed()
        time.sleep(1)
        return pending_session

    def clickDashboard(self):
        self.driver.find_element_by_xpath(self.dashboard_xpath).click()
        time.sleep(1)

    def checkSession(self):
        session_text = self.driver.find_element_by_xpath(self.session_xpath).is_displayed()
        time.sleep(1)
        return session_text

    def clickSession(self):
        self.driver.find_element_by_xpath(self.session_xpath).click()
        time.sleep(1)

    def checkHistorySession(self):
        history_session_text = self.driver.find_element_by_xpath(self.history_session_xpath).is_displayed()
        time.sleep(1)
        return history_session_text

    def clickHistorySession(self):
        self.driver.find_element_by_xpath(self.history_session_xpath).click()
        time.sleep(1)

    def Check_platformIcon(self):
        icon_pricingPage = self.driver.find_element_by_xpath(self.icon_onOrganisation_xpath).is_displayed()
        time.sleep(2)
        return icon_pricingPage

    def Check_platformName(self):
        heading_pricingPage = self.driver.find_element_by_xpath(self.platform_name_xpath).is_displayed()
        time.sleep(2)
        return heading_pricingPage

    def checkOrgProfileIcon(self):
        profile = self.driver.find_element_by_xpath(self.profile_icon_onOrg_xpath).display()
        time.sleep(2)
        return profile

    def checkOrgLogout(self):
        self.driver.find_element_by_xpath(self.profile_icon_onOrg_xpath).click()
        logout = self.driver.find_element_by_xpath(self.logout_onOrg_xpath).is_displayed()
        time.sleep(2)
        return logout

    def clickOrgLogout(self):
        self.driver.find_element_by_xpath(self.profile_icon_onOrg_xpath).click()
        self.driver.find_element_by_xpath(self.logout_onOrg_xpath).click()
        time.sleep(2)

    def checkProfile(self):
        profile = self.driver.find_element_by_xpath(self.profile_xpath).is_displayed()
        time.sleep(1)
        return profile
    def clickProfile(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()

    def checkUsername(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        time.sleep(1)
        username = self.driver.find_element_by_xpath(self.profile_username_xpath).is_displayed()
        return username

    def checkViewOrg(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        vieworg = self.driver.find_element_by_xpath(self.vieworg_xpath).is_displayed()
        time.sleep(1)
        return vieworg

    def clickViewOrg(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        self.driver.find_element_by_xpath(self.vieworg_xpath).click()
        time.sleep(1)

    def checkManagePlans(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        myPlans = self.driver.find_element_by_xpath(self.manage_plans_xpath).is_displayed()
        time.sleep(1)
        return myPlans

    def clickManagePlans(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        self.driver.find_element_by_xpath(self.manage_plans_xpath).click()

    def checkWebdriverUrl(self):
        webdriver_url = self.driver.find_element_by_xpath(self.webdriver_url_xpath).is_displayed()
        time.sleep(1)
        return webdriver_url

    def copyWebdriverUrl(self):
        copied_webdriver_url = self.driver.find_element_by_xpath(self.webdriver_url_copyButton_xpath).click()
        time.sleep(1)
        return copied_webdriver_url

    def clickSetting(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        self.driver.find_element_by_xpath(self.setting_xpath).click()
        time.sleep(1)

    def checkLogout(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        logout = self.driver.find_element_by_xpath(self.logout_xpath).is_displayed()
        time.sleep(1)
        return logout

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        self.driver.find_element_by_xpath(self.logout_xpath).click()
        time.sleep(1)

    def clickMyPlans(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        self.driver.find_element_by_xpath(self.manage_plans_xpath).click()
        time.sleep(2)

    def checkSetting(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
        setting = self.driver.find_element_by_xpath(self.setting_xpath).is_displayed()
        time.sleep(1)
        return setting

    def checkSearchIcon(self):
        search_icon = self.driver.find_element_by_xpath(self.search_icon_xpath).is_displayed()
        time.sleep(1)
        return search_icon

    def checkViewColumn(self):
        view_column = self.driver.find_element_by_xpath(self.view_column_xpath).is_displayed()
        time.sleep(1)
        return view_column

    def clickViewColumn(self):
        self.driver.find_element_by_xpath(self.view_column_xpath).click()
        time.sleep(1)

    def checkFilterTable(self):
        filter_table = self.driver.find_element_by_xpath(self.filter_table_xpath).is_displayed()
        time.sleep(1)
        return filter_table

    def clickFilterTable(self):
        self.driver.find_element_by_xpath(self.filter_table_xpath).click()

    def checkStatustextFilterTable(self):
        status = self.driver.find_element_by_xpath(self.status_text_filtertable_xpath).is_displayed()
        time.sleep(1)
        return status

    def checkSaveVideotextFilterTable(self):
        save_video = self.driver.find_element_by_xpath(self.save_videoText_onFilterTable).is_displayed()
        time.sleep(1)
        return save_video

    def clickCapabities(self):
        self.driver.find_element_by_xpath(self.capabilities_xpath).click()

    def random_generator_new_organisationname(size=4, chars=string.ascii_lowercase + string.digits):
        return 'vidya'+''.join(random.choice(chars) for x in range(size))

    def checkBrowserVersionOnHistorySession(self):
        time.sleep(1)
        self.driver.find_element_by_xpath(self.filter_table_xpath).click()
        time.sleep(1)
        browser_version = self.driver.find_element_by_xpath(self.browserVersionOnFilterTable_xpath).is_displayed()
        return browser_version

    def clickSessionId(self):
        time.sleep(1)
        if self.driver.find_element_by_xpath(self.sessionIdOnViewcolumn_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.sessionIdOnViewcolumn_xpath).click()

    def checkSessionIdTextInColumn(self):
        session_id = self.driver.find_element_by_xpath(self.sessionIdTextInColumn_xpath).is_displayed()
        time.sleep(1)
        return session_id

    def checkScreenResolutionInFilterTable(self):
        screen_resolution = self.driver.find_element_by_xpath(self.screenResolutionTextInFilterTable_xpath).is_displayed()
        time.sleep(1)
        return screen_resolution

    def checkSaveLogsInFilterTable(self):
        save_logs = self.driver.find_element_by_xpath(self.saveLogsTextInFilterTable_xpath).is_displayed()
        time.sleep(1)
        return save_logs

    def checkResetTextInFilterTable(self):
        reset = self.driver.find_element_by_xpath(self.resetTextInfilter_xpath).is_displayed()
        time.sleep(1)
        return reset

    def checkNoDataFoundText(self):
        data = self.driver.find_element_by_xpath(self.no_data_found_xpath).is_displayed()
        time.sleep(1)
        return data

    def clickSaveVideosAndLogsInViewColumn(self):
        self.driver.find_element_by_xpath(self.view_column_xpath).click()
        if self.driver.find_element_by_xpath(self.saveVideo_inViewColumn_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.saveVideo_inViewColumn_xpath).click()

        if self.driver.find_element_by_xpath(self.saveLogs_inViewColumn_xpath).is_selected():
            assert True
        else:
            self.driver.find_element_by_xpath(self.saveLogs_inViewColumn_xpath).click()
        time.sleep(2)

    def saveVideoEnable(self):
        enable = self.driver.find_element_by_xpath(self.saveVideo_enable_onHistorySession_xpath).is_displayed()
        time.sleep(2)
        return enable

    def saveLogsEnable(self):
        enable = self.driver.find_element_by_xpath(self.saveLogs_enable_onHistorySession_xpath).is_displayed()
        time.sleep(2)
        return enable

    def checkincreaseInSessionNumber(self):
        session_number = self.driver.find_element_by_xpath(self.increase_number_session_xpath)
        return session_number
