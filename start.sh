#!/bin/bash

# Linux命令学习系统启动脚本
# Author: Linux Learning System
# Version: 1.0

set -e  # 遇到错误时退出

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查Python是否安装
check_python() {
    if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
        print_error "Python未安装，请先安装Python 3.7+"
        exit 1
    fi
    print_success "Python环境检查通过"
}

# 检查pip是否安装
check_pip() {
    if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
        print_error "pip未安装，请先安装pip"
        exit 1
    fi
    print_success "pip环境检查通过"
}

# 安装依赖
install_dependencies() {
    print_info "正在安装Python依赖..."
    if command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt
    else
        pip install -r requirements.txt
    fi
    print_success "依赖安装完成"
}

# 启动后端服务
start_backend() {
    print_info "正在启动后端API服务器..."
    if command -v python3 &> /dev/null; then
        python3 app.py &
    else
        python app.py &
    fi
    BACKEND_PID=$!
    print_success "后端服务已启动 (PID: $BACKEND_PID)"
}

# 等待服务启动
wait_for_service() {
    print_info "等待服务启动..."
    sleep 3
    
    # 检查服务是否正常运行
    if curl -s http://localhost:5001/api/health > /dev/null 2>&1; then
        print_success "服务启动成功"
    else
        print_warning "服务可能未完全启动，请稍等片刻"
    fi
}

# 打开前端页面
open_frontend() {
    print_info "正在打开前端页面..."
    
    # 获取当前目录的绝对路径
    CURRENT_DIR=$(pwd)
    HTML_FILE="file://$CURRENT_DIR/index.html"
    
    if command -v open &> /dev/null; then
        # macOS
        open "$HTML_FILE"
        print_success "已在默认浏览器中打开前端页面"
    elif command -v xdg-open &> /dev/null; then
        # Linux
        xdg-open "$HTML_FILE"
        print_success "已在默认浏览器中打开前端页面"
    elif command -v start &> /dev/null; then
        # Windows (Git Bash)
        start "$HTML_FILE"
        print_success "已在默认浏览器中打开前端页面"
    else
        print_warning "无法自动打开浏览器，请手动打开: $HTML_FILE"
    fi
}

# 显示服务信息
show_info() {
    echo
    echo "=================================="
    print_success "Linux命令学习系统已启动！"
    echo "=================================="
    echo "📡 后端API: http://localhost:5001"
    echo "🌐 前端页面: 已在浏览器中打开"
    echo "📚 健康检查: http://localhost:5001/api/health"
    echo
    print_info "按 Ctrl+C 停止服务"
    echo
}

# 清理函数
cleanup() {
    print_info "正在停止服务..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
        print_success "后端服务已停止"
    fi
    exit 0
}

# 设置信号处理
trap cleanup SIGINT SIGTERM

# 主函数
main() {
    echo "🐧 Linux命令学习系统启动脚本"
    echo "=============================="
    
    check_python
    check_pip
    install_dependencies
    start_backend
    wait_for_service
    open_frontend
    show_info
    
    # 保持脚本运行
    wait
}

# 运行主函数
main