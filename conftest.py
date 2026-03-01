import os

def pytest_sessionfinish():
    os.system("allure generate ./allure-results -o ./allure")
    # os.system("allure generate ./allure-results -o ./allure -c")