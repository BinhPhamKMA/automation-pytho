import pytest
from selenium import webdriver
from time import sleep
from utils.read_config import  ConfigReader
class BaseTest:
    def __init__(self):
        self.drive = None

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, request):
        self.drive = webdriver.Chrome()
        self.drive.maximize_window()
        self.drive.get(ConfigReader.get_base_url())
        self.drive.implicitly_wait(20)
        yield
        self.drive.quit()





