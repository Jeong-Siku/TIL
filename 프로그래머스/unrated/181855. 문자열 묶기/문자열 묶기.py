def solution(strArr):
    ele_num = {i:0 for i in range(1,31)}
    for i in strArr:
        ele_num[len(i)]+=1
    
        
    return max(ele_num.values())