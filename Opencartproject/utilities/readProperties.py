import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class Readconfig:
    @staticmethod
    def getapplicationurl():
        url=(config.get('commonInfo','baseurl'))
        return url

    @staticmethod
    def getuseremail():
        username=config.get('commonInfo','email')
        return username

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password
