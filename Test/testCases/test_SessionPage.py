import pytest
from selenium import webdriver

from pageObjects.capabilities import Capabilities_Page
from pageObjects.create_org import Create_org_page
from pageObjects.pricing import PricingPage
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.dashboard import Dashboard
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from pageObjects.stripe import Stripe_Page


class Test_Session_Page:
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    orgName = CommonPage.random_generator_new_organisationname()
    logger = LogGen.loggen()
    cardnumber = 4242424242424242
    cardExp = 242
    cardCvc = 422
    cardName = "Demo"
    cardAdd ="Demo"
    name = "vidya-test"
    timeout = 3
#17 scenarios

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
    #1 validate session text on session page
    def test_session_textOnSessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkSession()
        self.logger.info("***** session text found on session page ********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #2 validate search icon on session page
    def test_search_icon_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkSearchIcon()
        self.logger.info("***** search icon has found on session page ********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #3 validate view column on session page
    def test_viewColumn_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkViewColumn()
        self.logger.info("***** view column has found on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #4 validate filter table on session page
    def test_filterTable_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.clickFilterTable()
        self.logger.info("***** filter table has found on session page ********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #5 validate profile icon on session page
    def test_profile_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkProfile()
        self.logger.info("***** profile icon has found on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #6 validate username after clicking on profile icon
    def test_profileUsername_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkUsername()
        self.logger.info("***** username has been found inside profile on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #7 validate manage plan after clicking on profile icon
    def test_managePlan_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkManagePlans()
        self.logger.info("***** manage plan has been found inside profile on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #8 validate setting after clicking on profile icon
    def test_setting_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkSetting()
        self.logger.info("***** setting has been found inside profile on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #9 validate logout button after clicking on profile icon
    def test_logout_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkLogout()
        self.logger.info("***** logout button has been found inside profile on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #10 validate screen resolution text inside filter table on session page
    def test_screenResolution_onSessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        self.comp.clickFilterTable()
        self.logger.info("***** clicked on filter table on session page ********")
        assert self.comp.checkScreenResolutionInFilterTable()
        self.logger.info("***** screen resolution text has been found inside filter table on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #11 validate save logs text inside filter table on session page
    def test_saveLogs_onSessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        self.comp.clickFilterTable()
        self.logger.info("***** clicked on filter table on session page ********")
        assert self.comp.checkSaveLogsInFilterTable()
        self.logger.info("***** save logs text has been found inside filter table on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #12 validate reset text inside filter table on session page
    def test_resetText_onSessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        self.comp.clickFilterTable()
        self.logger.info("***** clicked on filter table on session page ********")
        assert self.comp.checkResetTextInFilterTable()
        self.logger.info("***** reset text has been found inside filter table on session page ********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #13 validate no data found text on session page when no session is running
    def noDataFound_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        assert self.comp.checkNoDataFoundText()
        self.logger.info("***** no data found taxt on session page when no session was running ********")
        self.logger.info("**** test case pass ********")

    @pytest.mark.scenario
    #14 validate organisation is created after payment on stripe page
    def test_creationOfOrg_sessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickOnCreate()
        self.logger.info("********clicked on create button on organisation list page *********")
        self.createorg = Create_org_page(self.driver)
        self.createorg.clickEnter_organisation_text(self.orgName)
        self.logger.info("******** filled new org name on create organisation page *********")
        self.createorg.Create_button()
        self.logger.info("******** clicked on create button to create new org on create org page *********")
        self.pp = PricingPage(self.driver)
        self.logger.info("********routed on pricing page *********")
        self.pp.Confirm_button()
        self.logger.info("******** clicked on confirm button on pricing page *********")
        self.strp = Stripe_Page(self.driver)
        self.logger.info("********routed on stripe page *********")
        self.strp.clickOnChange()
        self.logger.info("******** clicked on change option on stripe page *********")
        self.strp.fillCardNumber(self.cardnumber)
        self.logger.info("******** filled card number on stripe page *********")
        self.strp.fillCardExpiry(self.cardExp)
        self.logger.info("******** filled card expiry on stripe page *********")
        self.strp.fillCardCvc(self.cardCvc)
        self.logger.info("******** filled card cvc on stripe page *********")
        self.strp.fillCardName(self.cardName)
        self.logger.info("******** filled card name on stripe page *********")
        self.strp.fillBillingAddress(self.cardAdd)
        self.logger.info("******** filled billing address on stripe page *********")
        self.strp.clickOnSubscriptionButton()
        self.logger.info("******** clicked on subscribe button on stripe page *********")
        self.comp.checkSession()
        self.logger.info("******** organisation has been created *********")
        self.logger.info("****test case pass ********")

    @pytest.mark.scenario
    #15 validate increase in number of session on session page after click on run manually button on capabilities page
    def test_increaseInSessionCount_session(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
        prvious_session_number = self.comp.checkincreaseInSessionNumber()
        self.logger.info("********** check total number of sessions on session page *********")
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
        after_session_number = self.comp.checkincreaseInSessionNumber()
        self.logger.info("********** again check total number of session on history session page *********")
        assert prvious_session_number != after_session_number
        self.logger.info("********** total number of sessions is increased by 1 on session page *********")
        self.logger.info("****test case pass ********")


    @pytest.mark.scenario
    #16 when we click on view all button at time of sessions are running then it should route to session page
    def test_sessionPageAfterClickOnDashboard(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
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
        self.comp.clickDashboard()
        self.logger.info("********** Routed on dashboard page *********")
        self.dp = Dashboard(self.driver)
        self.dp.clickViewAll()
        self.logger.info("********** Clicked on view all option on dashboard page *********")
        assert self.comp.checkHistorySession()
        self.logger.info("********** Routed on session  page *********")
        self.logger.info("***** test case pass ********")

    @pytest.mark.scenario
    #17 validate saved logs and videos are enabled on session page after click on save logs and saves videos on capabilities page
    def test_saveLogsAndVieosEnable_OnSession(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = organisationList(self.driver)
        self.logger.info("********routed on organisation list page *********")
        self.org.clickExplore()
        self.logger.info("********clicked on explore button *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("********** Routed on session page *********")
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
        self.comp.clickSaveVideosAndLogsInViewColumn()
        self.logger.info("******** clicked on saved logs and videos inside view column history session  page ********")
        assert self.comp.saveVideoEnable()
        assert self.comp.saveLogsEnable()
        self.logger.info("********** saved logs and videos are enabled on session page *********")
        self.logger.info("****test case pass ********")

