#coding=utf-8
from time import sleep
import unittest,random,sys
sys.path.append(".models")
sys.path.append("./Yige_page_obj")
from Yige_page_obj.loginPage import login
from models import myunit, function

class loginTest(myunit.MyTest):
    '''社区登陆测试'''
    #测试用户登录
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)
    def test_login1(self):
        '''用户名、密码为空登陆'''
        self.user_login_verify()
        po=login(self.driver)
        self.assertEqual(po.user_error_hint(),"请填写手机号码！")
        #self.assertEqual(po.pawd_error_hint(),"请填写登陆密码！")
        function.insert_img(self.driver,"user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名正确，密码为空登陆'''
        self.user_login_verify(username="18007551879")
        po =login(self.driver)
        self.assertEqual(po.pawd_error_hint(),"请填写登录密码！")
        function.insert_img(self.driver,"pawd_empty.jpg")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password="888888")
        po =login(self.driver)
        self.assertEqual(po.user_error_hint(),"请填写手机号码！")
        function.insert_img(self.driver,"user_empty.jpg")
    def test_login4(self):
        '''用户名与密码不匹配'''
        character=random.choice('abcdefghijklmnopqrstuvwxyz')
        Password="12345"+character
        self.user_login_verify(username='18007551879',password=Password)
        po =login(self.driver)
        self.assertEqual(po.pawd_wrong_hint(),"密码不正确")
        function.insert_img(self.driver,"user_pawd_error.jpg")
    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username="18007551879",password='888888')
        sleep(2)
        po=login(self.driver)
        self.assertEqual(po.user_login_success(),'请确认要登录的企业')
        function.insert_img(self.driver,"use"
                                        "r_pawd_ture.jpg")

if __name__== "__main__":
    unittest.main()