def solution(n):
    answer = []
    while n!=0:
        answer.append(n%3)
        n//=3
    
    result=0
    for idx,num in enumerate(answer):
        result+=answer[::-1][idx]*(3**idx)
    
    # int(num,진수)
        
    return result