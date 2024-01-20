import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

stack = [0]
result = []
start=1
for i in range(n): 
    while stack[-1]<arr[i]:
        stack.append(start)
        result.append('+')
        start+=1
    stack.pop()
    result.append('-')
    
if len(stack)>=2:
    print('NO')
else:
    for i in result:
        print(i)