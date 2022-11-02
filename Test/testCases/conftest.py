import self
import random
import string
import pytest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from pageObjects.signin import Login
username = "5zb"
password = "Hello123#"


# @pytest.fixture(params=["chrome"], scope="class")
#
# def init__driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#         request.cls.driver = web_driver
#     # capabilities = {
#     #     "name": "test_vidya1",
#     #     "browserName": "chrome",
#     #     "version": "102.0",
#     #     "timeout": 2,
#     #     "cloudify:options": {
#     #         "screenResolution": "1920x1080x24",
#     #         "enableVideo": 'true',
#     #         "enableLogs": 'true'
#     #     }
#     # }
#     #
#     # driver = webdriver.Remote(command_executor=webdriver.remote.remote_connection.RemoteConnection
#     # ('https://5zb:fcdc0aed080444f3940335d986049287@vidya-cloudify.cloudifytests.io/wd/hub', resolve_ip=True),
#     #                                desired_capabilities=capabilities)
#     driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#     driver.maximize_window()
#
#     driver.get(
#         "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth")
#     lp = Login(driver)
#     lp.setLogin(username, password)
#     yield
#     driver.quit()
#     #return driver
class Conftest:
    def random_generator_new_organisationname(size=4, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))