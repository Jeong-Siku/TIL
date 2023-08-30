def solution(i, j, k):
    # 등장 횟수
    # 범위
    # 원소가 크다. 다이나믹 프로그래밍
    cnt = 0 
    for i in range(i,j+1):
        cnt+=str(i).count(str(k))
    return cnt

def solution(i, j, k):
    return sum(str(i).count(str(k)) for i in range(i,j+1))