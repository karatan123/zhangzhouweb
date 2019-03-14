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

import random
import string

plate_num = ''
idnum = ''
boxid = ''

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


class VehiclemanagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("车辆管理测试开始")
        self.browser = webdriver.Chrome(executable_path='/Users/kara/Downloads/chromedriver')
        self.browser.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://recycling.3po-dwm.com:8080/login"
        self.browser.get("http://recycling.3po-dwm.com:8080/login")
        self.browser.find_element_by_name("username").send_keys("zhangzhou5551")
        self.browser.find_element_by_name("password").send_keys("123456")
        self.browser.find_element_by_css_selector(
            "#login > div > div > div > div.login_content > form > nz-form-item:nth-child(3) > nz-form-control > div > span > nz-spin > div > div.ant-spin-container > button").click()
        time.sleep(5)

    def isElementExist(self, css):
        try:
            self.browser.find_element_by_xpath(css)
            return True
        except:
            return False


    def test_vehiclemanagement_add(self):
        global plate_num

        global idnum
        global boxid
     # 车牌号、车架号、车载盒子id具有唯一性，通过随机数生成
        num1 = random.randint(00000, 99999)
        plate_num = "闽Y" + str(num1)
        print(plate_num)

        num2 = random.sample(
           ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z'], 17)
        idnum = num2[0] + num2[1] + num2[2] + num2[3] + num2[4] + num2[5] + num2[6] + num2[7] + num2[8] + num2[9] + num2[10] + num2[11] + num2[12] + num2[13] + num2[14] + num2[15] + num2[16]
        print(idnum)

        boxid = "1" + str(random.randint(10000000, 99999999))
        print(boxid)
    #     进入车辆管理页面
        self.browser.get("http://recycling.3po-dwm.com:8080/manage/baseInfo/vehicles")
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[1]/div/div[3]/div/button[1]').click()
        time.sleep(2)
        self.browser.find_element_by_name("plateNumber").send_keys(plate_num)
        #  选择购买时间
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[3]/nz-form-control/div/span/nz-date-picker/nz-picker/span/input').click()
        time.sleep(5)
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/date-range-popup/div/div/div/div/inner-popup/div/date-table/table/tbody/tr[3]/td[3]/div').click()
        # 选择计划出车时间
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[4]/nz-form-control[1]/div/span/app-time-picker/nz-cascader/div/div/span').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[1]/li[1]').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[2]/li[1]').click()
        time.sleep(2)

    #选择最晚回厂时间
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[4]/nz-form-control[2]/div/span/app-time-picker/nz-cascader/div/div/span').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[1]/li[6]').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[2]/li[1]').click()
        time.sleep(2)

        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[5]/nz-form-control/div/span/nz-select/div/div/div[2]/div/input').click()

        self.browser.find_element_by_xpath('/html/body/div/div[6]/div/div/div/ul/li[1]').click()
        time.sleep(2)

    #     提交
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[7]/nz-form-control[1]/div/span/button').click()
        time.sleep(5)
    #     搜索刚刚添加的车辆确认是否成功添加
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[5]/div/input').send_keys(plate_num)
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[1]/table/thead/tr/th[5]/div/input').send_keys(Keys.ENTER)
        time.sleep(2)
        message = self.isElementExist('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input')
        self.assertTrue(message)

    def test_vehiclemanagement_edit(self):
        global idnum

        global boxid
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input').click()
        time.sleep(2)
    #     点击编辑按钮
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[1]/div/div[3]/div/button[2]').click()
        time.sleep(2)
        self.browser.find_element_by_name('idNumber').send_keys(idnum)
        self.browser.find_element_by_name('boxId').send_keys(boxid)
        self.browser.find_element_by_name('engineModel').send_keys('HL0112')

        # 修改计划出车时间
        self.browser.find_element_by_xpath(
            '//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[4]/nz-form-control[1]/div/span/app-time-picker/nz-cascader/div/div/span').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[1]/li[3]').click()
        self.browser.find_element_by_xpath('/html/body/div/div[8]/div/div/ul[2]/li[1]').click()
        time.sleep(2)

        #     提交
        self.browser.find_element_by_xpath('//*[@id="form"]/nz-spin/div/div[2]/form/nz-form-item[7]/nz-form-control[1]/div/span/button').click()
        time.sleep(5)

        outtime = self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[7]')
        self.assertEqual(outtime.text, "02:00")

    def test_vehiclemanagement_delete(self):
    #    点击删除按钮
        self.browser.find_element_by_xpath('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[1]/div/div[3]/div/button[3]').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div/div[3]/div/nz-modal/div/div[2]/div[1]/div/div/div/div[2]/button[2]').click()
        time.sleep(5)
        message = self.isElementExist('/html/body/app-root/app-manage-app/div[2]/app-vehicle-info/div/div[2]/nz-spin/div/div[2]/nz-table/div/nz-spin/div/div[2]/div/div/div/div/div[2]/table/tbody/tr/td[1]/label/span[1]/input')
        self.assertFalse(message)

    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()