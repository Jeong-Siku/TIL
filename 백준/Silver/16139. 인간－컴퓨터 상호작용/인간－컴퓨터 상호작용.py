import sys
input = sys.stdin.readline
s = input().rstrip()
q = int(input().rstrip())
for _ in range(q):
    a, l, r = input().rstrip().split()
    l, r = int(l), int(r)
    print(s[l:r+1].count(a))