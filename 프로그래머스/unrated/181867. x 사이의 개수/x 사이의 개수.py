def solution(myString):
    splited = myString.split("x")
    answer = []
    for i in splited:
        answer.append(len(i))
    
    return answer