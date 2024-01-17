from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

arr = deque()
for _ in range(n):
    manual = input().split()
    if manual[0] == "push_back":
        arr.append(int(manual[1]))
    elif manual[0] == "push_front":
        arr.appendleft(int(manual[1]))
    elif manual[0] == "pop_front":
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif manual[0] == "pop_back":
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif manual[0] == "size":
        print(len(arr))
    elif manual[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif manual[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif manual[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)