# Linux命令学习系统 Makefile

.PHONY: help install start stop clean test docker-build docker-run docker-stop

# 默认目标
help:
	@echo "Linux命令学习系统 - 可用命令:"
	@echo "  install      - 安装依赖"
	@echo "  start        - 启动开发服务器"
	@echo "  stop         - 停止服务器"
	@echo "  clean        - 清理临时文件"
	@echo "  test         - 运行测试"
	@echo "  docker-build - 构建Docker镜像"
	@echo "  docker-run   - 运行Docker容器"
	@echo "  docker-stop  - 停止Docker容器"

# 安装依赖
install:
	@echo "安装Python依赖..."
	pip install -r requirements.txt

# 启动开发服务器
start:
	@echo "启动Linux命令学习系统..."
	chmod +x start.sh
	./start.sh

# 停止服务器
stop:
	@echo "停止服务器..."
	pkill -f "python.*app.py" || true

# 清理临时文件
clean:
	@echo "清理临时文件..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.log" -delete
	find . -type f -name ".DS_Store" -delete

# 运行测试
test:
	@echo "运行测试..."
	python -m pytest tests/ -v || echo "没有找到测试文件"

# Docker相关命令
docker-build:
	@echo "构建Docker镜像..."
	docker build -t linux-learning:latest .

docker-run:
	@echo "运行Docker容器..."
	docker run -d --name linux-learning -p 8080:8080 linux-learning:latest

docker-stop:
	@echo "停止Docker容器..."
	docker stop linux-learning || true
	docker rm linux-learning || true

# 使用docker-compose
compose-up:
	@echo "使用Docker Compose启动..."
	docker-compose up -d

compose-down:
	@echo "使用Docker Compose停止..."
	docker-compose down

# 开发环境设置
dev-setup: install
	@echo "开发环境设置完成"

# 生产环境部署
deploy: docker-build
	@echo "部署到生产环境..."
	docker-compose -f docker-compose.yml up -d