import configparser

config = configparser.RawConfigParser()
config.read('/Users/bargelman/PycharmProjects/python_Automation_Projects/Percepto/configurations/config.ini')


class ReadConfig:

    @staticmethod
    def getApplicationBrowserType():
        browser = config.get('common info', 'browserType')
        return browser

    @staticmethod
    def getApplicationBaseURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getApplicationBasedir():
        baseDir = config.get('common info', 'baseDir')
        return baseDir

    @staticmethod
    def getApplicationloginJsonPath():
        loginJsonPath = config.get('common info', 'loginJsonPath')
        return loginJsonPath
