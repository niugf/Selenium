# coding=utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.support.ui import Select
from LearnSelenium.config.config import Config, DRIVER_PATH,DATA_PATH
from LearnSelenium.log.log import logger
from LearnSelenium.config.file_reader import ExcelReader
#三种等待的介绍

# 继承unittest类
class Test(unittest.TestCase):

    def path(self,str):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = 'F:\\python\\image\\' + now+ str + '.png'
        return pic_path


    # unittest提供的初始化方法，setup在这里进行一些初始化的准备工作
    def setUp(self):
        #self.driver = webdriver.Firefox()
        chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(chromedriver)
        #隐性等待表示,在规定的时间内页面的所有元素都加载完了就执行下一步，否则一直等到时间截止，然后再继续下一步
        self.driver.implicitly_wait(30)
        self.excel=DATA_PATH+'//test.xlsx'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_qxxt_login(self):
        u"""权限系统登录"""
        driver = self.driver
        driver.get(Config().get('URLY'))
        driver.find_element_by_id("userid").send_keys("zms")
        driver.find_element_by_id("password").send_keys("ZZZms,123")
        driver.find_element_by_xpath('//*[@id="confirm"]').click()
        time.sleep(2)
        driver.switch_to.frame("frmRight")
        userid=driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/font").text
        if userid=='zms':
            logger.info("权限系统登录正常")
        else:
            self.verificationErrors.append(Exception('权限系统登录验证失败'))
            logger.error("没找到的登录页面呢，有问题吧")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unitest.main()函数用来测试 类中以test开头的测试用例

    unittest.main()
