#coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    '''
    用户登录页面
    '''
    url= '/'
    #Action
    Yige_login_tel_loc=(By.NAME,"tel")
    Yige_login_experience_btn=(By.XPATH,'//*[@id="fullpage"]/div[1]/div/div[4]/form/div/button')
    Yige_login_login_btn=(By.ID,'goLogin')

    def Yige_login(self):
        self.find_element(*self.Yige_login_experience_btn).click()
        sleep(2)
        self.find_element(*self.Yige_login_login_btn).click()
        sleep(2)

    login_username_loc=(By.ID,"userId")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.ID,"loginBtn")

    #登陆用户名
    def login_username(self,username):
         self.find_element(*self.login_username_loc).send_keys(username)
    #登陆密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    #登陆按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
    #定义统一登陆入口
    def user_login(self,username="18007551879",password="888888"):
        """获取的用户名密码登录"""
        self.open()
        self.Yige_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
    user_error_hint_loc=(By.ID,"loginErr")
    pawd_error_hint_loc=(By.ID,"loginErr")
    user_login_success_loc=(By.XPATH,'//*[@id="selectPart"]/div[1]/div')
    pawd_wrong_hint_loc=(By.ID,"msg")
    #用户名为空错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text
    #密码为空错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text
    #密码错误提示
    def pawd_wrong_hint(self):
        return self.find_element(*self.pawd_wrong_hint_loc).text
    #登陆成功用户名
    def user_login_success(self):
        return self.find_element(*self.usezr_login_success_loc).text