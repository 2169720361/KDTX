import requests

from utils.Log_Util import log0


class Request:
    def __init__(self,name='Request'):
        self.log = log0(name)

    def api(self, url, method="get", **kwargs):
        if method == "get":
            self.log.debug('发送了get请求')
            r = requests.get(url, **kwargs)
        elif method == "post":
            self.log.debug('发送了post请求')
            r = requests.post(url, **kwargs)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            print(f"JSON解析失败，具体错误：{e}")
            body = r.text

        res = {"status_code": code, "body": body}
        return res


    def get(self, url, **kwargs):
        return self.api(url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.api(url, method="post", **kwargs)
