# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持机测试用例
'''
import unittest
import os
import time
from test_case import test_login
from test_case import test_employeemanagement
from test_case import test_vehiclemanagement



from HTMLTestRunner import HTMLTestRunner

# 报告存放路径
report_path = "/Users/kara/zhangzhouweb/report"
print(report_path)

#构造测试集
suite = unittest.TestSuite()
'''suite.addTest(test_login.LoginTest('test_login_success'))
suite.addTest(test_login.LoginTest('test_login_pwd_error'))
suite.addTest(test_employeemanagement.EmployeemanagementTest('test_employeemanagement_add'))
suite.addTest(test_employeemanagement.EmployeemanagementTest('test_employeemanagement_edit'))
suite.addTest(test_employeemanagement.EmployeemanagementTest('test_employeemanagement_delete'))'''
suite.addTest(test_vehiclemanagement.VehiclemanagementTest('test_vehiclemanagement_add'))
suite.addTest(test_vehiclemanagement.VehiclemanagementTest('test_vehiclemanagement_edit'))
suite.addTest(test_vehiclemanagement.VehiclemanagementTest('test_vehiclemanagement_delete'))




if __name__=='__main__':
   now = time.strftime("%Y-%m-%d-%H-%M-%S")
   report_abspath = os.path.join(report_path,"result_"+now+".html")
   fp = open(report_abspath,"wb")
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告，测试结果如下：',description=u'用例执行情况：')
   runner.run(suite)