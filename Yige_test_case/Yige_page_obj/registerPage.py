#coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class register(Page):
   '''
   用户注册页面
   '''
   url='/'
   #Action
   #请输入你的手机号码输入框
   Yige_register_tel_loc=(By.NAME,"tel")
   #立即体验按钮
   Yige_register_exp_btn=(By.CSS_SELECTOR,"css=button.btn.btn-info")
   Yige_register_regiseter_btn=(By.XPATH,'//*[@id="registerBtn"]')
   #手机号
   Yige_register_companyUserPhone_loc=(By.ID,"companyUserPhone")
   '''
   验证码后面需要处理
   '''
   #验证码
   Yige_register_imageCode_loc=(By.ID,"imageCode")
   #获取验证码按钮
   Yige_register_getPhoneCode_btn=(By.ID,"getPhoneCode")
   #短信验证码按钮
   Yige_register_companyPhoneCode_loc=(By.ID,"companyPhoneCode")
   #设置密码输入框
   Yige_register_password_loc=(By.ID,"password")
   #注册按钮
   Yige_register_nextStep2_btn=(By.ID,"nextStep2")

   def Yige_register(self):
      self.find_element(*self.Yige_register_exp_btn).click()
      sleep(2)
      self.find_element(*self.Yige_register_regiseter_btn)
      sleep(2)
   #填写注册用手机号
   def register_companyUserPhone(self,companyUserPhone):
      self.find_element(*self.Yige_register_companyUserPhone_loc).send_keys(companyUserPhone)
   #填写注册用验证码
   def register_imageCode(self,imageCode):
      self.find_element(*self.Yige_register_imageCode_loc).send_keys(imageCode)
   #点击获取验证码
   def register_getPhoneCode(self):
      self.find_element(*self.Yige_register_getPhoneCode_btn).click()
   #填写注册用手机验证码
   def register_companyPhoneCode(self,companyPhoneCode):
      self.find_element(*self.Yige_register_companyPhoneCode_loc).send_keys(companyPhoneCode)
   #填写注册用密码
   def register_password(self,password):
      self.find_element(*self.Yige_register_password_loc).send_keys(password)
   #注册按钮
   def register_nextStep2(self):
      self.find_element(*self.Yige_register_nextStep2_btn).click()
   #定义正常注册流程
   '''
   imageCode和companyPhoneCode是动态的解决需要考虑
   '''
   def user_register(self,companyUserPhone="17727854261",imageCode="",companyPhoneCode="",password="mMa4t!n*"):
      self.open()
      self.Yige_register()
      self.register_companyUserPhone(companyUserPhone)
      self.register_imageCode(imageCode)
      self.register_companyPhoneCode(companyPhoneCode)
      self.register_password(password)
      self.register_nextStep2()

   companyUserPhone_error_hint_loc=()
   companyUserPhone_wrong_hint_loc=()
   imageCode_error_hint_loc=()
   imageCode_wrong_hint_loc=()
   companyPhoneCode_error_hint_loc=()
   companyPhoneCode_wrong_hint_loc=()
   password_error_hint_loc=()
   password_wrong_hint_loc=()
   nextStep2_error_hint_loc=()
   user_register_success_loc=(By.XPATH,'//*[@id="selectPart"]/div[1]/div')
   #用户注册成功流程
   def user_register_success(self):
      return self.find_element(*self.user_register_success_loc).text