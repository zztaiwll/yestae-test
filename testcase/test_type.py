# coding=utf-8
from utils.driver_utils import Driver
from pages.login_pages import LoginPage
from pages.type_pages import TypePages
from utils.base_utils import root_path,get_config_value
import pytest
from selenium import webdriver
import time

class TestType(object):
    @classmethod
    def setup_class(self):
        url = get_config_value("Brower", "url")
        brower_driver = Driver()

        self.driver: webdriver = brower_driver.open_brower()
        self.driver.get(url)
        user_name = get_config_value("Account", "username")
        password = get_config_value("Account", "password")
        login = LoginPage(self.driver)
        login.login(user_name, password)

    def test_skin(self):
        type=TypePages(self.driver)
        print("11111")
        print("11111")
        type.skin_to()
        type.add_head_type("zzt-auto test","12001","auto_test")

    # @classmethod
    # def teardown_class(cls):
    #     time.sleep(2)
    #     cls.driver.close()
    #     cls.driver.quit()

if __name__=="__main__":
    pytest.main(['-s', 'test_type.py'])