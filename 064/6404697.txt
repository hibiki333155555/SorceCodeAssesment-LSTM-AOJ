a, b, c = map(int, input().split())
cnt = 0
for x in range(a, b + 1):
    if c % x == 0:
        cnt += 1
print(cnt)
