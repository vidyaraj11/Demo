import time
import pytest
from selenium import webdriver
from pageObjects.signin import Login
from Utilities.readProperties import Readconfig
from pageObjects.organisationListPage import organisationList
from pageObjects.create_org import Create_org_page
from pageObjects.commonPage import CommonPage
from pageObjects.pricing import PricingPage
from Utilities.customLogger import LogGen


class TestPricingPage:
    # baseUrl2 = Readconfig.getUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    orgName = CommonPage.random_generator_new_organisationname()
    logger = LogGen.loggen()
#total 9 scenarios

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
        #self.driver = webdriver.Chrome(executable_path="D://chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://stg.cloudifytests.io/")
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        yield
        time.sleep(2)
        self.driver.quit()


    #scenarios
    @pytest.mark.scenario
    #1 validate logout button on pricing page
    def test_logoutOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.commonpage = CommonPage(self.driver)
        assert self.commonpage.checkOrgLogout()
        self.logger.info("**** logout button found on pricing page *********")
        self.logger.info("***** test case pass *********")


    @pytest.mark.scenario
    #2 validate organisation name on pricing page
    def test_orgNameOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.Check_orgName_text()
        self.logger.info("**** organisation name found on pricing page *******")
        self.logger.info("***** test case pass *******")

    @pytest.mark.scenario
    #3 validate parallel session text on pricing page
    def test_parallelSessionTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.CheckParallelSession_text()
        self.logger.info("***** parallel session text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #4 validate plan period text on pricing page
    def test_planPeriodTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.CheckPlanPeriod_text()
        self.logger.info("***** parallel period text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #5 validate pricing text on pricing page
    def test_pricingTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.Check_pricing_text()
        self.logger.info("***** pricing text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #6 validate retention period text on pricing page
    def test_retentionPeriodTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.CheckRetentionPeriod_text()
        self.logger.info("***** retention period text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #7 validate total parallel session text on pricing page
    def test_totalParallelSessionTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.CheckTotalParallelSession_text()
        self.logger.info("***** total parallel session text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #8 validate total price text on pricing page
    def test_totalPriceTextOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.pp = PricingPage(self.driver)
        assert self.pp.TotalPrice_text()
        self.logger.info("***** total price text found on pricing page *******")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #9 validate cloudify.io text on pricing page
    def test_platformNametOn_pricingPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.cb = organisationList(self.driver)
        self.cb.clickOnCreate()
        self.logger.info("*****clicked on create button on organisation list page*********")
        self.createorg = Create_org_page(self.driver)
        self.logger.info("**** routed on create organisation page *********")
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("*****filled new organisation name on create organisation page*********")
        self.createorg.Create_button()
        self.logger.info("*****clicked on create button on create organisation page*********")
        self.logger.info("**** routed on pricing page *********")
        self.cp = CommonPage(self.driver)
        assert self.cp.Check_platformName()
        self.logger.info("***** cloudify.io text found on pricing page *******")
        self.logger.info("***** test case pass *********")