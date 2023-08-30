def solution(i, j, k):
    # 등장 횟수
    # 범위
    # 원소가 크다. 다이나믹 프로그래밍
    cnt = 0 
    for i in range(i,j+1):
        cnt+=str(i).count(str(k))
    return cnt

# 1 2 3 4 5 6 7 8 9 
# 10 11 12 13 14 15 16 17 18 19