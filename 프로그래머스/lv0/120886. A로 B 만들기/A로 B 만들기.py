from collections import defaultdict
def solution(before, after):
    # 중복값 존재 replace x
    # 원소개수가 동일한지 확인 필요
    dic = defaultdict(int)
    for i in before:
        dic[i]+=1
    
    for i in after:
        if after.count(i) !=dic[i]:
            return 0
    return 1