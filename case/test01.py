# coding=utf-8
from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LearnSelenium.common.browser import CHROMEDRIVER_PATH ,IEDRIVER_PATH
import logging
from selenium.webdriver.support.ui import Select
from LearnSelenium.config.config import Config, DRIVER_PATH,DATA_PATH
from LearnSelenium.log.log import logger
from LearnSelenium.config.file_reader import ExcelReader
from LearnSelenium.page.BasePage import BasePage
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
        # IEdriver="E:\\IEDriverServer_Win32_2.39.0.exe"
        # self.driver = webdriver.Ie(IEdriver)
        #chromedriver = "C:/chromedriver.exe"
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        #隐性等待表示,在规定的时间内页面的所有元素都加载完了就执行下一步，否则一直等到时间截止，然后再继续下一步
        self.driver.implicitly_wait(30)
        self.base_url = Config().get('URL')
        self.excel=DATA_PATH+'//test.xlsx'
        self.verificationErrors = []
        self.accept_next_alert = True

    # 下面是测试方法
    def test_wfm_login(self):
        u"""施工调度系统登录"""
        driver = self.driver
        driver.get(self.base_url + '/')
        datas = ExcelReader(self.excel).data
        #logger.info(datas)
        #login_page = BasePage.LoginPage(self.driver)
        driver.find_element_by_id("useraccount").send_keys("jiake_new")
        driver.find_element_by_id("password").send_keys("Secret1001-")
        driver.find_element_by_xpath('//*[@id="formlogin"]/p[4]/button').click()
        #  login_page.set_username("jiake_new")
        # Step4: Enter password
        # login_page.set_password("Secret1001-")
        # Step4: click login
        # login_page.click_SignIn
        time.sleep(4)
        # for d in datas:
        #     driver.find_element_by_id("useraccount").send_keys(d["account"])
        #     driver.find_element_by_id("password").send_keys(d["pwd"])
        #     driver.find_element_by_xpath('//*[@id="formlogin"]/p[4]/button').click()
        #     time.sleep(2)
        logger.info("施工调度系统登录正常")

    def test_wfm_loginNot(self):
        u"""施工调度系统登录失败"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("useraccount").send_keys("jiake_new")
        driver.find_element_by_id("password").send_keys("1234123")
        driver.find_element_by_xpath('//*[@id="formlogin"]/p[4]/button').click()
        time.sleep(2)
        lactor = (By.ID, 'password')

        try:
            #selenium的显示等待，就是明确的要等到某个元素的出现或者是某个元素的可点击等条件，等不到，就一直等
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(lactor))
            logger.info("施工调度系统登录失败验证正常")

        except BaseException as e:
            logger.error('except:', e)
            self.verificationErrors.append(Exception('失败登录验证失败'))
            logger.error("没找到的登录页面呢，有问题吧")
        time.sleep(2)

    def test_wfm_appoint(self):
        u"""施工调度系统集中预约模块"""
        logger.info("集中预约开始正常")
        try:
            driver = self.driver
            logger.info("开始调用登陆方法")
            self.test_wfm_login()
            logger.info("开始调用登陆完成")
            driver.find_element_by_xpath('//*[@id="topMenu"]/li[1]/a').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="accordion2"]/div[2]/div/a').click()
            #driver.find_element_by_link_text('集中预约')
            time.sleep(3)
            #driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
            driver.switch_to.frame(0)
            driver.find_element_by_xpath('//*[@id="searchFrom"]/table/tbody[2]/tr[2]/td[1]/input').send_keys(
                'BJ-801-180303-3232')
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="btn_accept_refresh"]').click()
            time.sleep(3)
            driver.save_screenshot(self.path("集中预约"))
            logger.info("集中预约验证正常")
        except BaseException as e:
            logger.error('except:', e)

    def test_wfm_audit(self):
        u"""施工调度系统集中质检模块"""
        logger.info("质检开始正常")
        driver = self.driver
        self.test_wfm_login()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[2]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[2]/div/a').click()
        time.sleep(2)
        driver.save_screenshot(self.path("集中质检"))
        logger.info("集中质检验证正常")

    def test_wfm_report(self):
        u"""施工调度系统工单查询模块"""
        logger.info("工单查询正常")
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[4]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[4]/div').click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        options = Select(driver.find_element_by_id("formType")).select_by_visible_text("移机")
        driver.find_element_by_xpath('//*[@id="btn_query"]').click()
        time.sleep(20)
        driver.save_screenshot(self.path("工单查询"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        if len(table_rows) >10 :
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('移机工单查询数量小于10'))

    def test_wfm_report_manage(self):
        u"""施工调度系统报表质检原因日报模块"""
        logger.info("原因日报正常")
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[8]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="collapse6"]/div/ul/li[5]').click()
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        driver.save_screenshot(self.path("质检原因日报"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        print(len(table_rows))

        if len(table_rows) is 14:
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('质检原因报表数量不正确'))

    def test_wfm_report_manage_audit(self):
        u"""施工调度系统报表质检日报模块"""
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[8]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="collapse6"]/div/ul/li[4]').click()
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        driver.save_screenshot(self.path("质检日报"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        print(len(table_rows))

        if len(table_rows) is 14:
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('质检日报数量不正确'))

    def test_wfm_report_manage_online(self):
        u"""施工调度系统报表在途日报模块"""
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[8]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="collapse6"]/div/ul/li[3]').click()
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        driver.save_screenshot(self.path("在途日报"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        print(len(table_rows))

        if len(table_rows) is 14:
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('在途日报数量不正确'))

    def test_wfm_report_manage_shot(self):
        u"""施工调度系统报表短日报模块"""
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[8]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="collapse6"]/div/ul/li[2]').click()
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        driver.save_screenshot(self.path("短日报"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        print(len(table_rows))

        if len(table_rows) is 14:
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('短日报数量不正确'))

    def test_wfm_report_manage_create(self):
        u"""施工调度系统报表建单日报模块"""
        driver = self.driver
        self.test_wfm_login()
        driver.find_element_by_xpath('//*[@id="topMenu"]/li[5]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="accordion2"]/div[8]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="collapse6"]/div/ul/li[1]').click()
        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(3)
        driver.save_screenshot(self.path("建单日报"))
        table = driver.find_element_by_id('jqGrid')
        table_rows = table.find_elements_by_tag_name('tr')
        print(len(table_rows))

        if len(table_rows) is 14:
            logger.info("工单查询正常")
        else:
            self.verificationErrors.append(Exception('建单日报数量不正确'))

    def test_wore_login(self):
        u"""终端管理系统登录"""
        driver = self.driver
        driver.get(Config().get('URLX'))
        driver.find_element_by_id("useraccount").send_keys("inspur")
        driver.find_element_by_id("password").send_keys("inspur1")
        driver.find_element_by_xpath('//*[@id="formlogin"]/button').click()
        time.sleep(2)
        lactor = (By.XPATH, '//*[@id="topMenu"]/li[2]/a')
        try:
            #selenium的显示等待，就是明确的要等到某个元素的出现或者是某个元素的可点击等条件，等不到，就一直等
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(lactor))
            logger.info("终端管理系统登录正常")

        except BaseException as e:
            logger.error('except:', e)
            self.verificationErrors.append(Exception('终端管理系统登录验证失败'))
            logger.error("没找到的登录页面呢，有问题吧")
        time.sleep(2)
        logger.info("终端管理系统登录验证正常")

    def test_qkwfm_login(self):
        u"""企宽施工调度系统登录"""
        driver = self.driver
        driver.get(Config().get('URLZ'))
        datas = ExcelReader(self.excel).data
        logger.info(datas)
        driver.find_element_by_id("useraccount").send_keys("jiake_new")
        driver.find_element_by_id("password").send_keys("Secret1001-")
        driver.find_element_by_xpath('//*[@id="formlogin"]/p[4]/button').click()
        time.sleep(4)
        # for d in datas:
        #     driver.find_element_by_id("useraccount").send_keys(d["account"])
        #     driver.find_element_by_id("password").send_keys(d["pwd"])
        #     driver.find_element_by_xpath('//*[@id="formlogin"]/p[4]/button').click()
        #     time.sleep(2)
        logger.info("施工调度系统登录正常")

    def test_zmh_login(self):
        u"""门户系统登录"""
        driver = self.driver
        driver.get(Config().get('URLA'))
        datas = ExcelReader(self.excel).data
        logger.info(datas)
        driver.find_element_by_id("input-login-username").send_keys("xiejy")
        driver.find_element_by_id("input-login-password").send_keys("aaa,1234")
        driver.find_element_by_id('ctrlbuttonlogin-submittext').click()
        self.driver.implicitly_wait(30)
        time.sleep(4)
        driver.switch_to.frame("net_report_portfolio_Ifr")
        # msg=driver.find_element_by_xpath('//*[@id="s1"]').text
        # print(msg)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unitest.main()函数用来测试 类中以test开头的测试用例

    unittest.main()
