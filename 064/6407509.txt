alp = [0 for i in range(26)] #1次元配列の初期化
while True:
	try:
		str = input().lower()
	except:
		break
	for i in str:
		num = ord(i) - ord('a') #for i in strにおける i はstrの最初からの文字になる→０からの数字ではない！
		if num >= 0 and num < 26:
			alp[num] += 1

for i in range(26):
	print("%s : %d" % (chr(ord('a') + i), alp[i]))
