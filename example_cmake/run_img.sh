#!/bin/sh

i=0

while [ $i -le 10 ]
do
	echo "run code"
	echo $i
	./opencv_example
	i++
done

echo "finish"
