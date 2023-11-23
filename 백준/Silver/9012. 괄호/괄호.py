from collections import deque
t = int(input())
for _ in range(t):
    in_data = input()
    q = deque()
    for i in in_data:
        if i == "(":
            q.append(i)
        else:
            if q:
                q.pop()
            else:
                print("NO")
                break
    else:
        if q:
            print("NO")
        else:
            print("YES")