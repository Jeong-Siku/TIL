import sys
input = sys.stdin.readline

n = int(input())
exp_rnks = sorted([int(input()) for _ in range(n)])
rnks = [i for i in range(1,n+1)]

ans = 0
for exp, ori in zip(exp_rnks,rnks):
    ans+=abs(exp-ori)
print(ans)