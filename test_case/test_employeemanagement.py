# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:登录LockerLife Web端测试用例
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# available since 2.12
from selenium.webdriver.support.ui import Select

import logging

from selenium import webdriver
import unittest
import time

import re
import os
import random
import string

from selenium.webdriver.common.keys import Keys


username = ""
phone = ""
identity = ""


def start_driver(name, local_storage=None, log_file=None):
    """
    web driver 启动浏览器使用，支持使用local storage
    :param name: 浏览器名称
    :param local_storage: local storage保存路径（或者Chrome默认存在local storage的路径）
    :param log_file:浏览器运行日志保存路径（需要建立一个后缀名.log的文件）【此处可以为空，非必填】
    :return:
    """
    try:
        if name == u'chrome' or name == u'Chrome':
            logging.info(u'browser was opened')
            if local_storage is not None and local_storage is not None:
                setting = webdriver.ChromeOptions()
                setting.add_argument(local_storage)
                driver = webdriver.Chrome(chrome_options=setting, service_log_path=log_file)
                return driver
            elif local_storage is None and local_storage is None:
                driver = webdriver.Chrome(executable_path='/Users/kara/Downloads/chromedriver')
                return driver
        elif name == u'ie' or name == u'Ie' or u'IE':
            logging.info(u'browser was opened')
            driver = webdriver.Ie()
            return driver
        elif name == u'firefox' or name == u'FireFox' or name == u'ff':
            logging.info(u'browser was opened')
            driver = webdriver.Firefox()
            return driver
        elif name == u'safari' or name == u'Safari':
            logging.info(u'browser was opened')
            driver = webdriver.Safari()
            return driver
        else:
            logging.error(u'no found this browser,please try another values,such as(chrome,ie,firefox,safari)')
    except Exception:
        raise Exception('浏览器出现异常: %s')


class EmployeemanagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("人员管理测试开始")
        self.browser = webdriver.Chrome(executable_path='/Users/kara/Downloads/chromedriver')
        self.browser.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://recycling.3po-dwm.com:8080/login"
        self.browser.get("http://recycling.3po-dwm.com:8080/login")
        self.browser.find_element_by_name("username").send_keys("zhangzhou5551")
        self.browser.find_element_by_name("password").send_keys("123456")
        self.browser.find_element_by_css_selector(
            "#login > div > div > div > div.login_content > form > nz-form-item:nth-child(3) > nz-form-control > div > span > nz-spin > div > div.ant-spin-container > button").click()

    def isElementExist(self, css):
        try:
            self.browser.find_element_by_xpath(css)
            return True
        except:
            return False


    def test_employeemanagement_add(self):
        num1 = random.randint(1000, 9999)
        global username
        username = "testerkara" + str(num1)
        print(username)

        num2 = random.randint(70000000, 79999999)
        global phone
        phone = "186" + str(num2)
        print(phone)

        num3 = random.randint(100000, 999999)
        num4 = random.randint(1000, 9999)
        global identity
        identity = str(num3) + "19900101" + str(num4)
        print(identity)
        self.browser.find_element_by_css_selector("body > app-root > app-manage-app > div.manage-app-content > app-staff-info > div > div.table-operations > div > div.gutter-row.ant-col-8 > div > button:nth-child(1)").click()
        self.browser.find_element_by_name("name").send_keys("自动化测试生成人员")
        self.browser.find_element_by_css_selector("#sex > label:nth-child(1) > span:nth-child(2)").click()
        self.browser.find_element_by_name("username").send_keys(username)
        self.browser.find_element_by_name("password").send_keys("123456")
        # 选择岗位
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[3]/nz-form-control[1]/div/span/nz-select/div/div/div[2]/div/input').click()
        self.browser.find_element_by_xpath('/html/body/div/div[10]/div/div/div/ul/li[7]').click()
        # 选择时间
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[3]/nz-form-control[2]/div/span/nz-date-picker/nz-picker/span/input').click()
        self.browser.find_element_by_xpath('/html/body/div/div[12]/div/div/date-range-popup/div/div/div/div/inner-popup/div/date-table/table/tbody/tr[3]/td[1]').click()
        #选择角色
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[4]/nz-form-control/div/span/nz-select/div/div/div').click()
        self.browser.find_element_by_xpath('//html/body/div/div[10]/div/div/div/ul/li[5]').click()

        # 为了关闭角色下拉框
        self.browser.find_element_by_xpath('/html/body/div/div[9]').click()

        self.browser.find_element_by_name("identity").send_keys(identity)

        self.browser.find_element_by_name("email").send_keys("1143043178@qq.com")

        self.browser.find_element_by_name("mobilePhone").send_keys(phone)

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.browser.find_element_by_css_selector("#form > nz-spin > div > div.ant-spin-container > form > nz-form-item:nth-child(12) > nz-form-control.ant-col-3.ant-col-offset-17.ant-form-item-control-wrapper > div > span > button").click()
        time.sleep(10)

        self.browser.find_element_by_xpath(
            '/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[3]/div/input').send_keys(
            username)
        self.browser.find_element_by_xpath(
            '/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[3]/div/input').send_keys(
            Keys.ENTER)
        time.sleep(2)
        message = self.isElementExist('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input')
        self.assertTrue(message)

    def test_employeemanagement_edit(self):
     #     搜索到刚刚添加的人员进行编辑
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input').click()
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[1]/div/div[3]/div/button[2]').click()

    # 修改信息
        name = self.browser.find_element_by_name('name')
        name.clear()
        name.send_keys('修改后的姓名')
        self.browser.find_element_by_name('emergencyContact').send_keys('张三')
        self.browser.find_element_by_name('emergencyContactPhone').send_keys('18675083719')
        self.browser.find_element_by_name('detailAddress').send_keys('某某街某某社区某某栋')

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        self.browser.find_element_by_css_selector('#form > nz-spin > div > div.ant-spin-container > form > nz-form-item:nth-child(12) > nz-form-control.ant-col-3.ant-col-offset-17.ant-form-item-control-wrapper > div > span > button').click()
        time.sleep(5)
        name = self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[2]')
        self.assertEqual(name.text, u"修改后的姓名")


    def test_employeemanagement_delete(self):
    #     点击删除按钮
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[1]/div/div[3]/div/button[3]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div/div[5]/div/nz-modal/div/div[2]/div[1]/div/div/div/div[2]/button[2]').click()
        time.sleep(5)
        message = self.isElementExist('/html/body/app-root/app-manage-app/div[2]/app-staff-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input')
        self.assertFalse(message)

    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()