for item in apple banana orange;do
    echo $item
done

#!/bin/bash

for line in $(cat abc.txt)
do
  echo "Line: $line"
done

for i in $(seq 1 5)
do
  echo "Number: $i"
done

#!/bin/bash

for ((i=1; i<=5; i++));do
  echo "Counter: $i"
done

