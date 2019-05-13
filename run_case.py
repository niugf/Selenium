#coding=utf-8
import os
import time
import unittest
from BeautifulReport import BeautifulReport
from LearnSelenium.config.send_email import send_mail
from LearnSelenium.config.config import REPORT_PATH
from LearnSelenium.config.send_msg import send_msg


def allcase():
    # 这块是通过unittest的testsuite方式来组织测试
    case_dir=r"C:\Users\niugf\PycharmProjects\untitled1\LearnSelenium\case"
    #case_path=os.path.join(os.getcwd(),"case")
    #case_dir =os.path.join(os.getcwd(),"case")

    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,
                                                 pattern='test01.py',
                                                 top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    #print(discover)
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            print(test_case)
            testcase.addTest(test_case)
    return testcase

#======================查找最新的测试报告==========================

def new_report(testreport):

    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new

if __name__ == '__main__':
    # unittest.main()， 这里要说明一下， 如果测试方法是以test开头的，那么unittest可以识别出来，这里就可以直接调用它的main方法来执行所有测试方法了，运行顺序就是按测试方法的名字排序

    test_dir = os.path.join(os.getcwd(),)#获取当前目录
    #test_report = "F:\\python\\report\\"
    test_report=REPORT_PATH
    #test_report = os.path.join(os.getcwd(), 'report')
    #初始化一个测试套件
    #discover = unittest.defaultTestLoader.discover(test_dir,pattern='Fayua*.py')
    #testunit = unittest.TestSuite()
    #testunit.addTest(unittest.makeSuite(FaYuan.Test))
    #生成报告名字
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = REPORT_PATH+'result_'+now+'.html'
    #执行用例
    # 调用HTMLtestrunner来执行脚本并生成测试报告，html格式
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description='用例执行情况：')
    # runner.run(allcase())
    # fp.close()
    filename = 'result_'+now+'.html'
    #调用BeautifulReport来执行脚本并生成测试报告，html格式
    runner = BeautifulReport(allcase())
    runner.report(filename=filename, description='项目测试报告',log_path=test_report)

    new_report = new_report(test_report)
    send_mail(new_report)

    suite=unittest.TextTestRunner(verbosity=2).run(allcase())
    string="您好：本次测试共14个用例，包含集中预约、调度质检、工单查询、调度中心报表、终端管理系统、门户、权限、企宽。自动化测试结果为"
    msg=string+str(suite)[31:-1]+"详情请查看邮件"
    #phones = [ '15110253297', '15011178997', '15210004536','15010863224', '18201355957', ]
    phones = ['15110253297']
    # for phone in phones:
    #     send_msg(phone, msg)
    if str(suite)[-2]=="0" and str(suite)[-3]=="=":
        print(msg)
    else:
        #phones=['15010863224','18201355957','15110253297','15011178997','15210004536',]
        for phone in phones:
            send_msg(phone, msg)


