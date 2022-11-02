import pytest
from selenium import webdriver

from pageObjects.dashboard import Dashboard
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.historySession import History_Session
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from pageObjects.capabilities import Capabilities_Page
from pageObjects.session import session
from Utilities.customLogger import LogGen


class TestHistorySessionPage:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    name = "vidya-test"
    timeout = 2
    logger = LogGen.loggen()
# 8 scenarios

    @pytest.fixture()
    def setup(self):
        capabilities = {'browserName': "chrome", 'version': "102.0",

                        'cloudify:options': {
                            'name': "vidya-test",
                            'enableLogs': True,
                            'enableVideo': True,
                            'screenResolution': "1366x768x24",
                            'timeout': 2,
                        }}

        self.driver = webdriver.Remote(
            command_executor=webdriver.remote.remote_connection.RemoteConnection(
                "https://26qa:4ad31fb557c844768d557df049be15c9@vidya-cloudify8.cloudifytests.io/wd/hub",
                resolve_ip=True),
            desired_capabilities=capabilities)
        #self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://stg.cloudifytests.io/")
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        yield
        self.driver.quit()

    @pytest.mark.scenario
    #1 validate browser column should not be present on history session page after remove from view column
    def test_browserColumnOn_historySession(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        self.comp.clickViewColumn()
        self.hp = History_Session(self.driver)
        self.hp.deselectBrowserInsideViewColumn()
        self.logger.info("***** browser has been deselected ********")
        self.logger.info("***** browser column is not found on history session page ********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #2 validate status text inside filter table on history session page
    def test_statusText_onHistory_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        self.comp.clickFilterTable()
        assert self.comp.checkStatustextFilterTable()
        self.logger.info("***** status text has been found inside filter table ********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #3 validate save video text inside filter table on history session page
    def test_saveVideoText_onHistory_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        self.comp.clickFilterTable()
        assert self.comp.checkSaveVideotextFilterTable()
        self.logger.info("***** save video text found inside filter table ********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #4 validate saved logs and videos are enabled on history session page after click on save logs and saves videos on capabilities page
    def test_enabledSaveLogsAndVideos_onHistory_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.logger.info("********** Routed on session page *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickCapabities()
        self.logger.info("********** Routed on capabilities page *********")
        self.cp = Capabilities_Page(self.driver)
        self.cp.setTestName(self.name)
        self.logger.info("***** test name has been filled ********")
        self.cp.clickBrowser()
        self.logger.info("***** browser is selected ********")
        self.cp.clickVersion()
        self.logger.info("***** browser version is selected ********")
        self.cp.clickScreenResolution()
        self.logger.info("***** screen resolution is selected ********")
        self.cp.selectManualSessionTimeout(self.timeout)
        self.logger.info("***** timeout has been filled ********")
        self.cp.clickSaveLogs()
        self.logger.info("***** save logs is selected on ********")
        self.cp.clickSaveVideos()
        self.logger.info("***** save videos is selected on ********")
        self.cp.clickRunManually()
        self.logger.info("***** run manual button has been clicked ********")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("********** Routed second tab where you can see VNC *********")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("********** Routed on parent page *********")
        self.comp.clickSession()
        self.logger.info("********** Routed on session page *********")
        self.sp = session(self.driver)
        self.sp.click_on_session_Terminate()
        self.logger.info("********** running session has been terminated *********")
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session  page *********")
        self.comp.clickSaveVideosAndLogsInViewColumn()
        self.logger.info("******** clicked on saved logs and videos inside view column history session  page ********")
        assert self.comp.saveVideoEnable()
        assert self.comp.saveLogsEnable()
        self.logger.info("********** saved logs and videos are enabled on history session page *********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #5 validate browser version text inside filter table on history session page
    def test_browserVersionText_insideFilterTable_onHistory_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        assert self.comp.checkBrowserVersionOnHistorySession() == True
        self.logger.info("***** browser version text found ********")
        self.logger.info("***** test case pass ********")


    @pytest.mark.scenario
    #6 validate session_id is displayed on history session page after selecting from filter table
    def test_sessionId_onHistory_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        self.comp.clickViewColumn()
        self.comp.clickSessionId()
        assert self.comp.checkSessionIdTextInColumn()
        self.logger.info("***** Session Id text found inside view column ********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #7 validate increase in number of session on history session page after click on run manually button on capabilities page and terminating the session
    def test_increaseInSessionCount_historySession(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session page *********")
        previous_history_session_number = self.comp.checkincreaseInSessionNumber()
        self.logger.info("********** check total number of session on history session page *********")
        self.comp.clickCapabities()
        self.logger.info("********** Routed on capabilities page *********")
        self.cp = Capabilities_Page(self.driver)
        self.cp.setTestName(self.name)
        self.logger.info("***** test name has been filled ********")
        self.cp.clickBrowser()
        self.logger.info("***** browser is selected ********")
        self.cp.clickVersion()
        self.logger.info("***** browser version is selected ********")
        self.cp.clickScreenResolution()
        self.logger.info("***** screen resolution is selected ********")
        self.cp.selectManualSessionTimeout(self.timeout)
        self.logger.info("***** timeout has been filled ********")
        self.cp.clickSaveLogs()
        self.logger.info("***** save logs is selected on ********")
        self.cp.clickSaveVideos()
        self.logger.info("***** save videos is selected on ********")
        self.cp.clickRunManually()
        self.logger.info("***** run manual button has been clicked ********")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("********** Routed second tab where you can see VNC *********")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("********** Routed on parent page *********")
        self.comp.clickSession()
        self.logger.info("********** Routed on session page *********")
        self.sp = session(self.driver)
        self.sp.click_on_session_Terminate()
        self.logger.info("********** running session has been terminated *********")
        self.comp.clickHistorySession()
        self.logger.info("********** Routed on history session  page *********")
        after_history_session_number = self.comp.checkincreaseInSessionNumber()
        self.logger.info("********** again check total number of session on history session page *********")
        assert previous_history_session_number != after_history_session_number
        self.logger.info("********** total number of session is increased by 1 on history session page *********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #8 validate history session page after click on view all on dashboard page after terminating running session
    def test_historySessionPageOnclickingViewAllOnDashboard(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickCapabities()
        self.logger.info("********** Routed on capabilities page *********")
        self.cp = Capabilities_Page(self.driver)
        self.cp.setTestName(self.name)
        self.logger.info("***** test name has been filled ********")
        self.cp.clickBrowser()
        self.logger.info("***** browser is selected ********")
        self.cp.clickVersion()
        self.logger.info("***** browser version is selected ********")
        self.cp.clickScreenResolution()
        self.logger.info("***** screen resolution is selected ********")
        self.cp.selectManualSessionTimeout(self.timeout)
        self.logger.info("***** timeout has been filled ********")
        self.cp.clickSaveLogs()
        self.logger.info("***** save logs is selected on ********")
        self.cp.clickSaveVideos()
        self.logger.info("***** save videos is selected on ********")
        self.cp.clickRunManually()
        self.logger.info("***** run manual button has been clicked ********")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.logger.info("********** Routed second tab where you can see VNC *********")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("********** Routed on parent page *********")
        self.comp.clickSession()
        self.logger.info("********** Routed on session  page *********")
        self.sp = session(self.driver)
        self.sp.click_on_session_Terminate()
        self.logger.info("********** running session has been terminated *********")
        self.comp.clickDashboard()
        self.logger.info("********** Routed on dashboard page *********")
        self.dp = Dashboard(self.driver)
        self.dp.clickViewAll()
        self.logger.info("********** Clicked on view all option on dashboard page *********")
        assert self.comp.checkHistorySession()
        self.logger.info("********** Routed on history session  page *********")
        self.logger.info("****test case pass*********")

