# import pytest
# import time
# import os
#
#
# @pytest.fixture(autouse=True,scope='session')
# def allure():
#     print('===正在生成测试报告===')
#     yield
#     os.system("allure generate ./allure-results -o ./allure -c")
#     print('===测试报告生成完毕===')