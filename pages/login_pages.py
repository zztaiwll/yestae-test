# coding=utf-8
from poium import Page,PageElement,PageElements


class LoginPage(Page):
    user_name_path='//input[@name="userName"]'
    password_path = '//input[@name="password"]'
    button_path="//*[@id='app']/div/div/div[1]/div[2]/form/button"

    username = PageElement(xpath=user_name_path, describe="用户名")
    password = PageElement(xpath=password_path, describe="密码")
    button = PageElement(xpath=button_path, describe="登陆")
    def login(self,username_value,password_value):
        self.username.clear()
        self.username.send_keys(username_value)

        self.password.clear()
        self.password.send_keys(password_value)

        self.button.click()
