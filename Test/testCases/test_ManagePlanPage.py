import pytest
from selenium import webdriver
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.managePlan import ManagePlan
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class TestManagePlanPage:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()
#5 scenarios

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

        # self.driver = setup1
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        yield
        self.driver.quit()
    @pytest.mark.scenario
    #1 validate parallel session text on manage plan page
    def test_parallelSession_onManagePlan(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickManagePlans()
        self.logger.info("********clicked on manage plan *********")
        self.mp = ManagePlan(self.driver)
        self.logger.info("********** Routed on manage plan page *********")
        assert self.mp.checkParallelSessionText()
        self.logger.info("******** parallel session text is present on manage plan page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #2 validate retention period text on manage plan page
    def test_retentionPeriod_onManagePlan(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickManagePlans()
        self.logger.info("********clicked on manage plan *********")
        self.mp = ManagePlan(self.driver)
        self.logger.info("********** Routed on manage plan page *********")
        assert self.mp.retentionPeriodText()
        self.logger.info("******** retention period is present on manage plan page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #3 validate plan period text on manage plan page
    def test_planDuration_onManagePlan(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickManagePlans()
        self.logger.info("********clicked on manage plan *********")
        self.mp = ManagePlan(self.driver)
        self.logger.info("********** Routed on manage plan page *********")
        assert self.mp.checkPlanDurationText()
        self.logger.info("******** plan duration text is present on manage plan page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #4 validate retention period text on manage plan page
    def test_planText_onManagePlan(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickManagePlans()
        self.logger.info("********clicked on manage plan *********")
        self.mp = ManagePlan(self.driver)
        self.logger.info("********** Routed on manage plan page *********")
        assert self.mp.checkPlanText()
        self.logger.info("******** plan text is present on manage plan page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #5 validate upgrate button on manage plan page
    def test_upgrateButton_onManagePlan(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.comp.clickManagePlans()
        self.logger.info("********clicked on manage plan *********")
        self.mp = ManagePlan(self.driver)
        self.logger.info("********** Routed on manage plan page *********")
        assert self.mp.checkUpgratePlanButton()
        self.logger.info("******** upgrate button is present on manage plan page *********")
        self.logger.info("****test case pass*********")

