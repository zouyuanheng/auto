#coding=utf-8
from time import sleep
import unittest,random,sys
sys.path.append(".models")
sys.path.append("./Yige_page_obj")
from models import myunit, function
from Yige_page_obj.loginPage import login
from Yige_page_obj.staffPage import staff

class staffTest(myunit.MyTest):
    def test_staff(self):
         login(self.driver).user_login()
         sleep(2)
         staff(self.driver).staff_login_platform()






if __name__== "__main__":
    unittest.main()