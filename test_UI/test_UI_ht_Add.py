import os
import uuid

import allure
import pytest


from playwright.sync_api import sync_playwright, expect


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


@allure.epic('客达天下')
@allure.feature('添加合同')
class Test_UI_ht_add:
    te = uuid.uuid4().hex[:9]
    path = os.path.dirname(__file__)
    pdf = path + os.sep + '1.pdf'


    @allure.title('添加合同成功')
    def test_add1(self,login):
        page = login
        page.reload()

        with allure.step('1、进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        with allure.step('2、输入姓名、手机号、合同编号'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(self.te)
        with allure.step('3、选择学科与课程'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
            page.get_by_role("listitem").filter(has_text="Java").click()
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
            page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        with allure.step('4、上传合同'):
            with page.expect_file_chooser() as fc_info:
                page.get_by_role("button", name="上传").click()
            file_chooser = fc_info.value
            file_chooser.set_files(self.pdf)
        with allure.step('5、点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()
        with allure.step('6、断言'):
            expect(page.locator("text=操作成功")).to_be_visible(timeout=2000)
            expect(page.locator("text=操作成功")).to_contain_text('成功')
        # page.wait_for_timeout(2000)

    @allure.title('添加合同失败（5位中文的姓名）')
    def test_add2(self, login):
        page = login
        page.reload()

        with allure.step('1、进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        with allure.step('2、输入手机号、合同编号、5位中文姓名'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三李四王')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(self.te)
        with allure.step('3、选择学科与课程'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
            page.get_by_role("listitem").filter(has_text="Java").click()
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
            page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        with allure.step('4、上传合同'):
            with page.expect_file_chooser() as fc_info:
                page.get_by_role("button", name="上传").click()
            file_chooser = fc_info.value
            file_chooser.set_files(self.pdf)
        with allure.step('5、点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()
        with allure.step('6、断言'):
            expect(page.locator("text=请输入真实的客户姓名")).to_be_visible(timeout=2000)
            expect(page.locator("text=请输入真实的客户姓名")).to_contain_text('请输入真实的客户姓名')
        # page.wait_for_timeout(2000)

    @allure.title('添加合同失败（手机号非11位数字）')
    def test_add3(self, login):
        page = login
        page.reload()

        with allure.step('1、进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        with allure.step('2、输入姓名、合同编号、12位手机号'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('132123412345')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(self.te)
        with allure.step('3、选择学科与课程'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
            page.get_by_role("listitem").filter(has_text="Java").click()
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
            page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        with allure.step('4、上传合同'):
            with page.expect_file_chooser() as fc_info:
                page.get_by_role("button", name="上传").click()
            file_chooser = fc_info.value
            file_chooser.set_files(self.pdf)
        with allure.step('5、点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()
        with allure.step('6、断言'):
            expect(page.locator("text=请输入正确的客户手机号")).to_be_visible(timeout=2000)
            expect(page.locator("text=请输入正确的客户手机号")).to_contain_text('请输入正确的客户手机号')
        # page.wait_for_timeout(2000)

    @allure.title('添加合同失败（合同编号为空）')
    def test_add4(self, login):
        page = login
        page.reload()

        with allure.step('1、进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        with allure.step('2、输入姓名、手机号'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
        with allure.step('3、选择学科与课程'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
            page.get_by_role("listitem").filter(has_text="Java").click()
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
            page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        with allure.step('4、上传合同'):
            with page.expect_file_chooser() as fc_info:
                page.get_by_role("button", name="上传").click()
            file_chooser = fc_info.value
            file_chooser.set_files(self.pdf)
        with allure.step('5、点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()
        with allure.step('6、断言'):
            expect(page.locator("text=合同编号不能为空")).to_be_visible(timeout=2000)
            expect(page.locator("text=合同编号不能为空")).to_contain_text('合同编号不能为空')
        # page.wait_for_timeout(2000)

    @allure.title('添加合同失败（未上传合同）')
    def test_add5(self, login):
        page = login
        page.reload()

        with allure.step('1、进入添加合同页面'):
            page.get_by_role("button", name="添加合同").click()
        with allure.step('2、输入姓名、12位手机号、合同编号'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(self.te)
        with allure.step('3、选择学科与课程'):
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
            page.get_by_role("listitem").filter(has_text="Java").click()
            page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
            page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()

        with allure.step('4、点击确定'):
            page.wait_for_timeout(2000)
            page.get_by_role("button", name="确 定").click()
        with allure.step('5、断言'):
            expect(page.locator("text=请上传合同")).to_be_visible(timeout=2000)
            expect(page.locator("text=请上传合同")).to_contain_text('请上传合同')
        page.wait_for_timeout(2000)

if __name__ == '__main__':
    pytest.main([__file__])