from utils.Log_Util import log0


class Ass:
    def __init__(self, name='Assert'):
        self.log = log0(name)

    def code(self, expected_code, code):
        try:
            assert int(expected_code) == int(code)
            self.log.debug('HTTP状态码断言通过')
            return True
        except:
            self.log.error(f'HTTP状态码断言失败，预期状态码：{expected_code}，实际状态码：{code}')
            raise Exception('HTTP状态码断言失败')

    def bo(self, expected_body, body):
        try:
            assert expected_body in body
            self.log.debug('响应体 包含 断言通过')
            return True
        except:
            self.log.error(f'响应体 包含 断言失败，预期包含内容：{expected_body}，实际响应体：{body}')
            raise Exception('响应体 包含 断言失败')

    def dy(self, expected_body, body):
        bool1 = body > 0
        try:
            assert expected_body == bool1
            self.log.debug('响应体 相等 断言通过')
            return True
        except:
            self.log.error(f'响应体 相等 断言失败，预期响应体：{expected_body}，实际响应体：{bool1, body}')
            raise Exception('响应体 相等 断言失败')

    def code2(self, expected_code, code):
        try:
            assert int(expected_code) == int(code)
            self.log.debug('业务状态码断言通过')
            return True
        except:
            self.log.error(f'业务状态码断言失败，预期状态码：{expected_code}，实际状态码：{code}')
            raise Exception('业务状态码断言失败')