def solution(answers):
    method_1 = [1,2,3,4,5]*2000
    method_2 = [2,1,2,3,2,4,2,5]*1700
    method_3 = [3,3,1,1,2,2,4,4,5,5]*1000
    
    method_1_cnt = 0
    method_2_cnt = 0
    method_3_cnt = 0
    
    for idx, i in enumerate(answers):
        if method_1[idx] == i:
            method_1_cnt+=1
        if method_2[idx] == i:
            method_2_cnt+=1
        if method_3[idx] == i:
            method_3_cnt+=1
             
    dic = {1:method_1_cnt,2:method_2_cnt,3:method_3_cnt}

    result=[]
    for i in dic:
        if dic[i]== max(method_1_cnt,method_2_cnt,method_3_cnt):
            print(dic[i])
            result.append(i)
    return result

def solution(answers):
    method_1 = [1,2,3,4,5]
    method_2 = [2,1,2,3,2,4,2,5]
    method_3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    
    for idx,answer in enumerate(answers):
        if answer == method_1[idx%len(method_1)]:
            cnt[0]+=1
        if answer == method_2[idx%len(method_2)]:
            cnt[1]+=1
        if answer == method_3[idx%len(method_3)]:
            cnt[2]+=1
    
    result = []
    for idx,i in enumerate(cnt):
        if i == max(cnt):
            result.append(idx+1)
    return result

