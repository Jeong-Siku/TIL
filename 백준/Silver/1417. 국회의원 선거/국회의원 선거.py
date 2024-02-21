n = int(input())
votes = [int(input()) for _ in range(n)]

cnt = 0
while n!=1 and votes[0]<=max(votes[1:]):
    for i in range(n-1):
        if max(votes[1:]) == votes[i+1]:
            votes[i+1]-=1
            votes[0]+=1
            cnt+=1
            break

print(cnt)