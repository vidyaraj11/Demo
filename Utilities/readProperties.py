import configparser

#make object for class rawconfigparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\Vidya raj\\PycharmProjects\\framework\\Configurations\\config.ini")

class Readconfig:
    #make satatic method so that we can access it directly without using object
    @staticmethod
    def getBaseUrl():
        baseurl = config.get('common info', 'baseUrl')
        return baseurl

    @staticmethod
    def getUrl():
        url = config.get('common info', 'baseUrl2')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getUsername2():
        username2 = config.get('common info', 'username2')
        return username2

    @staticmethod
    def getPassword2():
        password2 = config.get('common info', 'password2')
        return password2

    @staticmethod
    def getInvalidUsername():
        invalid_username = config.get('common info', 'invalidUser')
        return invalid_username

    @staticmethod
    def getInvalidPassword():
        invalidPassword = config.get('common info', 'invalidPassword')
        return invalidPassword

    @staticmethod
    def enterOrgName():
        orgname = config.get('common info', 'orgName')
        return orgname
