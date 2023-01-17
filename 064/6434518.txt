def calc(a, op, b):
	if op == "+":
		return a+b
	elif op == "-":
		return a-b
	elif op == "*":
		return a*b
	elif op == "/":
		return a//b

while 1:
	a, op, b = input().split()
	a = int(a)
	b = int(b)
	if op == "?":
		break
	print("%d" % (calc(a, op, b)))
