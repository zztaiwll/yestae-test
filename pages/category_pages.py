# coding=utf-8
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
import time


class CategoryPage(BasePage):
    book_gaparent_path=(By.XPATH,"//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div")
    book_parent_path=(By.XPATH,"/html/body/div[2]/ul/div[1]")
    book_category_path=(By.XPATH,"/html/body/div[2]/ul/div[1]/li/div[2]/ul/div[1]")

    category_add_head_path=(By.XPATH,'//*[@id="pane-list"]/div/div[1]/div[1]/button[1]')
    category_add_next_path=(By.XPATH,'//*[@id="pane-list"]/div/div[1]/div[1]/button[2]')
    category_update_path = (By.XPATH,'//*[@id="pane-list"]/div/div[1]/div[1]/button[3]')
    category_del_path = (By.XPATH,'//*[@id="pane-list"]/div/div[1]/div[1]/button[4]')

    category_parent_checkbox_path=(By.XPATH,'//*[@id="pane-list"]/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div')
    category_child_checkbox_path = (By.XPATH,'//*[@id="pane-list"]/div/div[2]/div/div/div[3]/table/tbody/tr[2]/td[1]/div')
    category_checkbox_path=(By.XPATH,'//*[@id="pane-list"]/div/div[2]/div/div/div[3]/table/tbody/tr[3]/td[1]/div')

    category_add_name_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[2]/div/div[1]/input')
    category_add_item_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[3]/div/div[1]/input')
    category_add_order_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[4]/div/div/input')
    category_add_button=(By.XPATH,'//*[@id="pane-top"]/div/div/button[2]')

    category_add_child_name_path=(By.XPATH,'//*[@id="pane-subset"]/div/form/div[2]/div/div[1]/input')
    category_add_child_item_path = (By.XPATH, '//*[@id="pane-subset"]/div/form/div[3]/div/div[1]/input')
    category_add_child_order_path = (By.XPATH, '//*[@id="pane-subset"]/div/form/div[4]/div/div/input')
    category_add_child_button_path = (By.XPATH, '//*[@id="pane-subset"]/div/div[1]/button[2]')

    category_update_name=(By.XPATH,'//div[starts-with(@id,"pane-edit")]/div/form/div[2]/div/div/input')
    category_update_item=(By.XPATH,'//div[starts-with(@id,"pane-edit")]/div/form/div[3]/div/div/input')
    category_update_order_path=(By.XPATH,'//div[starts-with(@id,"pane-edit")]/div/form/div[4]/div/div/input')
    categort_update_button=(By.XPATH,'//div[starts-with(@id,"pane-edit")]/div/div[1]/button[2]')

    button_accept_path=(By.XPATH,'//div[@class="el-message-box__btns"]/button[2]')
    conf_attr_path=(By.XPATH,'//table[@class="el-table__body"]/tbody/tr/td[6]/div/button[1]')
    attr_path1=(By.XPATH,"//input[@class='el-checkbox__original'][1]")
    attr_path2 = (By.XPATH, "//input[@class='el-checkbox__original'][2]")
    attr_path3 = (By.XPATH, "//input[@class='el-checkbox__original'][3]")

    attr_relative_button_path=(By.XPATH,"//button//span[contains(text(), '关联')]")
    attr_save_button_path = (By.XPATH, "//button//span[contains(text(), '保存')]")
    def skin(self):
        self.move_to_element(self.book_gaparent_path)
        self.move_to_element(self.book_parent_path)
        self.click(self.book_category_path)

    def add_head_category(self,name,item,order):
        self.click(self.category_add_head_path)
        self.driver.implicitly_wait(10)

        self.clear(self.category_add_name_path)
        self.send_key(self.category_add_name_path,name)

        self.clear(self.category_add_item_path)
        self.send_key(self.category_add_item_path, item)

        self.clear(self.category_add_order_path)
        self.send_key(self.category_add_order_path, order)

        self.click(self.category_add_button)


    def add_parent_category(self,name,item,order):
        self.click(self.category_parent_checkbox_path)

        self.click(self.category_add_next_path)

        self.clear(self.category_add_child_name_path)
        self.send_key(self.category_add_child_name_path, name)

        self.clear(self.category_add_child_item_path)
        self.send_key(self.category_add_child_item_path, item)

        self.clear(self.category_add_child_order_path)
        self.send_key(self.category_add_child_order_path, order)

        self.click(self.category_add_child_button_path)

    def add_child_category(self,name,item,order):
        self.click(self.category_child_checkbox_path)

        self.click(self.category_add_next_path)

        self.clear(self.category_add_child_name_path)
        self.send_key(self.category_add_child_name_path, name)

        self.clear(self.category_add_child_item_path)
        self.send_key(self.category_add_child_item_path, item)

        self.clear(self.category_add_child_order_path)
        self.send_key(self.category_add_child_order_path, order)

        self.click(self.category_add_child_button_path)

    def update_category(self,name,item,order):
      self.click(self.category_checkbox_path)

      self.click(self.category_update_path)

      self.clear(self.category_update_name)
      self.send_key(self.category_update_name, name)

      self.clear(self.category_update_item)
      self.send_key(self.category_update_item, item)

      self.clear(self.category_update_order_path)
      self.send_key(self.category_update_order_path, order)

      self.click(self.categort_update_button)

    def dele_category(self):
        time.sleep(2)
        self.click(self.category_checkbox_path)
        self.click(self.category_del_path)
        self.click(self.button_accept_path)
        time.sleep(2)
        self.click(self.category_child_checkbox_path)
        self.click(self.category_del_path)
        self.click(self.button_accept_path)
        time.sleep(2)
        self.click(self.category_parent_checkbox_path)
        self.click(self.category_del_path)
        self.click(self.button_accept_path)
        time.sleep(2)

    def conf_attr(self):
        self.click(self.conf_attr_path)

        self.click(self.attr_path1)

        self.click(self.attr_path2)

        self.click(self.attr_path3)

        self.click(self.attr_relative_button_path)
        time.sleep(2)

        self.click(self.attr_save_button_path)













