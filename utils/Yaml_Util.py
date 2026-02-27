import os
import yaml


def yaml0(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
    else:
        raise FileNotFoundError('文件不存在，请检查传入的参数或路径')

    return yaml_data


class yaml1:
    def __init__(self,name):
        self.path = os.path.dirname(os.path.dirname(__file__))
        self.yaml = self.path + os.sep + 'Yaml'
        self.name = name
        self.yaml_path = self.yaml + os.sep + name + '.yaml'

    def data1(self):
        yaml_data = yaml0(self.yaml_path)
        data_list = []
        for i in yaml_data[self.name]:
            id = i['id']
            title = i['title']
            url = i['url']
            data = i['data']
            expected = i['expected']
            data_list.append((id,title,url,data,expected))
        return data_list

if __name__ == '__main__':
    a = yaml1('Search').data1()
    a1 = a[0][4]['body']['total']
    print(a)
    print(a1,type(a1))