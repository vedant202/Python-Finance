#!/bin/bash
echo "Hello"

files=$('ls')


# echo $files
dir="wheel_files"

if [ -d "$dir" ];
then
	echo "Directory already exists"
else
	mkdir -p $dir
	echo "$dir is created"
fi


for file in $files
do
	
	ext="${file##*.}"
	if [ "$ext" = "whl" ];
	then
		echo $ext
		mv $file ./wheel_files
	fi
	# echo $ext
done
