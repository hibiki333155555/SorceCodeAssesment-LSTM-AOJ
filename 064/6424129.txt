while True:
	x = int(input())
	if x == 0:
		break
	numstr = str(x)
	sum = 0
	for i in numstr:
		sum += int(i)
	print(sum)
