#!/bin/bash
prefix="day_"
dir=$prefix$1

python_file="main.py"
input_file="input.txt"

check_argument () {
	if [ -z $1 ]
	then
		finish "Argument is missing."
	fi
}

check_directory() {
	if [ ! -d $1 ]; then
		finish "Directory doesn't exist."
	else
		cd $dir
	fi
}

check_input() {
	if [ ! -f $1 ]
	then
		finish "$1 doesn't exist."
	fi
}

check_python() {
	if [ ! -f $1 ]; then
		finish "$1 doesn't exist."
	else
		python $1
		finish
	fi
}

finish() {
	echo $1
	echo "Done..."
	exit 1
}

check_argument $1
check_directory $dir
check_input $input_file
check_python $python_file

