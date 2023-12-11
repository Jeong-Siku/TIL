n = int(input())
arr = list(map(int,input().split()))

dp = [0]

for target in arr:
    if dp[-1]<target: # 증가하는 수는 대입
        dp.append(target)
    
    else: # 감소하는 수는 대입된 수에서 바꾼다.
        start = 0 
        end = len(dp)
        result = 0
        
        while start<=end:
            mid = (start+end)//2 # mid는 교체해야할 인덱스를 찾는 최적화값
            if dp[mid] < target:
                # result = mid
                start = mid +1
            else: # 동일한 수가 있을 시 인덱스 에러 방지를 위해 부등호를 붙인다.
                result = mid
                end=mid - 1
        dp[result] = target
print(len(dp)-1)