import pytest
import uuid
import allure

from utils.Asser_Util import Ass
from utils.Requests_Util import Request


@pytest.fixture()
def uid():
    url = "https://kdtx-test.itheima.net/api/captchaImage"
    r = Request('前置操作: 获取最新uuid').get(url)
    uuid = r['body']['uuid']
    yield uuid


@allure.epic('客达天下')
@allure.feature('合同管理业务')
class Test_htgl:
    url_login = 'https://kdtx-test.itheima.net/api/login'
    url_add = 'https://kdtx-test.itheima.net/api/contract'
    url_list = 'https://kdtx-test.itheima.net/api/contract/list'


    @allure.title('合同管理业务流程成功（全流程成功）')
    def test_htgl1(self,uid):
        bh = 'HT' + uuid.uuid4().hex[:9]

        with allure.step('1、登录'):
            data = {
                "username": "admin",
                "password": "HM_2023_test",
                "code": "2",
                "uuid": uid}
            r = Request('TC-BIZ-001').post(url=self.url_login,json=data)
            token = r['body']['token']
        with allure.step('2、添加合同'):
            data = {
                "name":"张三",
                "phone":"13212340001",
                "contractNo":bh,
                "subject":"6",
                "courseId":"361",
                "fileName":"/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"}
            headers = {'Authorization': token}
            r = Request('TC-BIZ-001').post(url=self.url_add,json=data,headers=headers)
        with allure.step('3、查询刚刚添加的合同'):
            data = {'contractNo': bh}
            headers = {'Authorization': token}
            r = Request('TC-BIZ-001').get(url=self.url_list,headers=headers,params=data)
        with allure.step('4、断言'):
            Ass('TC-BIZ-001').code(200,r['status_code'])
            Ass('TC-BIZ-001').bo(bh,r['body']['rows'][0]['contractNo'])


    @allure.title('合同管理业务流程失败（登录失败-密码错误）')
    def test_htgl2(self,uid):
        with allure.step('1、登录'):
            data = {
                "username": "admin",
                "password": "wrong_password",
                "code": "2",
                "uuid": uid}
            r = Request('TC-BIZ-002').post(url=self.url_login,json=data)
        with allure.step('2、断言'):
            Ass('TC-BIZ-002').code(200,r['status_code'])
            Ass('TC-BIZ-002').bo('密码错误',r['body']['msg'])


    @allure.title('合同管理业务流程失败（添加合同失败-合同编号重复）')
    def test_htgl3(self, uid):
        with allure.step('1、登录'):
            data = {
                "username": "admin",
                "password": "HM_2023_test",
                "code": "2",
                "uuid": uid}
            r = Request('TC-BIZ-003').post(url=self.url_login, json=data)
            token = r['body']['token']
        with allure.step('2、添加合同'):
            data = {
                "name": "张三",
                "phone": "13212340001",
                "contractNo": 'A',
                "subject": "6",
                "courseId": "361",
                "fileName": "/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"}
            headers = {'Authorization': token}
            r = Request('TC-BIZ-003').post(url=self.url_add, json=data, headers=headers)
        with allure.step('3、断言'):
            Ass('TC-BIZ-003').code(200,r['status_code'])
            Ass('TC-BIZ-003').bo('已存在',r['body']['msg'])

    @allure.title('合同管理业务流程失败（查询合同失败-输入不存在的合同编号）')
    def test_htgl4(self,uid):
        bh = 'HT' + uuid.uuid4().hex[:9]

        with allure.step('1、登录'):
            data = {
                "username": "admin",
                "password": "HM_2023_test",
                "code": "2",
                "uuid": uid}
            r = Request('TC-BIZ-004').post(url=self.url_login,json=data)
            token = r['body']['token']
        with allure.step('2、添加合同'):
            data = {
                "name":"张三",
                "phone":"13212340001",
                "contractNo":bh,
                "subject":"6",
                "courseId":"361",
                "fileName":"/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"}
            headers = {'Authorization': token}
            r = Request('TC-BIZ-004').post(url=self.url_add,json=data,headers=headers)
        with allure.step('3、查询刚刚添加的合同'):
            data = {'contractNo': '不存在的合同'}
            headers = {'Authorization': token}
            r = Request('TC-BIZ-004').get(url=self.url_list,headers=headers,params=data)
        with allure.step('4、断言'):
            Ass('TC-BIZ-004').code(200,r['status_code'])
            Ass('TC-BIZ-004').dy(False,r['body']['total'])
            print(f'\n{r}\n{bh}')


if __name__ == '__main__':
    pytest.main(['-s',__file__])