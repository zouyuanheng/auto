#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class staff(Page):
    '''
    员工管理页面
    '''
    url='/'
    #actiong
    Yige_staff_choice_DW_btn=(By.XPATH,'//*[@id="dg-container"]/nav/div[1]/img')
    Yige_staff_affirm_DW_btn=(By.XPATH,'//*[@id="loginBtn2"]')
    Yige_staff_staff_btn=(By.XPATH,'//*[@id="F020000"]/a')
    Yige_staff_psnRecord_btn=(By.XPATH,'//*[@id="F020800"]')
    Yige_staff_oznChart_btn=(By.XPATH,'//*[@id="F021000"]')
    Yige_staff_onJob_btn=(By.XPATH,'/html/body/div[1]/div[1]/div/div/ul/li[1]/a')
    Yige_staff_leftOffice_btn=(By.XPATH,'/html/body/div[1]/div[1]/div/div/ul/li[2]/a')
    Yige_staff_entering_btn=(By.XPATH,'//*[@id="divOnPayroll"]/div[1]/div[1]/div/button')
    Yige_staff_export_btn=(By.XPATH,'//*[@id="divOnPayroll"]/div[1]/div[1]/button')

    #选择DW
    def staff_choice_DW(self):
        self.find_element(*self.Yige_staff_choice_DW_btn).click()

    #选择公司页确认
    def staff_affirm_DW(self):
        self.find_element(*self.Yige_staff_affirm_DW_btn).click()

    #登陆到工作台
    def staff_login_platform(self):
        self.staff_choice_DW()
        sleep(1)
        self.staff_affirm_DW()
        sleep(1)
    #访问“员工”模块
    def staff_platform_staff(self):
        self.find_element(*self.Yige_staff_staff_btn).click()
    #访问人事办理记录
    def staff_psnRecord(self):
        self.find_element(*self.Yige_staff_psnRecord_btn).click()

    #访问组织架构
    #访问在职人员列表
    #访问离职人员列表
    #单个录入员工
    #批量录入员工