客达天下CRM系统自动化测试

📖 项目简介
本项目为“客达天下”CRM系统的自动化测试项目，覆盖 合同管理 登录模块。通过接口自动化与UI自动化相结合，实现业务回归与数据验证，并集成至GitHub Actions持续运行。

🛠️ 技术栈
编程语言：Python 3.10
- 测试框架：Pytest（接口）、Playwright（UI）
- 工具库：Requests、PyYAML、Allure
- 持续集成：GitHub Actions

📁 项目结构
KDTX/
├── .github/workflows/         # GitHub Actions 配置
│ └── ci.yml
├── allure/                    # allure报告（运行代码时自动生成该目录）
├── allure-results/            # allure报告原始数据（运行代码时自动生成该目录）
├── Logs/                      # 日志
├── test_api/                  # 接口自动化测试用例
│ ├── test_login.py               # 登录模块
│ ├── test_ht_Add.py              # 合同添加
│ ├── test_ht_Search.py           # 合同查询
│ └── test_htgl.py                # 业务流程
├── test_ui/                   # UI自动化测试用例
│ └── test_UI_ht_Add.py           # 合同添加UI流程
├── utils/                     # 工具类封装
│ ├── Asser_Util.py               # 断言工具
│ ├── Log_Util.py                 # 日志工具
│ ├── Requests_Util.py            # HTTP请求封装
│ └── Yaml_Util.py                # YAML数据读取
├── Yaml/                      # 测试数据
│ ├── login.yaml
│ ├── Add.yaml
│ └── Search.yaml
├── conftest.py                # pytest钩子函数
├── pytest.ini                 # pytest配置
├── requirements.txt           # 项目依赖
└── README.md                  # 项目说明
