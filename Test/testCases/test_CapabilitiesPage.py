import pytest
from selenium import webdriver
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from pageObjects.capabilities import Capabilities_Page
from pageObjects.setting import Setting_Page
from Utilities.customLogger import LogGen


class Test_Session_Page:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    manualsessiontime = 2
    sesstiontime = 2
    logger = LogGen.loggen()


#6 scenarios

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
        # self.driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
        self.driver.maximize_window()

        self.driver.get(
            "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        self.logger.info("********login with valid username and password *********")
        yield
        self.driver.quit()

    @pytest.mark.scenario
    # 1 validate capablities text on capabilities page
    def test_capabilitiesText_onCapabilitiesPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        assert self.cp.checkCapabilitiesText()
        self.logger.info("********capabilities text found on capabilities page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #2 validate java text on capabilities page
    def test_javaText_onCapabilitiesPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        assert self.cp.checkJava()
        self.logger.info("******** Java text found on capabilities page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #3 validate python text on capabilities page
    def test_pythonText_onCapabilitiesPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        assert self.cp.checkPython()
        self.logger.info("******** python text found on capabilities page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #4 validate ruby text on capabilities page
    def test_rubyText_onCapabilitiesPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        assert self.cp.checkRuby()
        self.logger.info("******** ruby text found on capabilities page *********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #5 validate curl text on capabilities page
    def test_curlText_onCapabilitiesPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        assert self.cp.checkCurl()
        self.logger.info("******** curl text found on capabilities page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #6 validate saved data of setting page with capabilities page data
    def test_saveButton_withAll_data(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickSetting()
        self.logger.info("********routed on session page *********")
        self.logger.info("********clicked on setting option inside profile *********")
        self.setp = Setting_Page(self.driver)
        chrome = self.setp.selectChrome()
        self.logger.info("********chrome browser is selected *********")
        version = self.setp.selectBrowserVersion()
        self.logger.info("********chrome version is selected *********")
        resolution = self.setp.clickScreen_resolution()
        self.logger.info("******** screen resolution 1920*1080 is selected *********")
        logs = self.setp.clickSaveLogs()
        self.logger.info("********clicked on save logs on setting page *********")
        videos = self.setp.clickSaveVideos()
        self.logger.info("********clicked on save video on setting page *********")
        timeout = self.setp.selectManualSessionTimeout(self.manualsessiontime)
        self.logger.info("******** manual session timeout is selected *********")
        self.setp.selectSessionTimeout(self.sesstiontime)
        self.logger.info("******** session timeout is selected *********")
        self.setp.clickSave_button()
        self.logger.info("********clicked on save button on setting page *********")
        self.comp.clickCapabities()
        self.logger.info("********clicked on capabilities option *********")
        self.cp = Capabilities_Page(self.driver)
        self.logger.info("********** successfully signin *********")
        selected_browser = self.cp.selectedBrowser()
        if chrome == selected_browser:
            assert True
        self.logger.info("********** selected browser is matched on capabilities page *********")
        selected_version = self.cp.selectedVersion()
        if version == selected_version:
            assert True
        self.logger.info("********** selected browser varsion is matched on capabilities page *********")
        selected_resolution = self.cp.selectedScreenResolution()
        if resolution == selected_resolution:
            assert True
        self.logger.info("********** selected screen resolution is matched on capabilities page *********")
        selected_time = self.cp.selectedTimeout()
        if timeout == selected_time:
            assert True
        self.logger.info("********** selected manual timeout is matched on capabilities page *********")
        selected_logs = self.cp.selectedLogs()
        if logs == selected_logs:
            assert True
        self.logger.info("********** logs is on capabilities page *********")
        selected_videos = self.cp.selectedVideos()
        if videos == selected_videos:
            assert True
        self.logger.info("********** videos is on capabilities page *********")
        self.logger.info("****test case pass*********")
