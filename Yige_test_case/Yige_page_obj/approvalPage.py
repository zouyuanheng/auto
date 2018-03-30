#coding=utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.ui import Select

class approval(Page):
    '''审批页'''
    url='/'
    #Action//Filter
    Yige_approval_approval_btn=(By.XPATH,'//*[@id="F080000"]/a')
    Yige_approval_goApproval_btn=(By.XPATH,'//*[@id="F080100"]')
    Yige_approval_approvalRecord_btn=(By.XPATH,'//*[@id="F080200"]')
    Yige_approval_suserName_loc=(By.XPATH,'//*[@id="suserName"]')
    Yige_approval_btnFilter_btn=(By.ID,'btnFilter')
    Yige_approval_Filter_activity_loc=(By.XPATH,'//*[@id="sxform"]/div[1]/div/span/span[1]/span/ul/li/input')
    Yige_approval_leaveType_loc=(By.XPATH,'//*[@id="sxform"]/div[2]/div/span/span[1]/span/ul/li/input')
    Yige_approval_applyTime_loc=(By.ID,'applyTime')
    Yige_approval_approvalTime_loc=(By.ID,'approvalTime')
    Yige_approval_result_loc=(By.XPATH,'//*[@id="sxform"]/div[5]/div/span/span/span[1]/span/ul/li/input')
    Yige_approval_query_btn=(By.ID,'btnQuerySalary')
    Yige_approval_pass_btn=(By.ID,'btnPass')
    Yige_approval_revoke_btn=(By.ID,'btnRevoke')
    Yige_approval_all_btn=(By.XPATH,'//*[@id="memberTable"]/thead/tr/th[1]/div/label/div/ins')
    Yige_approval_first_btn=(By.XPATH,'//*[@id="memberTable"]/tbody/tr/td[1]/div/label/div/ins')
    Yige_approval_pageUp_btn=(By.XPATH,'//*[@id="memberTable_previous"]/a')
    Yige_approval_pageDown_btn=(By.XPATH,'//*[@id="memberTable_next"]/a')
    Yige_approval_first_activity_btn=(By.XPATH,'//*[@id="memberTable"]/tbody/tr/td[2]/a')
    Yige_approval_details_opinion_loc=(By.XPATH,'//*[@id="formApproval"]/div[2]/div/textarea')
    Yige_approval_details_pass_btn=(By.XPATH,'//*[@id="formApproval"]/div[3]/div/button[1]')
    Yige_approval_details_revoke_btn=(By.XPATH,'//*[@id="formApproval"]/div[3]/div/button[1]')
    Yige_approval_details_back_btn=(By.XPATH,'/html/body/div[5]/h4/a')
    #缺少一个单独选择申请的“勾选”按钮

    def approval_approval(self):
        self.find_element(*self.Yige_approval_approval_btn).click()
    def approval_goApproval(self):
        self.find_element(*self.Yige_approval_goApproval_btn).click()
    def approval_approvalRecord(self):
        self.find_element(*self.Yige_approval_approvalRecord_btn).click()
    def approval_suserName(self,usernameOrPhone):
        self.find_element(*self.Yige_approval_suserName_loc).send_keys(usernameOrPhone)
    def approval_btnFilter(self):
        self.find_element(*self.Yige_approval_btnFilter_btn).click()
    def approval_activity(self,activity):
        self.find_element(*self.Yige_approval_Filter_activity_loc).send_keys(activity)
    def approval_leaveType(self,leaveType):
        self.find_element(*self.Yige_approval_leaveType_loc).send_keys(leaveType)
    def approval_applyTime(self,applyTime):
        self.find_element(*self.Yige_approval_applyTime_loc).send_keys(applyTime)
    def approval_approvalTime(self,approvalTime):
        self.find_element(*self.Yige_approval_approvalTime_loc).send_keys(approvalTime)
    def approval_result_pass(self):
        Select(self.find_element(*self.Yige_approval_result_loc)).select_by_value("通过")
    def approval_result_revoke(self):
        Select(self.find_element(*self.Yige_approval_result_loc)).select_by_value("驳回")
    def approval_pass(self):
        self.find_element(*self.Yige_approval_pass_btn).click()
    def approval_revoke(self):
        self.find_element(*self.Yige_approval_revoke_btn).click()
    def approval_all(self):
        self.find_element(*self.Yige_approval_all_btn).click()
    def approval_first(self):
        self.find_element(*self.Yige_approval_first_btn).click()
    def approval_pageUp(self):
        self.find_element(*self.Yige_approval_pageUp_btn).click()
    def approval_pageDown(self):
        self.find_element(*self.Yige_approval_pageDown_btn).click()
    def approval_first_detail(self):
        self.find_element(*self.Yige_approval_first_activity_btn).click()
    def approval_details_opinion(self,opinion):
        self.find_element(*self.Yige_approval_details_opinion_loc).send_keys(opinion)
    def approval_details_pass(self):
        self.find_element(*self.Yige_approval_details_pass_btn).click()
    def approval_details_revoke(self):
        self.find_element(*self.Yige_approval_details_revoke_btn).click()
    def approval_detail_back(self):
        self.find_element(*self.Yige_approval_details_back_btn).click()

    def goApproval(self):
        self.approval_approval()
        self.approval_goApproval()
    def user_first_pass(self):
        self.goApproval()
        self.approval_first()
        self.approval_pass()
    def user_first_revoke(self):
        self.goApproval()
        self.approval_first()
        self.approval_revoke()
    def user_all_pass(self):
        self.goApproval()
        self.approval_all()
        self.approval_pass()
    def user_all_revoke(self):
        self.goApproval()
        self.approval_all()
        self.approval_revoke()

    def oppinion(self,opinion):
        self.approval_first_detail()
        self.approval_details_opinion(opinion)


    def user_details_pass(self,opinion):
        self.goApproval()
        self.oppinion(opinion='测试')
        self.approval_details_pass()

    def user_details_revoke(self,opinion):
        self.goApproval()
        self.oppinion(opinion='测试')
        self.approval_details_revoke()

    def user_details_back(self,opinion):
        self.goApproval()
        self.approval_details_opinion(opinion='测试')
        self.approval_detail_back()