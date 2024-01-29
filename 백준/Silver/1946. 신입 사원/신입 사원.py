import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort() # 각 성적의 순위이기때문에 낮은 수 일수록 높은 점수. 

    top = scores[0][1]
    selected = 1 # 서류심사 1위는 무조건 선발되기때문에 1
    for i in range(1,n):
        if scores[i][1] < top:
           selected += 1
           top = scores[i][1]

    print(selected)    