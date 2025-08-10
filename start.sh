#!/bin/bash

# 安装依赖
pip install -r requirements.txt

# 启动后端API
echo "启动后端API服务器..."
python app.py &

# 等待后端启动
sleep 2

# 打开前端页面
echo "打开前端页面..."
if command -v open &> /dev/null; then
    open index.html
elif command -v xdg-open &> /dev/null; then
    xdg-open index.html
else
    echo "请手动打开 index.html 文件"
fi

echo "后端API: http://localhost:5000"
echo "前端页面: 直接打开 index.html 文件"