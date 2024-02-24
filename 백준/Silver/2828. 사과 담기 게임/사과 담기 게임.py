import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
apples = []
for _ in range(j):
    apples.append(int(input())-1)

left, right = 0, m-1 # 바구니 처음과 끝 위치, 중간 위치는 상관없음

ans = 0
for apple in apples:
    if right<apple:
        ans+=apple-right
        left+=apple-right
        right+=apple-right
    elif left>apple:
        ans+=left-apple
        right-=left-apple
        left-=left-apple
    
print(ans)