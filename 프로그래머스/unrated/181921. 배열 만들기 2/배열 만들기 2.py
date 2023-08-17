def solution(l, r):
    answer = []
    for i in range(l,r+1):
        num=str(i)
        if all(j in "05" for j in num):
            answer.append(i)
            
    return [-1] if answer==[] else answer
   
