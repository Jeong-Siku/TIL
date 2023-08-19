def solution(array):
    cnt = dict()
    for i in array:
        if i in cnt:
            cnt[i] +=1
        else:
            cnt[i] = 1
        
    max_cnt = -1
    max_key = 0
    for i in cnt:
        if cnt[i] > max_cnt:
            max_cnt = cnt[i]
            max_key = i
        elif cnt[i] == max_cnt:
            max_key = -1
    
    return max_key
            