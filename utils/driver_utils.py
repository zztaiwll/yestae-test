# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.Logger import logger
import platform
from utils.base_utils import get_config_value
import os
from utils.base_utils import root_path

class Driver(object):
    system_name = platform.system()
    logger.info("当前系统为" + system_name)
    browser = get_config_value('BrowserType', 'browserName')
    logger.info("选择的浏览器为: %s 浏览器" % browser)
    chrome_driver_path = os.path.join(root_path, 'driver', 'chromedriver')

    def open_brower(self):
        options = Options()
        driver = webdriver.Chrome(self.chrome_driver_path, options=options)
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(10)
        return driver
