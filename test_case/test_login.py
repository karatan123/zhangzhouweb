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


class LoginTest(unittest.TestCase):
    def setUp(self):
        print('登录测试开始')
        self.browser = webdriver.Chrome(executable_path='/Users/kara/Downloads/chromedriver')
        self.browser.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "http://recycling.3po-dwm.com:8080/login"

    def isElementExist(self, css):
        try:
            self.browser.find_element_by_xpath(css)
            return True
        except:
            return False

    # 定义登录方法
    def login(self, username, password):
         self.browser.get("http://recycling.3po-dwm.com:8080/login")
         self.browser.find_element_by_name("username").send_keys(username)
         self.browser.find_element_by_name("password").send_keys(password)
         self.browser.find_element_by_css_selector(
             "#login > div > div > div > div.login_content > form > nz-form-item:nth-child(3) > nz-form-control > div > span > nz-spin > div > div.ant-spin-container > button").click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('zhangzhou5551','123456')
        time.sleep(3)
        title = self.browser.title
        print(title)
        self.assertEqual(title, u"人员管理")
        self.browser.get_screenshot_as_file("/Users/kara/zhangzhouweb/screenshot/login_success.jpg")

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('zhangzhou5551', '343434')  # 正确用户名，错误密码
        time.sleep(5)
        # self.browser.get_screenshot_as_file("/Users/kara/zhangzhouweb/screenshot/login_pwd_error.jpg")
        message = self.isElementExist('//*[@id="login"]/div/div/div/div[1]/img[2]')
        self.assertTrue(message)


    def tearDown(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()