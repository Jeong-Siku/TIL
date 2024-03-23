a, b = input().split()
gap = len(b)-len(a)

if gap==0:
    cnt = 0
    for i in range(len(b)):
        if a[i]!=b[i]:
            cnt+=1
    print(cnt)
else:
    min_cnt = float('inf')
    for i in range(gap+1):
        cnt=0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt+=1
        min_cnt=min(min_cnt,cnt)
    print(min_cnt)