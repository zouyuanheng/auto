#coding=utf-8
'''import MySQLdb'''
from selenium.webdriver.support.ui import Select
'''
Projet:
这是“base”模块，提供了一个名为Page()的函数，这个函数的作用是
页面基础类，用于所有页面的继承
Author:
邹沅恒
history:
2017.3.3  版本1

class mysqldelete():
#每次测试注册功能的时候要去数据库删除已经注册的用户信息
 conn=MySQLdb.connect(host='testyigewango.mysql.rds.aliyuncs.com',user='root',passwd='password',db='rm_yang',port=3306)
 cur=conn.cursor()

 vars = cur.execute("select * from bussiness_account where member_id = '10987385' ")
    print vars
    result=cur.fetchone()
    print result
    cur.close()
    conn.close()
 def deleteuser(s/elf):
     self.cur.execute("DELETE from common_user where MOBILE_NO = '18565737457'")
     self.conn.commit()
     self.cur.execute("DELETE from base_user where MOBILE_NO = '18565737457'")
     self.conn.commit()
     self.cur.close()
     self.conn.close()
'''
class Page (object):

    Yige_url='https://test.yigewang.com.cn/#1'
    #设置测试初始访问地址

    def __init__(self,selenium_driver,base_url=Yige_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30
        self.parent=parent
    #初始化url、驱动、超时时间

    def _open(self,url):
        url=self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url
    #设置断言：浏览器当前访问的页面是不是初始化地址方法

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    #设置查找元素方法

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    #设置查找元素集方法

    def open(self):
        self._open(self.url)
    #设置打开浏览器方法

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self,src):
        return self.driver.execute_script(src)