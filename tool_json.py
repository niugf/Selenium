import json
import jmespath
from LearnSelenium.client import HTTPClient

class JMESPathExtractor(object):
    """
    用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取。
    """
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


if __name__ == '__main__':
    #from utils import HTTPClient
    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1]', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)
    print(j)
    print("#################")
    print(j_1)
    print("#################")
    print(j_2)



