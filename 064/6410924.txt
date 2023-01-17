n = int(input())
*A, = map(int, input().split())
for i in range(n):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    print(*A)

