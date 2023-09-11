def solution(nums):
    nums.sort()
    
    mod_2 = []
    for i in range(2,3001):
        list_1 = []
        for j in range(1,i+1):
            if i%j==0:
                list_1.append(j)
        if len(list_1)==2:
            mod_2.append(i)
    
    result = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] in mod_2:
                    result+=1
        
    return result


def solution(nums):
    from itertools import combinations
    result=0
    for i in combinations(nums,3):
        cb = sum(i)
    # 소수 구별하기
    # 2~사이값으로 나눠지면 소수가 아님
    # for - else 문법
        for j in range(2,cb):
            if cb%j==0:
                break
        else:
            result+=1
    return result