# coding=utf-8

from pages.login_pages import LoginPage
from utils.base_utils import root_path,get_config_value
import pytest
from selenium import webdriver
from utils.driver_utils import Driver
import time
class TestLogin(object):

    @classmethod
    def setup_class(self):
        url=get_config_value("Brower","url")
        brower_driver=Driver()
        self.driver: webdriver=brower_driver.open_brower()
        self.driver.get(url)
    @pytest.mark.run(order=1)
    def test_login(self):
        user_name=get_config_value("Account","username")
        password=get_config_value("Account","password")
        login = LoginPage(self.driver)
        login.login(user_name, password)


    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

if __name__=="__main__":
    pytest.main(['-s', 'test_login.py'])