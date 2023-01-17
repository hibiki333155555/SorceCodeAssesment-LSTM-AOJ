import sys
readline = sys.stdin.readline
write = sys.stdout.write
N = int(readline())
write("0:\n")
for i in range(1, 1 << N):
    write("%d: %s\n" % (i, " ".join(str(j) for j in range(N) if i & (1 << j))))
