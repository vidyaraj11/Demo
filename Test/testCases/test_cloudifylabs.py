# import time
# import pytest
# from selenium import webdriver
# from pageObjects.login import Login
# from pageObjects.organisationListPage import organisationList
# from pageObjects.create_org import Create_org_page
# from pageObjects.signup import signup
# from pageObjects.pricing import Pricing_Page
# from pageObjects.stripe import Stripe_Page
# from pageObjects.session import session
# from pageObjects.setting import Setting_Page
# from pageObjects.capabilities import Capabilities_Page
# #@pytest.mark.po
#
# class Test_org_icon:
#     baseUrl = "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth"
#     baseUrl2 = "https://stage-cloudifytests.ap-south-1.amazoncognito.com/login?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth"
#     username = "5zb"
#     password = "Hello123#"
#     username2 = "1zb"
#     password2 = "Hello123#"
#     invalidUser = "12345"
#     invalidPassword = "12345"
#     signupUrl = "https://stage-cloudifytests.auth.ap-south-1.amazoncognito.com/signup?client_id=5s5aovc7epna18uoi47dkahnc1&response_type=code&scope=profile+aws.cognito.signin.user.admin+openid+email+phone&redirect_uri=https://stg.cloudifytests.io/auth"
#     newUser = "19qa"
#     name = "19qa"
#     email = "19qa@mailinator.com"
#     newPassword = "Hello123#"
#     newOrgName = "abcd"
#     sessionNumber = "444"
#     manualsession_timeout = "5"
#     session_timeout = "5"
#     def test_icon_onOrglist(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)                        # created lp objt for Login cls to acess all actn mthd
#         self.lp.setLogin(self.username, self.password)              # calling actn mthd thrgh objt lp
#         self.org = organisationList(self.driver)
#         icon_org = self.org.platformIcon()
#         assert icon_org == True
#         self.driver.close()
#
#     def test_heading_onOrglist(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         heading_org = self.org.platformName()
#         assert heading_org == True
#         self.driver.close()
#
#     def test_logout_ofSessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)  # created lp objt for Login cls to acess all actn mthd
#         self.lp.setLogin(self.username, self.password)  # calling actn mthd thrgh objt lp
#         self.org = organisationList(self.driver)
#         self.org.clickProfile()
#         logout_org = self.org.checkLogout()
#         assert logout_org == True
#         self.driver.close()
#
#     def test_session_textOnSessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#
#         self.orgl= organisationList(self.driver)
#         self.orgl.clickExplore()
#         self.sp = session(self.driver)
#         self.sp.checkSession()
#
#         sesionPage = self.sp.checkSession()
#         assert sesionPage == True
#         self.driver.close()
#
#     def test_signin_invalid_data(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.invalidUser, self.invalidPassword)
#         self.driver.close()
#
#     def test_signin_as_differentUser(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickProfile()
#         self.org.clickLogout()
#         self.lp.signinAsDifferentUser()
#         self.lp.setLogin(self.username2, self.password2)
#         self.driver.close()
#
#     def test_signin_with_incorrectUrl(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl2)                          #7
#         self.driver.close()
#
#     def test_logout(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.driver.back()
#         differentuser = self.lp.checksigninAsDifferentUser()
#         assert differentuser == True
#         self.driver.close()
#
#     def test_orglist_afterforward(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.driver.back()
#         self.driver.forward()
#         self.org = organisationList(self.driver)
#         orgtext= self.org.organisation_text()
#         assert orgtext == True
#         self.driver.quit()
#
#     def test_invalidMsg_signinPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.invalidUser, self.invalidPassword)
#         invalidMsg = self.lp.checkInvalidMsg()
#         assert invalidMsg == True
#
#         self.driver.close()
#
#     def test_AllelementOn_signinPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         username = self.lp.checkUsernameText()
#         assert username == True
#         password = self.lp.checkPasswordText()
#         assert password == True
#         forgotPass = self.lp.checkForgotPasswordText()
#         assert forgotPass == True
#         signinButton = self.lp.checkSigninButton()
#         assert signinButton == True
#         signupoption = self.lp.checkSignupLink()
#         assert signupoption == True
#         self.driver.close()
#
#     def test_orglist_info(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.info_button()
#         info_org = self.org.info_button()
#         assert info_org == True
#         self.driver.close()
#
#     def test_orglist_explore(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#
#         explore_org = self.org.explore_button()
#         assert explore_org == True
#         self.driver.quit()
#
#     def test_organisations_text(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#
#         org_text = self.org.organisation_text()
#         assert org_text == True
#         self.driver.quit()
#
#     def test_orglist_afterSessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         self.sp.clickViewOrg()
#         org_text = self.org.organisation_text()
#         assert org_text == True
#         self.driver.quit()
#
#     # def test_cloudifytestsio_oncreateorg(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                            #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickCreate()
#     #     self.co = Create_org_page(self.driver)
#     #     cloudifytext = self.co.Cloudifytests()
#     #     assert cloudifytext == True
#     #     self.driver.quit()
#
#     # def test_error_msg_signup(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.signupUrl)
#     #     self.su = signup(self.driver)
#     #     self.su.signup(self.newUser, self.name, self.email, self.newPassword)               #recheck(17)
#     #     self.driver.back()
#     #     msg = self.su.errorMsg()
#     #     assert msg == True
#     #     self.driver.quit()
#
#     # def test_pricing_text(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickCreate()
#     #     self.co = Create_org_page(self.driver)
#     #     self.co.New_orgname(self.newOrgName)                    #make new org(18) do not run this
#     #     self.co.Create_button()
#     #     self.pp = Pricing_Page(self.driver)
#     #     pricing = self.pp.Check_pricing_text()
#     #     assert pricing == True
#     #     self.driver.quit()
#
#     # def test_nameOn_pricingPage(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     orgtext = self.pp.Check_orgName_text()
#     #     assert orgtext == True
#     #     self.driver.quit()
#
#     # def test_totalParallelSession(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                                   #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.TotalParallelSession_text()
#     #     assert text == True
#     #     self.driver.quit()
#
#     # def test_totalParallelSession_info(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                        #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.TotalParallelSession_info()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_retentionPeriod(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.RetentionPeriod_text()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_retentionPeriod_info(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                      #23/do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.RetentionPeriod_info()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_planPeriod(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.PlanPeriod_text()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_freeSession_text(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                        #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     text = self.pp.FreeSessions_text()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_freeSession_checkbox(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     self.pp.FreeSession_checkbox()
#     #     self.driver.quit()
#     #
#     # def test_confirmButton_onPricingPage(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     button = self.pp.check_Confirm_button()
#     #     assert button == True
#     #     self.driver.quit()
#     #
#     # def test_stripePage(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                    #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     self.pp.Confirm_button()
#     #     self.stripe = Stripe_Page(self.driver)
#     #     text = self.stripe.Change()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_total_price(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                #do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     self.pp.inputParallelSession(self.sessionNumber)
#     #     self.pp.Confirm_button()
#     #     text = self.pp.Check_pricing_text()
#     #     assert text == True
#     #     self.driver.quit()
#     #
#     # def test_priceOfStripe_page(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)                                     #check30 /do not run this
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.pp = Pricing_Page(self.driver)
#     #     pTotalPrice = self.pp.TotalPrice()
#     #     assert pTotalPrice == True
#     #     self.pp.Confirm_button()
#     #     self.sp = Stripe_Page(self.driver)
#     #     sTotalPrice = self.sp.Price()
#     #
#     #     assert sTotalPrice== True
#     #     if pTotalPrice == sTotalPrice:
#     #         assert True
#     #
#     #     self.driver.quit()
#     #
#     # def test_subscription_button(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)                            #check/ do not run this
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickCreate()
#     #     self.cp = Create_org_page(self.driver)
#     #     self.cp.New_orgname(self.newOrgName)
#     #     self.cp.Create_button()
#     #     self.pp = Pricing_Page(self.driver)
#     #     self.pp.Confirm_button()
#     #     self.sp = Stripe_Page(self.driver)
#     #     # subscription = self.sp.checkSubscription()
#     #     # assert subscription == True
#     #     self.sp.Subscription()
#     #     self.driver.quit()
#
#     def test_search_icon_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)                            #check
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         sesrch_icon = self.sp.checkSearchIcon()
#         assert sesrch_icon == True
#         self.driver.quit()
#
#     def test_viewColumn_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         view_column = self.sp.checkViewColumn()
#         assert view_column == True
#         self.driver.quit()
#
#     def test_filterTable_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         view_column = self.sp.checkViewColumn()
#         assert view_column == True
#         self.driver.quit()
#
#     def test_profile_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         profile = self.sp.checkProfile()
#         assert profile == True
#         self.driver.quit()
#
#     def test_profileUsername_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         profile_username = self.sp.checkUsername()
#         assert profile_username == True
#         self.driver.quit()
#
#     def test_managePlan_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         my_plans = self.sp.checkMyPlans()
#         assert my_plans == True
#         self.driver.quit()
#
#     def test_setting_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         setting = self.sp.checkSetting()
#         assert setting == True
#         self.driver.quit()
#
#     def test_logout_sessionPage(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseUrl)
#         self.lp = Login(self.driver)
#         self.lp.setLogin(self.username, self.password)
#         self.org = organisationList(self.driver)
#         self.org.clickExplore()
#         self.sp = session(self.driver)
#         setting = self.sp.checkLogout()
#         assert setting == True
#         self.driver.quit()
#
#     # def test_browserVersionOfSession(self, setup):
#     #     self.driver = setup
#     #     self.driver.get(self.baseUrl)
#     #     self.lp = Login(self.driver)
#     #     self.lp.setLogin(self.username, self.password)
#     #     self.org = organisationList(self.driver)
#     #     self.org.clickExplore()
#     #     self.sp = session(self.driver)
#     #     self.sp.clickSetting()
#     #     self.setting = Setting_Page(self.driver)
#     #     self.setting.selectChrome()
#     #     self.setting.selectBrowserVersion()
#     #     self.setting.clickScreen_resolution()
#     #     self.setting.selectManualSessionTimeout(self.manualsession_timeout)             #incomplete
#     #     self.setting.selectSessionTimeout(self.session_timeout)
#     #     self.setting.clickSave_button()
#     #     self.sp.clickCapabities()
#     #     self.capabilities = Capabilities_Page(self.driver)
#     #     self.capabilities.setTestName(self.name)
#     #     self.capabilities.clickRunManually()
#     #     self.driver
#     #     self.sp.clickSession()
#     #     version = self.sp.checkBrowserVersion()
#     #     assert version == True
#     #     self.driver.quit()
#
#
#
