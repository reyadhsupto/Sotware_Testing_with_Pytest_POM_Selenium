import configparser
import os

directory = r"E:\Internship\SDET_selenium\Sotware_Testing_with_Pytest_POM_Selenium\Configurations"
filename = "config.ini"

# Construct the full file path
full_path = os.path.join(directory, filename)

# Normalize the path
normalized_path = os.path.normpath(full_path)

config = configparser.RawConfigParser()
config.read(normalized_path)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password