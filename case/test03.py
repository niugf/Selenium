# coding=utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

#处理window、添加检查点

class Test(unittest.TestCase):
    def path(self,str):
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = 'F:\\python\\image\\' + now+ str + '.png'
        return pic_path

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://passport.jd.com/new/login.aspx"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_jidong(self):
        u"""京东登录"""
        driver=self .driver
        driver.implicitly_wait(30)
        driver.get("https://passport.jd.com/new/login.aspx")

        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_name("loginname").clear()
        driver.find_element_by_name("loginname").send_keys("13698629279")
        driver.find_element_by_name("nloginpwd").send_keys("yajie147258")
        driver.find_element_by_id("loginsubmit").click()
        time.sleep(3)

    def test_skip_jidong(self):
        u"""京东补水"""
        self.test_login_jidong()
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="J_cate"]/ul/li[6]/a[1]').click()
        time.sleep(2)

        print(driver.current_window_handle)
        handles = driver.window_handles
        print(handles)
        for handle in handles:  # 切换窗口
            if handle != driver.current_window_handle:
                print('switch to window', handle)
                driver.switch_to.window(handle)

        title = driver.title
        url = driver.current_url
        print(url)
        print(title)
        locator = (By.ID, 'beauty_nav_1')
        time.sleep(1)
        try:
            WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            print("获取到了")
            driver.find_element_by_xpath('//*[@id="beauty_nav_1"]/div/div/div[2]/div[1]/div[2]/div[1]/div/a[1]').click()

        except BaseException as e:
            print('except:', e)
            logging.error("没找到补水'")
            self.verificationErrors.append(Exception('没找到补水'))


        handles = driver.window_handles
        print(handles)
        for handle in handles:  # 切换窗口
            if handle != driver.current_window_handle:
                print('switch to second window', handle)
                driver.switch_to.window(handle)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="J_selector"]/div[3]/div/div[3]/a[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="J_selector"]/div[3]/div/div[2]/div[1]/ul/li[12]/a').click()
        driver.find_element_by_xpath('//*[@id="J_selector"]/div[3]/div/div[2]/div[1]/ul/li[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="J_selector"]/div[3]/div/div[2]/div[2]/a[1]').click()


        try:
            lactor = (By.LINK_TEXT, '完美芦荟胶40g 3支装')
            WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(lactor))

        except BaseException as e:
            print('except:', e)
            logging.error("5秒内没找到不到完美芦荟胶40g 3支装'")
            self.verificationErrors.append(Exception('获取不到完美芦荟胶40g'))

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
    unittest.main()