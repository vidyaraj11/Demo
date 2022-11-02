import pytest
from selenium import webdriver
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.dashboard import Dashboard
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class TestDashboardPage:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()
#4 scenarios

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

        self.driver.get(
            "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        yield
        self.driver.quit()

    @pytest.mark.scenario
    #1 validate total,running and pending session of session page is same as dashboard page
    def test_total_running_pending_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********routed on session page *********")
        total_session_of_sessionpage = self.comp.checkTotalSesion()
        self.logger.info("******** total session is checked on session page *********")
        running_session_of_sessionpage = self.comp.checkRunningSession()
        self.logger.info("******** running session is checked on session page *********")
        pending_session_of_sessionpage = self.comp.checkPendingSession()
        self.logger.info("******** pending session is checked on session page *********")
        self.comp.clickDashboard()
        self.logger.info("********routed on dashboard page *********")
        total_session_of_dashboard = self.comp.checkTotalSesion()
        self.logger.info("******** total session is checked on dashboard page *********")
        running_session_of_dashboard = self.comp.checkRunningSession()
        self.logger.info("******** running session is checked on dashboard page *********")
        pending_session_of_dashboard = self.comp.checkPendingSession()
        self.logger.info("******** pending session is checked on dashboard page *********")
        assert total_session_of_sessionpage == total_session_of_dashboard, "total session is not same"
        assert running_session_of_sessionpage == running_session_of_dashboard, "running session is not same"
        assert pending_session_of_sessionpage == pending_session_of_dashboard, "pending session is not same"
        self.logger.info("******** total, running and pending session is matched on dashboard page *********")

    @pytest.mark.scenario
    #2 validate charts text on dashboard page
    def test_charts_text_onDashbord(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickDashboard()
        self.logger.info("********routed on dashboard page *********")
        self.dp = Dashboard(self.driver)
        assert self.dp.checkChartsText()
        self.logger.info("******** chart text found on dashboard page *********")

    @pytest.mark.scenario
    #3 validate  recent activities text on dashboard page
    def test_recentActivity_text_onDashboard(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickDashboard()
        self.logger.info("********routed on dashboard page *********")
        self.dp = Dashboard(self.driver)
        assert self.dp.checkRecentActivityText()
        self.logger.info("******** Recent Activity text found on dashboard page *********")

    @pytest.mark.scenario
    #4 validate  start date, end date and save button on dashboard page
    def test_startdate_enddate_savebutton_onDashboard(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickDashboard()
        self.logger.info("********routed on dashboard page *********")
        self.dp = Dashboard(self.driver)
        assert self.dp.checkStartDate()
        assert self.dp.checkEndDate()
        assert self.dp.checkSaveButton()
        self.logger.info("******** start date, end date and save button found on dashboard page *********")