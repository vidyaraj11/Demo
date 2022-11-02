import time
import pytest
from selenium import webdriver
from pageObjects.signin import Login
from Utilities.readProperties import Readconfig
from pageObjects.commonPage import CommonPage
from Utilities.customLogger import LogGen

class Test_Signin_Page:
    baseUrl2 = Readconfig.getUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    username2 = Readconfig.getUsername2()
    password2 = Readconfig.getPassword2()
    invalidUser = Readconfig.getInvalidUsername()
    invalidPassword = Readconfig.getInvalidPassword()
    logger = LogGen.loggen()

#total 4 scenarios

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
        yield
        time.sleep(2)
        self.logger.info("****test case pass*********")
        self.driver.quit()

    #scenarios
    @pytest.mark.scenario
    #1 first signin with valid credential then logout and again signin with different valid credential
    def test_signin_as_differentUser(self, setup):
        self.logger.info("********** successfully signin *********")
        self.logger.info("********login with credential *********")
        self.lp.setLogin(self.username, self.password)
        self.logger.info("*********Successful login **********")
        self.org = CommonPage(self.driver)
        self.logger.info("*******organisation page ******")
        self.org.clickOrgLogout()
        self.logger.info("*******Logout from org page**********")
        self.lp.signinAsDifferentUser()
        self.logger.info("********signin with different user *********")
        self.lp.setLogin(self.username2, self.password2)
        self.logger.info("*********successfully login with different username *******")

    @pytest.mark.testing1
    #2 validate you can logout from application after login
    def test_logout_org(self, setup):
        self.logger.info("********** successfully signin *********")
        self.lp.setLogin(self.username, self.password)
        self.logger.info("********login with valid username and password *********")
        self.logger.info("********routed on organisation list page *********")
        self.driver.back()
        self.logger.info("********clicked on backward optin *********")
        self.logger.info("********logout from application*********")
        differentuser = self.lp.checksigninAsDifferentUserText()
        assert differentuser == True
        self.logger.info("******** found text sign in as different user *********")

    @pytest.mark.scenario
    #3 validate invalid msg with invalid credential
    def test_invalidMsg_signinPage(self, setup):
        self.logger.info("********** successfully signin *********")
        self.lp.setLogin(self.invalidUser, self.invalidPassword)
        self.logger.info("********** unable to login with invalid username and password *********")
        invalidMsg = self.lp.checkInvalidMsgText()
        assert invalidMsg == True
        self.logger.info("********** invalid msg text found *********")

    @pytest.mark.scenario
    #4 validate all elements on signin page
    def test_allElementOn_signinPage(self, setup):
        self.logger.info("********** successfully signin *********")
        username = self.lp.checkUsernameText()
        assert username == True
        self.logger.info("********** Username textbox is present on signin page *********")
        password = self.lp.checkPasswordText()
        assert password == True
        self.logger.info("********** Password textbox is present on signin page *********")
        forgotPass = self.lp.checkForgotPasswordText()
        assert forgotPass == True
        self.logger.info("********** Forgot password option is present on signin page *********")
        signinButton = self.lp.checkSigninButton()
        assert signinButton == True
        self.logger.info("********** sign in button is present on sign in page *********")
        signupoption = self.lp.checkSignupLinkOnSignin()
        assert signupoption == True
        self.logger.info("********** sign up option present on sign in page *********")
