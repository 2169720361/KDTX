import os
import uuid
import allure
import pytest


from playwright.sync_api import sync_playwright, expect
from utils.Yaml_Util import yaml1



@pytest.fixture(autouse=True,scope="class")
def login():
    with sync_playwright() as p:
        a = p.chromium.launch()
        b = a.new_context()
        page = b.new_page()
        page.goto("https://kdtx-test.itheima.net/#/login")

        page.get_by_role("textbox", name="密码").fill("HM_2023_test")
        page.get_by_role("textbox", name="账号").fill("admin")
        page.get_by_role("img").click()
        page.get_by_role("textbox", name="验证码").fill("2")
        page.get_by_role("button", name="登录").click()
        page.get_by_role("link", name="合同管理").click()
        yield page


a = yaml1('UI_add').data2()

@allure.epic('客达天下')
@allure.feature('UI_添加合同')
class Test_UI_ht_add:
    @pytest.mark.flaky(reruns=1, reruns_delay=2)
    @pytest.mark.parametrize('title,data,x',a)
    def test_add5(self,login,title,data,x):
        page = login
        allure.dynamic.title(title)
        page.reload()
        with allure.step('进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        if '姓名' in data:
            with allure.step('输入姓名'):
                page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill(data['姓名'])
        if '手机号' in data:
            with allure.step('输入手机号'):
                page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill(data['手机号'])
        if '合同编号' in data:
            te = uuid.uuid4().hex[:9]
            if data['合同编号'] == 'U':
                data['合同编号'] = data['合同编号'] + te
            elif data['合同编号'] == 'U1':
                data['合同编号'] = data['合同编号'] + te + '123456789'
            with allure.step('输入合同编号'):
                page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(data['合同编号'])
        if '学科' in data:
            with allure.step('选择学科'):
                page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
                page.get_by_role("listitem").filter(has_text="Java").click()
        if '课程' in data:
            with allure.step('选择课程'):
                page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
                page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()

        path = os.path.dirname(__file__)
        if '合同' in data and not data['合同']:
            pdf = path + os.sep + '1.pdf'
            with allure.step('上传合同'):
                with page.expect_file_chooser() as fc_info:
                    page.get_by_role("button", name="上传").click()
                file_chooser = fc_info.value
                file_chooser.set_files(pdf)
        elif '合同' in data and data['合同']:
            pdf = path + os.sep + '1.text'
            with allure.step('上传合同'):
                with page.expect_file_chooser() as fc_info:
                    page.get_by_role("button", name="上传").click()
                file_chooser = fc_info.value
                file_chooser.set_files(pdf)

        if '渠道' in data:
            with allure.step('选择渠道来源'):
                page.get_by_role("textbox", name="请输入渠道来源").click()
                page.get_by_role("listitem").filter(has_text="线上活动").click()
        with allure.step('点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()

        with allure.step('断言'):
            expect(page.locator(x['a'])).to_contain_text(x['b'])
        # page.wait_for_timeout(2000)