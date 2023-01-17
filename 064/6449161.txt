while True:
    s=input()
    if s=="-":break
    m=int(input())
    for i in range(m):
        h=int(input())
        le=s[0:h]
        ri=s[h:]
        s=ri+le
    print(s)
