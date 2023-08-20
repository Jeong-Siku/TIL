def solution(num_list):
    answer = 0
    for i in num_list:
        while True:
            if i==1:
                break
                
            if i%2:
                i = (i-1)/2
                answer +=1
            else:
                i = i/2
                answer +=1
    return answer

def solution(num_list):
    answer = 0 
    for i in num_list:
        while i!=1:
            i = i//2
            answer+=1
    return answer