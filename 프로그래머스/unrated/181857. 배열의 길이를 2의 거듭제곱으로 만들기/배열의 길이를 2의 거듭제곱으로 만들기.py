def solution(arr):
    answer = []
    arr_2 = [2**i for i in range(0,11)]
    
    for i in arr_2:
        answer.append(i - len(arr))
        
    arr+=[0]*[i for i in answer if i>=0][0]
    
    return arr

def solution(arr):
    n = 1
    while n < len(arr):
        n*=2
    return  arr+[0]*(n-len(arr))