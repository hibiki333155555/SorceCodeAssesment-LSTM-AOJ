n = int(input())
a = list()
for i in range(120):
	a.append(0)
for i in range(n):
	b, f, r, v = map(int, input().split())
	a[(b - 1) * 30 + (f - 1) * 10 + (r - 1)] += v
for i in range(4):
	if i >= 1:
		print("#" * 20)
	for j in range(3):
		for k in range(10):
			print(' ', end = '')
			print(a[i * 30 + j * 10 + k], end = '')
		print()
