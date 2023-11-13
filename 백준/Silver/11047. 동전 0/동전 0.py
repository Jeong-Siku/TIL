import sys
input = sys.stdin.readline
n, k = map(int,input().rstrip().split())
arr = []
for _ in range(n):
    num = int(input().rstrip())
    if num<=k:
        arr.append(num)
arr.sort(reverse=True)

result = 0
for i in arr:
    result+=k//i
    r = k%i
    k = r
print(result)