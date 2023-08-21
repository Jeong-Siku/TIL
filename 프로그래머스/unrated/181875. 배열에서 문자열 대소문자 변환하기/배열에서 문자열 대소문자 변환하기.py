def solution(strArr):
    answer = []
    for idx,i in enumerate(strArr):
        if idx%2:
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return answer