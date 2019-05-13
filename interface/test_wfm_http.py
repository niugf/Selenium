import unittest
from LearnSelenium.config.config import Config, REPORT_PATH
from LearnSelenium.client import HTTPClient
from LearnSelenium.log.log import Logger
from HTMLTestRunner import HTMLTestRunner


class TestBaiDuHTTP(unittest.TestCase):
    URL = Config().get('URL')
    params = 'requestParam={"userMobile":"","mobileModel": "","mobileImei":"","userAccount":"hx_dujun","userPassord":"null","userId":"273758","token":"2dba4ae36b169801b6ecf9342c32c796","flowId":"180413143000015","activeName":"费用支付","flowType":"0"}&useraccount=hx_dujun&token=2dba4ae36b169801b6ecf9342c32c796'
    URL = 'http://10.4.149.63:6873/wfm/plugins/taskquery/taskInfos.ilf?'+params

    def setUp(self):

        self.client = HTTPClient(url=self.URL, method='GET')

    def test_wfm_http(self):
        res = self.client.send()
        # Logger.get_logger(res.text)
        self.assertIn("wfm",res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='wfm工单展示接口测试', description='接口html报告')
        runner.run(TestBaiDuHTTP('test_wfm_http'))