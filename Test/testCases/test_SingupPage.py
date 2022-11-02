import pytest
from selenium import webdriver
from pageObjects.signup import signup
from pageObjects.create_org import Create_org_page
from Utilities.customLogger import LogGen


class Test_Signup_Page:
    newUser = "22qa"
    name = "22qa"
    email = "22qa@mailinator.com"
    newPassword = "Hello123#"
    logger = LogGen.loggen()
    # signupUrl = "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/signup?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth"
#2 sce
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
            "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/signup?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")

        yield
        self.driver.quit()

    @pytest.mark.scenario
    #1 validate error msg on signup with valid data and click on back option after confirming the validation otp
    def test_error_msg_signup(self, setup):
        self.logger.info("********routed on sign up page *********")
        self.su = signup(self.driver)
        self.su.signup(self.newUser, self.name, self.email, self.newPassword)
        self.logger.info("******** successfully sign up with validation otp*********")
        self.createorg = Create_org_page()
        assert self.createorg.checkCreate_org_text()
        self.logger.info("******** routed on create organisation page *********")
        self.driver.back()
        self.logger.info("******** clicked on backward *********")
        assert self.su.errorMsg()
        self.logger.info("******** error msg found(User cannot be confirmed, do not refresh the confirmation page) *********")
        self.logger.info("****test case pass*********")

    @pytest.mark.scenario
    #2 validate user can create new account on cloudify
    def test_newUser_signup(self, setup):
        self.logger.info("********routed on sign up page *********")
        self.su = signup(self.driver)
        self.su.signup(self.newUser, self.name, self.email, self.newPassword)
        self.logger.info("******** successfully sign up with validation otp*********")
        self.createorg = Create_org_page()
        assert self.createorg.checkCreate_org_text()
        self.logger.info("******** routed on create organisation page *********")
        self.logger.info("******** new user has been created *********")
        self.logger.info("****test case pass*********")
