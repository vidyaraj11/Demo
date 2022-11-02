import pytest
from selenium import webdriver
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.setting import Setting_Page
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class TestSettingPage:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()
    manual_sessiontime = "2"
    sesstiontime = "2"
#3 scenarios

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
    #1 validating save button after choosing chrome, version-100, manual session and sesstion timeout with logs and video on setting page
    def test_saveButton_withAll_data(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickSetting()
        self.logger.info("******** clicked on setting on session page *********")
        self.setp = Setting_Page(self.driver)
        self.logger.info("********routed on setting page *********")
        self.setp.selectChrome()
        self.logger.info("******** chrome browser has been selected on setting page *********")
        self.setp.selectBrowserVersion()
        self.logger.info("******** chrome browser version has been selected on setting page *********")
        self.setp.clickScreen_resolution()
        self.logger.info("******** screen resolution has been selected on setting page *********")
        self.setp.clickSaveLogs()
        self.logger.info("******** save log is on selected on setting page *********")
        self.setp.clickSaveVideos()
        self.logger.info("******** save video is on selected on setting page *********")
        self.setp.selectManualSessionTimeout(self.manual_sessiontime)
        self.logger.info("******** manual session timeout has been selected on setting page *********")
        self.setp.selectSessionTimeout(self.sesstiontime)
        self.logger.info("******** session timeout has been selected on setting page *********")
        self.setp.clickSave_button()
        self.logger.info("******** clicked on save button on setting page *********")
        assert self.setp.checkVariablesChanged()
        self.logger.info("******** variables changed text found on setting page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #2 validating save button on setting page
    def test_saveButton_onSettingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickSetting()
        self.logger.info("******** clicked on setting on session page *********")
        self.setp = Setting_Page(self.driver)
        self.logger.info("********routed on setting page *********")
        assert self.setp.checkSave_button()
        self.logger.info("******** save button found on setting page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #3 validate new token is regenerated after clicking on regenerate token button
    def test_saveButton_withAll_data(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickSetting()
        self.logger.info("******** clicked on setting on session page *********")
        self.setp = Setting_Page(self.driver)
        self.logger.info("********routed on setting page *********")
        before_regeneratedtoken = self.setp.checkAutomationToken()
        self.logger.info("******** check token on setting page *********")
        self.setp.clickRegenate_button()
        self.logger.info("******** clicked on regenerate token button on setting page *********")
        regenrated_token = self.setp.checkAutomationToken2()
        self.logger.info("******** check token after regenetion on setting page *********")
        assert before_regeneratedtoken != regenrated_token, "token is same"
        self.logger.info("******** token is not matched on setting page *********")
        self.logger.info("****test case pass*********")


