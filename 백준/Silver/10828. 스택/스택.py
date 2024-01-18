from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    manual = input().split()
    if manual[0] == 'push':
        q.append(manual[1])
    elif manual[0] == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif manual[0] == 'size':
        print(len(q))
    elif manual[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif manual[0] == 'top':
        if q:
            print(q[-1])
        else:
            print(-1)