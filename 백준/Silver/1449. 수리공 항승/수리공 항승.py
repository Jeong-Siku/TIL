n, l = map(int,input().split())
pour = list(map(int,input().split()))
pour.sort()
# 길이
dist = 1
# 테이프
ans = 1
for i in range(n-1):
    dist += pour[i+1]-pour[i]
    if dist>l:
        ans+=1
        dist=1
    else:
        continue

print(ans)