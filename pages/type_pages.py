# coding=utf-8
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
import time

class TypePages(BasePage):
    book_gaparent_path = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div")
    book_parent_path = (By.XPATH, "/html/body/div[2]/ul/div[1]")
    book_type_path=(By.XPATH,'/html/body/div[2]/ul/div/li/div[2]/ul/div[2]')
    # "//*[@id="pane-list"]/div/div[1]/div[1]/button[1]"
    add_head_type_path=(By.XPATH,'//div[@class="tb-left"]/button[1]')

    add_head_type_name_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[1]/div[2]/div/div/div/input')
    add_head_type_itemno_path = (By.XPATH, '//*[@id="pane-top"]/div/form/div[2]/div[1]/div/div/div[1]/input')
    add_head_type_name_sx_path = (By.XPATH, '//*[@id="pane-top"]/div/form/div[2]/div[2]/div/div/div[1]/input')
    add_head_type_category_path = (By.XPATH, '//*[@id="pane-top"]/div/form/div[3]/div/div/div/div/div[1]/input')
    category_select_path=(By.XPATH,'//ul[contains(@class,"el-cascader-menu__list")]/li[1]/label/span/span')

    add_head_type_skin_path=(By.XPATH,"//*[@id='pane-top']/div/form/div[6]/div/div/div/div/div")
    skin_select_path=(By.XPATH,"//ul[contains(@class,'el-select-dropdown__list')]/li[1]")

    add_head_app_pic_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[5]/div[1]/div/div/div/div[1]')
    add_head_pc_pic_path = (By.XPATH, '//*[@id="pane-top"]/div/form/div[5]/div[2]/div/div/div/div[1]/div')

    add_head_app_pic_input_path = (By.XPATH, '//*[@id="pane-top"]/div/form/div[5]/div[1]/div/div/div/div[1]/div/input')
    add_head_pc_pic_input_path=(By.XPATH,'//*[@id="pane-top"]/div/form/div[5]/div[2]/div/div/div/div[1]/div/input')

    def skin_to(self):
        time.sleep(1)
        self.move_to_element(self.book_gaparent_path)
        time.sleep(1)
        self.move_to_element(self.book_parent_path)
        time.sleep(1)
        self.click(self.book_type_path)

    def add_head_type(self,name,item_no,abbreviate_name,):
        time.sleep(2)
        self.click(self.add_head_type_path)
        time.sleep(1)
        self.send_key(self.add_head_type_name_path,name)
        self.send_key(self.add_head_type_itemno_path,item_no)
        self.send_key(self.add_head_type_name_sx_path,abbreviate_name)
        self.click(self.add_head_type_category_path)
        self.click(self.category_select_path)
        self.click(self.add_head_type_name_path)
        self.click(self.add_head_type_skin_path)
        self.click(self.skin_select_path)

        time.sleep(10)

#上传问题没有办法解决，目前
    def upload_pic_type(self):
        # self.click(self.add_head_app_pic_path)
        self.send_key(self.add_head_app_pic_input_path,"/Users/juanjuan/Downloads/ss.jpg ")
        time.sleep(2)




