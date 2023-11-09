import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))+[0]
s = [0]

for i in range(len(arr)):
    s.append(s[i]+arr[i])

for _ in range(m):
    i,j = map(int,input().rstrip().split())
    print(s[j]-s[i-1])