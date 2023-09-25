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

def solution(priorities, location):
    queue = deque([i for i in enumerate(priorities)])
    answer = 0
    while queue:
        cur = queue.popleft()
        # pop을 하는 순간 최고의 값이 queue배열에서 사라지므로 조건문의 순서를 잘 따질 것.
        if any(cur[1]< i[1] for i in queue):
            queue.append(cur)
        else:
            answer+=1
            if cur[0]==location:
                return answer
    return answer