import allure
import pytest

from utils.Asser_Util import Ass
from utils.Requests_Util import Request
from utils.Yaml_Util import yaml1




@pytest.fixture(autouse=True,scope='class')
def token():
    url = "https://kdtx-test.itheima.net/api/captchaImage"
    r = Request('=====前置条件（获取登录所需的uuid）========').get(url)
    uuid = r['body']["uuid"]

    url = "https://kdtx-test.itheima.net/api/login"
    data ={
        'username': "admin",
        'password': "HM_2023_test",
        'code': "2",
        'uuid': uuid}
    r = Request('=====前置条件（获取登录成功返回的token）=====').post(url, json=data)
    print(r['body']['token'])
    yield r['body']['token']


a = yaml1('Search').data1()


@allure.epic('客达天下')
@allure.feature('合同管理-合同列表查询')
class Test_ht_ss:

    @pytest.mark.parametrize('id,title,url,data,x', a)
    def test_ss(self,token,id,title,url,data,x):
        headers = {'Authorization': token}
        allure.dynamic.title(title)

        r = Request(f'\n{id}').get(url, headers=headers,params=data)

        a = Ass(id)
        a.code(x['status_code'],r['status_code'])
        a.bo(x['body']['msg'],r['body']['msg'])
        a.dy(x['body']['total'],r['body']['total'])

