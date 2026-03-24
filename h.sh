my_func(){
	echo hi
	echo hello
	echo patil
}
p=$(my_func| tail -n 1)
echo $p
