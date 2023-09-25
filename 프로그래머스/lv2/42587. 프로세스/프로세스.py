from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    goal = [0 for i in range(len(priorities))]
    goal[location] = 1
    ord_p = 0
    print(goal)
    while q:
        if max(goal)==0:
            break
        if q[0] == max(q):
            q.popleft()
            del goal[0]
            ord_p+=1
        else:
            q.append(q[0])
            goal.append(goal[0])
            q.popleft()
            del goal[0]

    return ord_p