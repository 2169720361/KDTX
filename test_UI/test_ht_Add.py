import os
import time
import pytest


from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def te():
    te1 = time.strftime("%m-%d %H:%M:%S", time.localtime())
    yield te1


@pytest.fixture(autouse=True,scope="class")
def login():
    with sync_playwright() as p:
        a = p.firefox.launch(headless=False)
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


class Test_ht_Add:
    path = os.path.dirname(__file__)
    pdf = path + os.sep + '1.pdf'

    def test_add(self,login,te):
        page = login

        page.get_by_role("button", name="添加合同").click()
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(te)
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
        page.get_by_role("listitem").filter(has_text="Java").click()
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
        page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()

        with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="上传").click()
        file_chooser = fc_info.value
        file_chooser.set_files(self.pdf)

        # page.get_by_role("button", name="确 定").click()

        page.wait_for_timeout(2000)

    def test_add1(self,login,te):
        page = login

        page.get_by_role("button", name="添加合同").click()
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户姓名").fill('张三')
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入客户手机号").fill('13212341234')
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请输入合同编号").fill(te)
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买学科").click()
        page.get_by_role("listitem").filter(has_text="Java").click()
        page.get_by_role("dialog", name="添加合同").get_by_placeholder("请选择购买课程").click()
        page.locator('xpath=/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()

        with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="上传").click()
        file_chooser = fc_info.value
        file_chooser.set_files(self.pdf)

        # page.get_by_role("button", name="确 定").click()

        page.wait_for_timeout(2000)




if __name__ == '__main__':
    pytest.main([__file__])