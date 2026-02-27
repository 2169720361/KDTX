import logging
import time
import os



def logger(path,name):
    a01 = logging.getLogger(name)
    a01.setLevel(logging.DEBUG)
    if not a01.handlers:
        b11 = logging.StreamHandler()
        b11.setLevel(logging.DEBUG)
        c01 = logging.Formatter('执行时间：%(asctime)s\t用例编号：%(name)s\t日志级别：%(levelname)s\t日志内容：%(message)s')
        b11.setFormatter(c01)

        b21 = logging.FileHandler(path, encoding='utf-8')
        b21.setLevel(logging.DEBUG)
        b21.setFormatter(c01)

        a01.addHandler(b11)
        a01.addHandler(b21)
    return a01



path0 = os.path.dirname(os.path.dirname(__file__))
path1 = path0 + os.sep + 'Logs'

time1 = time.strftime("%Y-%m-%d",time.localtime())
path2 = time1 + '.log'

path = path1 + os.sep + path2


def log0(name=__file__):
    logger01 = logger(path,name)
    return logger01
if __name__ == "__main__":
    print(f'目录：{path1}\n当前时间：{time1}\n日志名称：{path2}\n日志的路径：{path}')
    log0().debug("我是debug级日志：用于打印程序调试的详细数据/细节信息")