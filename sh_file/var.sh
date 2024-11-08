str="Hello, World!"
echo $str

num=5
result=$((num + 3))
echo $result  # 输出 8

array=(1 2 3 4 5)
echo ${array[0]}  # 输出 1

var='yes'

if [ "$var" = "yes" ]; then
    echo "True"
else
    echo "False"
fi

declare -A myArray
myArray["name"]="Alice"
myArray["age"]=25
echo ${myArray["name"]}  # 输出 Alice
