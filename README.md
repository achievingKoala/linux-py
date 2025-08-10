# Linux命令学习系统

一个基于Web的Linux命令学习和练习系统，帮助用户通过分类练习掌握Linux命令。

## 功能特性

- 🎯 **分类学习**: 按命令类型分类练习（Find、Grep、Docker、进程管理等）
- 🎲 **随机练习**: 随机选择命令进行练习
- 📊 **学习记录**: 记录学习进度和正确率
- 🎨 **友好界面**: 简洁直观的Web界面
- 📱 **响应式设计**: 支持不同设备访问

## 项目结构

```
linux-py/
├── app.py                 # Flask后端API
├── index.html            # 前端页面
├── requirements.txt      # Python依赖
├── start.sh             # 启动脚本
├── Dockerfile           # Docker配置
├── csv/                 # 数据文件
│   ├── command_data.csv # 命令数据
│   └── count.csv        # 学习记录
├── sh_file/             # Shell脚本示例
└── utils/               # 工具模块
    ├── query_csv.py     # 数据查询
    └── record_csv.py    # 记录管理
```

## 快速开始

### 方法1: 使用启动脚本
```bash
chmod +x start.sh
./start.sh
```

### 方法2: 手动启动
```bash
# 安装依赖
pip install -r requirements.txt

# 启动后端
python app.py

# 在浏览器中打开 index.html
```

### 方法3: Docker部署
```bash
docker build -t linux-learning .
docker run -p 8080:8080 linux-learning
```

## API接口

- `GET /api/commands/<category>` - 获取指定类别的命令
- `GET /api/commands/random` - 获取随机命令
- `GET /api/categories` - 获取所有类别
- `POST /api/record` - 记录学习结果

## 支持的命令类别

- **find_commands** - Find命令
- **grep_commands** - Grep命令  
- **docker_basic_commands** - Docker基础
- **process_commands** - 进程管理
- **user_group_commands** - 用户组管理
- **archive_commands** - 压缩归档
- **service_commands** - 服务管理
- 更多类别...

## 测试

### 运行测试
```bash
# 运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=app --cov-report=html

# 运行特定测试
pytest test_app.py::test_health_check -v
```

### CI/CD
项目配置了GitHub Actions自动化流程：
- 代码推送时自动运行测试
- 测试通过后构建Docker镜像
- 支持代码质量检查

## 开发说明

### 添加新命令
1. 在 `csv/command_data.csv` 中添加命令数据
2. 重启服务即可生效

### 数据格式
```csv
id,command_group,command,description,ignore
1,find_commands,find /dir -name 'filename',查找指定名称的文件,
```

## 技术栈

- **前端**: HTML5, CSS3, JavaScript
- **后端**: Python Flask
- **数据**: CSV文件存储
- **部署**: Docker支持

## 许可证

MIT License