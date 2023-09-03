def solution(food):
    # 배열
    answer = ''
    for idx,i in enumerate(food[1:]):
        answer += (i//2)*str(idx+1)
    
    answer = answer+"0"+answer[::-1]
    return answer