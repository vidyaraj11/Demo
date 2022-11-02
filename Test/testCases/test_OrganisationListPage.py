import pytest
from selenium import webdriver
from pageObjects.signin import Login
from pageObjects.organisationListPage import organisationList
from pageObjects.commonPage import CommonPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_OrganisationList_page:
    baseurl = Readconfig.getBaseUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()
#9

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
        #print("driver:", self.driver)
        self.lp = Login(self.driver)
        self.lp.setLogin(self.username, self.password)
        yield
        self.driver.quit()

    @pytest.mark.scenario
    #1 validate cloudifylabs icon on organisation list page
    def test_icon_onOrglist(self, setup):
        self.logger.info("********** successfully signin *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("**** routed on organisation list page*********")
        assert self.comp.Check_platformIcon()
        self.logger.info("**** cloudify labs icon found*********")
        self.logger.info("****test case pass*********")


    @pytest.mark.scenario
    #2 validate cloudify heading on organisation list page
    def test_heading_onOrglist(self, setup):
        self.logger.info("********** successfully signin *********")
        self.comp = CommonPage(self.driver)
        self.logger.info("**** routed on organisation list page*********")
        assert self.comp.Check_platformName()
        self.logger.info("**** CloudifyLabs.io found*********")
        self.logger.info("***** test case pass *********")

    @pytest.mark.scenario
    #3 validate logout button on organisation list page
    def test_logout_ofSessionPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.org = CommonPage(self.driver)
        self.logger.info("**** routed on organisation list page*********")
        self.org.clickProfile()
        self.logger.info("**** clicked on profile icon on organisation list page*********")
        logout_org = self.org.checkLogout()
        assert logout_org == True
        self.logger.info("**** logout button found on organisation list page*********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #4 validate organisation list page after signin, click on backward and forward option
    def test_orglist_afterforward(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.driver.back()
        self.logger.info("**** clicked backward from organisation list page*********")
        self.driver.forward()
        self.logger.info("**** clicked forward on page*********")
        self.org = organisationList(self.driver)
        assert self.org.checkOrganisation_text()
        self.logger.info("**** organisation text found on organisation list page*********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #5 validate info button on org list
    def test_orglist_info(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.org = organisationList(self.driver)
        assert self.org.info_button()
        self.logger.info("**** info button found on organisation list page*********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #6 validate vidya-cloudify explore button on org list
    def test_orglist_explore(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.org = organisationList(self.driver)
        assert self.org.explore_button()
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #7 validate organisation text on org list
    def test_organisations_text(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.org = organisationList(self.driver)
        org_text = self.org.checkOrganisation_text()
        assert org_text == True
        self.logger.info("**** explore button found on organisation list page*********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #8 validate org list after click on view org on session page
    def test_orglist_afterClickOnViewOrg(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.org = organisationList(self.driver)
        self.org.clickExplore()
        self.logger.info("********** Routed on session page *********")
        self.sp = CommonPage(self.driver)
        self.sp.clickViewOrg()
        self.logger.info("********** clicked on view organisation on session page *********")
        assert self.org.checkOrganisation_text()
        self.logger.info("********** Routed on organisation list page *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #9 validate all organisation one by one of organisation page whether it is routing on session page or pricing page
    def test_allOrg_onOrglist(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("**** routed on organisation list page*********")
        self.org = organisationList(self.driver)
        self.org.ExploreAll()
        self.logger.info("**** all explore button has been visited on organisation list page*********")
        self.logger.info("****test case pass*********")