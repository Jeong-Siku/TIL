def solution(num_list):
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if num_list[i]%2==0:
            even+=1
        else:
            odd+=1
    return [even,odd]

def solution(num_list):
    answer = [0,0]
    for i in num_list:
        answer[i%2]+=1
    return answer