from utils.driver_utils import Driver
from pages.login_pages import LoginPage
from pages.category_pages import CategoryPage
from utils.base_utils import root_path,get_config_value
import pytest
from selenium import webdriver
import time
class TestCategory(object):

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

    def test_category(self):
        category=CategoryPage(self.driver)
        category.skin()
        # category.add_head_category("zzt-pytest-gaparent",1001,1)
        # time.sleep(2)
        #
        # category.add_parent_category("zzt-pytest-parent",1001001,1)
        # time.sleep(2)
        #
        # category.add_child_category("zzt-pytest",1001001001,1)
        # time.sleep(2)
        #
        # category.update_category("zzt-pytest-01",1001001001,1)
        # time.sleep(2)
        #
        # category.dele_category()
        category.conf_attr()

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

if __name__=="__main__":
    pytest.main(['-s', 'test_category.py'])