#!/bin/bash

# 读取用户输入
read -p "请输入一个数字: " num

# if 分支处理
if [ $num -gt 10 ]; then
    echo "数字大于10"
elif [ $num -eq 10 ]; then
    echo "数字等于10"
else
    echo "数字小于10"
fi
