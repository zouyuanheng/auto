#coding=utf-8
from time import sleep
import unittest,random,sys
sys.path.append(".models")
sys.path.append("./Yige_page_obj")
from Yige_page_obj.registerPage import register
from models import myunit, function

class registerTest(myunit.MyTest):
    def user_register_verify(self,companyUserPhone="",imageCode="",companyPhoneCode="",password=""):
        register(self.driver).user_register(companyUserPhone,imageCode,companyPhoneCode,password)
    def test_register1(self):
        '''填写正确的信息注册'''
        self.user_register_verify(companyUserPhone='',imageCode='',companyPhoneCode='',password='')
        sleep(2)
        po=register(self.driver)
        self.assertEqual(po.user_register_success(),'请选择您的角色')
        function.insert_img(self.driver,"register_ture.jpg")

if __name__== "__main__":
    unittest.main()