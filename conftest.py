import os

def pytest_sessionfinish():
    os.system("allure generate ./allure-results -o")