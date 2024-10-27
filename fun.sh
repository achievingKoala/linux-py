#!/bin/bash

# 定义一个函数
add_numbers() {
    local sum=$(( $1 + $2 ))  # 使用local定义局部变量
    echo "Sum: $sum"
}

# 提示用户输入两个数字
read -p "请输入第一个数字: " num1
read -p "请输入第二个数字: " num2

# 调用函数
add_numbers "$num1" "$num2"
