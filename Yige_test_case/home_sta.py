#coding=utf-8
from time import sleep
import unittest,random,sys
sys.path.append(".models")
sys.path.append("./Yige_page_obj")
from Yige_page_obj.homePage import home
from models import myunit, function

class homeTest(myunit.MyTest):
    def user_experience_verify(self,userphone=''):
        home(self.driver).user_experience(userphone)
    def test_home1(self):
        '''填写手机号点击立即体验'''
        self.user_experience_verify(userphone='18565737457')
        po=home(self.driver)
        self.assertEqual(po.userphone_experience_success(),'18565737457')
        function.insert_img(self.driver,'user_experience_ture')
    def test_home2(self):
        '''不填写手机号点击立即体验'''
        self.user_experience_verify()
        po=home(self.driver)
        self.assertEqual(po.userphone_experience_success(),"")
        function.insert_img(self.driver,"user_experience_empty_ture")
    def user_home_function(self):
        home(self.driver).user_function()
    def test_home3(self):
        '''首页“功能”按钮跳转功能'''
        self.user_home_function()
        po=home(self.driver)
        self.assertEqual(po.down_function_success(),"人员组织")
    def user_home_dynamic(self):
        home(self.driver).user_dynamic()
    def test_home4(self):
        '''首页“动态”按钮跳转功能'''
        self.user_home_dynamic()
        po=home(self.driver)
        self.assertEqual(po.down_dunamic_success(),"版本更新")
    def user_home_help(self):
        home(self.driver).user_help()
    def test_home5(self):
        '''首页“帮助”按钮跳转功能'''
        self.user_home_help()
        po=home(self.driver)
        self.assertEqual(po.down_help_success(),"企业管理者使用")
    def user_home_our(self):
        home(self.driver).user_our()
    def test_home6(self):
        '''首页“我们”按钮跳转功能'''
        self.user_home_our()
        po=home(self.driver)
        self.assertEqual(po.down_our_success(),"公司介绍")
    def user_home_serviceTel(self):
        home(self.driver).home_down()
    def test_home7(self):
        '''首页“客服电话”文本的显示'''
        self.user_home_serviceTel()
        po=home(self.driver)
        self.assertEqual(po.down_serviceTel_success(),"客服电话：400-991-0601")
    def user_home_register(self):
        home(self.driver).user_down_register()
    def test_home8(self):
        self.user_home_register(self)
        po=home(self.driver)
        self.assertEqual(po.down_register_success(),"注册")
        sleep(1)
    def user_home_login(self):
        home(self.driver).user_down_login()
    def test_home9(self):
        self.user_home_login()
        po=home(self.driver)
        self.assertEqual(po.down_login_success_loc,"登陆")
        sleep(1)

if __name__== "__main__":
    unittest.main()