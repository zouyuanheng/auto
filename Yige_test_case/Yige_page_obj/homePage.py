#coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class home(Page):
    '''首页（一格网介绍）'''
    url= '/'
    #Action
    Yige_home_tel_loc=(By.NAME,"tel")
    Yige_home_experience_btn=(By.XPATH,'//*[@id="fullpage"]/div[1]/div/div[4]/form/div/button')
    Yige_home_down_btn=(By.XPATH,'//*[@id="s2"]/img')
    Yige_home_function_btn=(By.LINK_TEXT,'功能')
    Yige_home_dynamic_btn=(By.LINK_TEXT,'动态')
    Yige_home_help_btn=(By.LINK_TEXT,'帮助')
    Yige_home_our_btn=(By.LINK_TEXT,'我们')
    Yige_home_register_btn=(By.XPATH,'//*[@id="navbar-menu"]/ul/li[7]/a')
    Yige_home_login_btn=(By.XPATH,'//*[@id="navbar-menu"]/ul/li[8]/a')

    #请输入您的手机号
    def home_userphone(self,userphone):
        self.find_element(*self.Yige_home_tel_loc).send_keys(userphone)
    #立即体验按钮
    def home_expClick(self):
        self.find_element(*self.Yige_home_experience_btn).click()
    #正确的立即体验流程
    def user_experience(self,userphone):
        self.home_userphone(userphone)
        self.home_expClick()
        sleep(1)
    #点击向下翻页按钮
    def home_down(self):
        self.find_element(*self.Yige_home_down_btn).click()
    #点击“功能”按钮
    def home_function(self):
        self.find_element(*self.Yige_home_function_btn).click()
    #用户访问“功能”页流程
    def user_function(self):
        self.home_down()
        self.home_function()
        sleep(1)
    #点击“动态”按钮
    def home_dynamic(self):
        self.find_element(*self.Yige_home_dynamic_btn).click()
    #用户访问“动态”页流程
    def user_dynamic(self):
        self.home_down()
        self.home_dynamic()
        sleep(1)
    #点击“帮助”按钮
    def home_help(self):
        self.find_element(*self.Yige_home_help_btn).click()
    #用户访问“帮助”页流程
    def user_help(self):
        self.home_down()
        self.home_help()
        sleep(1)
    #点击“我们”按钮
    def home_our(self):
        self.find_element(*self.Yige_home_our_btn).click()
    #用户访问“我们”页流程
    def user_our(self):
        self.home_down()
        self.home_our()
        sleep(1)
    def home_register(self):
        self.find_element(*self.Yige_home_register_btn).click()
    def user_down_register(self):
    #用户点击首页“免费注册”按钮，user和login页里面的userregister
        self.home_down()
        self.home_register()

        sleep(1)
    def home_login(self):
        self.find_element(*self.Yige_home_login_btn).click()
    def user_down_login(self):
    #用户点击首页“登陆”按钮
        self.home_down()
        self.home_login()
        sleep(1)


    userphone_experience_success_loc=(By.ID,"id=companyUserPhone")
    down_function_success_loc=(By.XPATH,'//*[@id="organization"]/div/div[1]/h2')
    down_dynamic_success_loc=(By.XPATH,'//*[@id="hbaner"]/div/ul/li[1]/a')
    down_help_success_loc=(By.XPATH,'//*[@id="hbaner"]/div/ul/li[1]/a')
    down_our_success_loc=(By.XPATH,'/html/body/div/h4[1]')
    down_serviceTel_success_loc=(By.XPATH,'//*[@id="navbar-menu"]/ul/li[6]/a')
    down_register_success_loc=(By.XPATH,'//*[@id="nextStep2"]')
    down_login_success_loc=(By.XPATH,'//*[@id="loginBtn"]')


    #注册页显示的手机号
    def userphone_experience_success(self):
        return self.find_element(*self.userphone_experience_success_loc).text
    #功能页“人员组织”文本
    def down_function_success(self):
        return self.find_element(*self.down_function_success_loc).text
    #动态页“版本更新”文本
    def down_dunamic_success(self):
        return self.find_element(*self.down_dynamic_success_loc).text
    #帮助页“供企业管理者使用”文本
    def down_help_success(self):
        return self.find_element(*self.down_help_success_loc).text
    #我们页“公司介绍”文本
    def down_our_success(self):
        return self.find_element(*self.down_our_success_loc).text
    #首页“客服电话”文本
    def down_serviceTel_success(self):
        return self.find_element(*self.down_serviceTel_loc).text
    #注册页“注册”按钮的文本
    def down_register_success(self):
        return self.find_element(*self.down_register_success_loc).text
    #登陆页“登陆”按钮的文本
    def down_login_success(self):
        return self.find_element(*self.down_login_success_loc).text