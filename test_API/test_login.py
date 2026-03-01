import allure
import pytest

from utils.Asser_Util import Ass
from utils.Requests_Util import Request
from utils.Yaml_Util import yaml1



def uuid(name):
    url = "https://kdtx-test.itheima.net/api/captchaImage"
    r = Request(name).get(url)
    uuid = r['body']['uuid']
    return uuid


a = yaml1('login').data1()


@allure.epic('客达天下')
class Test_login:
    @allure.feature('登录模块')
    @pytest.mark.parametrize('id,title,url,data,x', a)
    def test_login(self,id,title,url,data,x):
        if data['uuid'] == 'uid':
            data['uuid'] = uuid(id)
        allure.dynamic.title(title)
        r = Request(id).post(url, json=data)
        a = Ass(id)
        a.code(x['status_code'], r['status_code'])
        a.bo(x['body']['msg'], r['body']['msg'])

if __name__ == '__main__':
    pytest.main(['-s', __file__])