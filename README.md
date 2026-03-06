# 客达天下CRM系统自动化测试

## 项目简介
本项目为“客达天下”CRM系统的自动化测试项目，覆盖 **合同管理**、**登录模块** 等核心业务。通过**接口自动化**与**UI自动化**相结合，实现业务回归与数据验证，并集成至 **GitHub Actions** 持续运行。

---

## 技术栈
- **编程语言**：Python 3.10  
- **测试框架**：Pytest（接口）、Playwright（UI）  
- **工具库**：Requests、PyYAML、Allure  
- **持续集成**：GitHub Actions  

---

## 项目结构
```
KDTX/
├── .github/workflows/           # GitHub Actions 配置
│   └── ci.yml
├── Logs                         # 日志
├── test_api/                    # 接口自动化测试用例
│   ├── test_login.py                # 登录模块
│   ├── test_ht_Add.py               # 合同添加
│   ├── test_ht_Search.py            # 合同查询
│   └── test_htgl.py                 # 业务流程
├── test_ui/                     # UI自动化测试用例
│   └── test_UI_ht_Add.py            # 合同添加UI流程
├── utils/                       # 工具类封装
│   ├── Asser_Util.py                 # 断言工具
│   ├── Log_Util.py                   # 日志工具
│   ├── Requests_Util.py              # HTTP请求封装
│   └── Yaml_Util.py                  # YAML数据读取
├── Yaml/                        # 测试数据
│   ├── login.yaml
│   ├── Add.yaml
│   └── Search.yaml
├── conftest.py                    # pytest钩子函数
├── pytest.ini                     # pytest配置
├── requirements.txt               # 项目依赖
└── README.md                      # 项目说明
```

> **注**：`allure/`、`allure-results/`目录为运行测试后自动生成，不包含在版本控制中。

---

## 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/2169720361/KDTX.git
cd KDTX
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
# 安装 Playwright 浏览器（仅UI测试需要）
playwright install chromium
```

### 3. 运行测试
```bash
# 运行所有接口测试
pytest test_api/

# 运行所有UI测试（默认有界面）
pytest test_ui/

# 运行所有测试（接口+UI）
pytest test_*/
```

### 4. 生成Allure报告
```bash
# 运行测试时已自动生成测试报告（在 allure 目录）
# 打开 allure 目录
python3 -m http.server 8080
# 打开浏览器，访问 http://localhost:8080/，即可看到完整的 Allure 报告
```

---

## 持续集成
本项目已集成 **GitHub Actions**，每次推送至 `main` 分支或创建 PR 时自动运行全部测试，并生成 Allure 报告作为构建产物下载。 

---

## 测试成果
- **接口自动化用例**：52条（覆盖登录、合同增/查、业务流程）
- **UI自动化用例**：5条（核心正向流程 + 典型异常）
- **发现缺陷**：通过接口测试发现后端校验缺失缺陷10个
- **持续集成**：单次CI运行时间约3分钟，自动生成可视化报告。

---

## 许可证
本项目仅供学习交流使用。
