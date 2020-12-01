#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import allure
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from utils.Logger import logger
from utils.base_utils import root_path
from unittest import TestCase


class BasePage(object):
    path = root_path

    def __init__(self, driver):
        """
        :param driver:打开浏览器驱动
        """
        self.driver: WebDriver = driver
        self.accept_next_alert = True
        self.case = TestCase()
        self.time_out = 10

    def open_url(self, url):
        logger.info("浏览器打开链接：%s" % url)
        self.driver.get(url)

    def get_title(self):
        logger.info("当前页面的title为: %s" % self.driver.title)
        return self.driver.title

    def find_element(self, *locator):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            element = WebDriverWait(self.driver, self.time_out, 0.5).until(EC.visibility_of_element_located(locator))
            return element
        except NoSuchElementException:
            logger.error('Can not find element: %s' % locator[1])
            self.get_screen_img()
            raise
        except TimeoutException:
            logger.error('Can not find element: %s' % locator[1])
            self.get_screen_img()
            raise
        except Exception as e:
            logger.error('Can not find element: %s, exception is: %s' % (locator[1], e))
            self.get_screen_img()
            raise

    def find_elements(self, *locator):
        try:
            # 查找元素组, 入参为元组的元素，需要加*
            elements = WebDriverWait(self.driver, self.time_out, 0.5).until(
                lambda driver: driver.find_elements(*locator))
            return elements
        except NoSuchElementException:
            logger.error('Can not find elements: %s' % locator[1])
            self.get_screen_img()
            raise
        except TimeoutException:
            logger.error('Can not find elements: %s' % locator[1])
            self.get_screen_img()
            raise
        except Exception as e:
            logger.error('Can not find elements: %s, exception is: %s' % (locator[1], e))
            self.get_screen_img()
            raise

    def get_screen_img(self):
        """将页面截图下来"""
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        screen_name = os.path.join(self.path, 'screenshots', now + '.png')
        try:
            self.driver.get_screenshot_as_file(screen_name)
            allure.attach.file(screen_name, attachment_type=allure.attachment_type.PNG)
            logger.info("页面已截图，截图的路径为: %s" % screen_name)
        except Exception as e:
            logger.error("失败截图 %s" % e)

    def click(self, locator):
        logger.info('Click element by %s: %s...' % (locator[0], locator[1]))
        try:
            element = self.find_element(*locator)
            element.click()
        except Exception as e:
            logger.error("无法点击元素: %s" % e)
            self.get_screen_img()
            raise

    def clear(self, locator):
        """输入文本框清空操作"""
        element = self.find_element(*locator)
        try:
            element.clear()
            logger.info('清空文本框内容')
        except Exception as ne:
            logger.error("Failed to clear in input box with %s" % ne)
            self.get_screen_img()
            raise

    def send_key(self, locator, text):
        logger.info('Input element by %s: %s...' % (locator[0], locator[1]))
        logger.info('Input: %s' % text)
        try:
            element = self.find_element(*locator)
            element.send_keys(text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_screen_img()
            raise

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        Usage:
        element = ("id","xxx")
        driver.move_to_element(element)
        """
        try:
            element = self.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def move_loc_from_to(self, source, target):
        try:
            ele_source = self.find_element(*source)
            ele_target = self.find_element(*target)
            ActionChains(self.driver).drag_and_drop(ele_source, ele_target).perform()
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def move_element_from_to(self, ele_source, ele_target):
        try:
            ActionChains(self.driver).drag_and_drop(ele_source, ele_target).perform()
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def back(self):
        """
        浏览器返回窗口
        """
        self.driver.back()
        logger.info('返回上一个页面')

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        self.driver.forward()
        logger.info('前进到下一个页面')

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    @staticmethod
    def sleep(seconds=2):
        time.sleep(seconds)
        logger.info("等待 %d 秒" % seconds)

    def close(self):
        """
        关闭浏览器
        """
        try:
            self.driver.close()
            logger.info('关闭浏览器窗口')
        except Exception as e:
            logger.error("关闭浏览器窗口失败 %s" % e)

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()

    def get_url(self):
        """获取当前的url"""
        return self.driver.current_url

    def get_text(self, locator):
        """获取文本"""
        try:
            element = self.find_element(*locator)
            return element.text
        except AttributeError as e:
            logger.error(e)
            self.get_screen_img()
            raise

    def get_attribute(self, locator, name):
        """获取属性"""
        try:
            element = self.find_element(*locator)
            return element.get_attribute(name)
        except AttributeError as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def js_execute(self, js):
        """执行js"""
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        """通过索引,index是索引第几个，从0开始"""
        try:
            element = self.find_element(*locator)
            Select(element).select_by_index(index)
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def select_by_value(self, locator, value):
        """通过value属性"""
        try:
            element = self.find_element(*locator)
            Select(element).select_by_value(value)
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise e

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        try:
            element = self.find_element(*locator)
            Select(element).select_by_value(text)
        except Exception as e:
            logger.info(e)
            self.get_screen_img()
            raise

    def is_text_in_element(self, locator, text, timeout=10):
        """判断文本在元素里，没定位到元素返回False，定位到元素返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            logger.info("元素没有定位到:" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            logger.info("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        """判断title完全等于"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        """判断title包含"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        """判断元素被选中，返回布尔值,"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(
            EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        """判断元素的状态，selected是期望的参数true/False
        返回布尔值"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        """判断页面是否有alert，
        有返回alert(注意这里是返回alert,不是True)
        没有返回False"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(EC.alert_is_present())
        return result

    def alert_accept(self):
        """接受alert"""
        try:
            alert = self.driver.switch_to_alert()
            logger.info(alert.text)
            alert.accept()
        except UnexpectedAlertPresentException as e:
            print(e)
        except NoAlertPresentException as e1:
            print(e1)

    def is_visibility(self, locator, timeout=10):
        try:
            """元素可见返回本身，不可见返回Fasle"""
            result = WebDriverWait(self.driver, timeout, 0.5).until(
                EC.visibility_of_element_located(locator))
            return result
        except TimeoutException as e:
            logger.info(e)

    def is_invisibility(self, locator, timeout=10):
        """元素可见返回False，不可见返回True，没找到元素也返回True"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(
            EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        """元素可以点击is_enabled返回本身，不可点击返回False"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        """判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False"""
        result = WebDriverWait(self.driver, timeout, 0.5).until(
            EC.presence_of_element_located(locator))
        return result

    def set_element_wait(self, wait_time, locator):
        WebDriverWait(self.driver, wait_time, 0.5).until(EC.presence_of_element_located(locator))

    def upload_file(self, locator, file_path):
        """上传文件"""
        try:
            self.find_element(*locator).send_keys(file_path)
            time.sleep(1)
        except Exception as e:
            logger.error("Failed to upload file %s" % e)
            self.get_screen_img()

    def switch_handle(self, title_name):
        """根据窗口title切换窗口"""
        all_handles = self.driver.window_handles()
        for handle in all_handles:
            if self.driver.title.find(title_name) == -1:
                self.driver.switch_to_window(handle)
            else:
                print("Can't find the handle")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            logger.error("Element is not present. %s" % e)
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def get_attribute_text(self, locator):
        try:
            text_content = self.find_element(*locator).get_attribute('textContent')
        except Exception as e:
            logger.error("Failed to upload file %s" % e)
            text_content = ''
            self.get_screen_img()
        return text_content

    def get_screenshot(self, case_name):
        """screen shot"""
        file_path = os.path.join(root_path, 'screenshots', case_name + '.png')
        self.driver.get_screenshot_as_file(file_path)
        allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG)
        logger.info("Screen shot had been saved: %s" % file_path)
        return file_path

    @staticmethod
    def get_current_time():
        temp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        return temp

    def verify_true(self, expr, msg=None):
        try:
            self.case.assertTrue(expr, msg)
        except Exception as e:
            self.get_screen_img()
            raise e

    def verify_in(self, member, container, msg=None):
        try:
            self.case.assertIn(member, container, msg)
        except Exception as e:
            self.get_screen_img()
            raise e
