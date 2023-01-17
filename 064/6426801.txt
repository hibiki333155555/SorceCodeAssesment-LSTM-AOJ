N = int(input())
x = 0

for i in range(1,N+1):

    if i%3 == 0:
            print(" %d"%i,end = "");
    else:
        x = i
        while (x):
            if x%10 == 3:
                print(" %d"%i,end = "")
                break
            x //= 10
print()
