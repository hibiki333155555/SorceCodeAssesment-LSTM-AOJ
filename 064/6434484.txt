def calc(a, b):
	d = a // b
	r = a % b
	f = float(a/b)
	return(d, r, f)

a, b = map(int, input().split())
print("%d %d %f" % (calc(a, b)))
