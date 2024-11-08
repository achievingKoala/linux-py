# 定义变量
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# 默认目标，创建虚拟环境并安装依赖
.PHONY: all
all: install

# 创建虚拟环境
.PHONY: venv
venv:
	python3 -m venv $(VENV)

# 安装依赖
.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

# 运行程序
.PHONY: run
run:
	$(PYTHON) gpt_domo.py

# 运行测试
.PHONY: test
test:
	$(PYTHON) -m unittest discover -s tests

# 格式化代码 (使用 black)
.PHONY: format
format:
	$(PYTHON) -m black src tests

# 清理文件
.PHONY: clean
clean:
	rm -rf $(VENV) __pycache__ **/__pycache__

# 删除依赖并重新安装
.PHONY: reinstall
reinstall: clean install
