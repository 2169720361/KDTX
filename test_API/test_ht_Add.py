import uuid
import allure
import pytest
import os

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
    yield r['body']['token']



a = yaml1('Add').data1()

@allure.epic('客达天下')
class Test_ht_Add:

    @allure.feature('合同管理——添加合同')
    @pytest.mark.parametrize("id,title,url,data,x",a)
    def testAdd(self,token,id,title,url,data,x):

        allure.dynamic.title(title)
        if data['contractNo'] == 'H':
            pytest.skip(f'{title} 的合同编号必定重复')

        te = uuid.uuid4().hex[:8]
        if 'contractNo' in data and data['contractNo'] == 'HT':
            data['contractNo'] = data['contractNo'] + te
        elif 'contractNo' in data and data['contractNo'] == 'HT1':
            data['contractNo'] = data['contractNo'] + te + 'a123456789'
        elif 'contractNo' in data and data['contractNo'] == 'HT2':
            data['contractNo'] = data['contractNo'] + te + 'a1234567890'

        headers = {'Authorization': token}

        r = Request(id).post(url, json=data,headers=headers)

        print(r)
        print(te)

        ass = Ass(title)
        ass.code(x['status_code'],r['status_code'])
        ass.code2(x['body']['code'],r['body']['code'])
        if 'msg' in x['body'] and 'msg' in r['body']:
            ass.bo(x['body']['msg'],r['body']['msg'])


    @allure.feature('合同管理——添加合同——上传合同')
    @allure.title('上传合同成功（上传PDF格式的合同）')
    def test_Up1(self,token):
        url = "https://kdtx-test.itheima.net/api/common/upload"
        headers = {"Authorization": token}

        path = os.path.dirname(__file__) + os.sep + "1.pdf"
        pdf = open(path,"rb")
        files = {"file": pdf}

        r1 = Request('KT-CM-ADD-026').post(url, headers=headers, files=files)
        print('上传结果:',r1)

        ass = Ass('KT-CM-ADD-026')
        ass.code(200, r1['status_code'])
        ass.bo('成功',r1['body']['msg'])
        ass.code2(200, r1['body']['code'])


    @allure.feature('合同管理——添加合同——上传合同')
    @allure.title('上传合同失败（上传非PDF格式的合同）')
    def test_Up2(self,token):
        url = "https://kdtx-test.itheima.net/api/common/upload"
        headers = {"Authorization": token}

        path = os.path.dirname(__file__) + os.sep + "1.text"
        pdf = open(path,"rb")
        files = {"file": pdf}

        r1 = Request('KT-CM-ADD-027').post(url, headers=headers, files=files)
        print('上传结果:',r1)
        ass = Ass('KT-CM-ADD-027')
        ass.code(200,r1['status_code'])
        ass.code2(500, r1['body']['code'])



if __name__ == "__main__":
    pytest.main(["-s", __file__])