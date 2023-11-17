import sys
input = sys.stdin.readline
n, k = map(int,input().rstrip().split())

per_value = [0 for _ in range(k+1)]

for _ in range(n):
    w, v = map(int,input().rstrip().split())
    for j in range(k,0,-1):
        if w<=j: # 해당 조건을 주지 않으면 j-w가 -가 되어 인덱스의 위치가 꼬일 수 있다.
            per_value[j] = max(per_value[j],per_value[j-w]+v) # top->bottom

print(per_value[k])
