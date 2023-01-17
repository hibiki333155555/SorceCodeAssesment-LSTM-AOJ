import string
import sys

words = sys.stdin.read().lower()
for i in range(26):
    alp = string.ascii_lowercase[i]
    print("%s : %d" % (alp, (words.count(alp))))
