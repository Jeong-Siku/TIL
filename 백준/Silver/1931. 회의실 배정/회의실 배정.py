import sys
input = sys.stdin.readline

n = int(input().rstrip())
sch = []
for _ in range(n):
    sch.append(list(map(int,input().rstrip().split())))

sch.sort(key= lambda x : (x[1],x[0]))

cnt=0
pre_e=0
for post_s,post_e in sch:
    if post_s>=pre_e:
        cnt+=1
        pre_e=post_e
print(cnt)