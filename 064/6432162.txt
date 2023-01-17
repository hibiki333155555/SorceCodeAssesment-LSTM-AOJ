a,b,c = map(int,input().split())

ans = 0
num = a

while True:
    if c%num == 0:
        ans += 1
    num += 1
    if num > b:
        break

print(ans)
