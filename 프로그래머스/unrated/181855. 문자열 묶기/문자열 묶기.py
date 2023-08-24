def solution(strArr):
    ele_num = {i:0 for i in range(1,31)}
    for i in strArr:
        ele_num[len(i)]+=1
    return max(ele_num.values())

def solution(strArr):
    ele_num = {}
    for i in strArr:
        ele_num[len(i)] = ele_num.get(len(i),0)+1
    return max(ele_num.values())

def solution(strArr):
    ele_num = [0]*31
    for i in strArr:
        ele_num[len(i)]+=1
    return max(ele_num)