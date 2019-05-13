# coding=utf-8
from selenium import webdriver
import unittest
import time
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#切换iframe,frame、获取指标值进行处理、添加检查点、自定义异常
from selenium.common.exceptions import NoSuchElementException



class Test1(unittest.TestCase):

    def dealS(self,str):
        #处理1.70%
        list1=list(str)
        del list1[len(list1)-1]
        strnew="".join(list1)
        number=float(strnew)
        return number

    def setUp(self):

        # chromedriver = "C:/ProgramFiles(x86)/Google/Chrome/Application/chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://10.4.149.37:8081/ui/ui.lsp?file=zflt/index"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_dp_test(self):
        u"""大屏查看话务量"""
        driver=self.driver

        driver.implicitly_wait(30)
        driver.get(self.base_url)
        driver.switch_to.frame(0)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[5]/div/div/div[1]/div').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="main"]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[5]/div/div/div[2]/div').click()
        time.sleep(2)

        driver.find_element_by_xpath('.//*[@id="main"]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[5]/div/div/div[3]/div').click()
        time.sleep(2)

    def test_dp_zb(self):
        u"""大屏查看指标"""
        driver=self.driver
        driver.implicitly_wait(30)
        driver.get(self.base_url)
        driver.switch_to.frame(0)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        time.sleep(2)
        jkfg=driver.find_element_by_xpath('//*[@id="FGYHSID"]/p[4]').text
        print(jkfg)
        jkfgd=driver.find_element_by_xpath('//*[@id="FGYHSID"]/p[3]').text
        jkfgdn=self.dealS(jkfgd)
        print(jkfgdn)
        jkkt=driver.find_element_by_xpath('//*[@id="XZYHSID"]/p[4]').text
        print(jkkt)
        jkktd=driver.find_element_by_xpath('//*[@id="XZYHSID"]/p[3]').text
        jkktdn=self.dealS(jkktd)
        print(jkktdn)
        hlwkt=driver.find_element_by_xpath('//*[@id="ZXKDYHS"]/p[4]').text
        print(hlwkt)
        hlwktd=driver.find_element_by_xpath('//*[@id="ZXKDYHS"]/p[3]').text

        hlwktdn=self.dealS(hlwktd)
        print(hlwktdn)

        if jkfgdn>0.5 or jkfgdn>5.0 or hlwktdn>1.0 :
            self.verificationErrors.append(Exception('指标预警'))
            logging.error("家宽覆盖用户数比率: "+jkfgdn+" 家宽开通用户数比率 "+jkktdn+ " 互联网电视开通数"+hlwktdn )

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





