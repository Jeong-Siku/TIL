import sys
input = sys.stdin.readline
n = int(input())
count = [0]*(10001)
for _ in range(n):
    i = int(input())
    count[i]+=1

for i in range(1,10001):
    while count[i]:
        count[i]-=1
        print(i)