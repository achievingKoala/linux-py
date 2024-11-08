#!/bin/bash

# 定义一个函数
add_numbers() {
    local sum=$(( $1 + $2 ))  # 使用local定义局部变量
    echo "Sum: $sum"
}

# 检查参数个数
if [ "$#" -ne 2 ]; then
    echo "用法: $0 <数字1> <数字2>"
    # exit 1
else
    # 调用函数
    add_numbers "$1" "$2"
fi

