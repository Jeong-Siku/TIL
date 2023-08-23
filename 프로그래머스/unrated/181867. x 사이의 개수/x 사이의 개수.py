def solution(myString):
    splited = myString.split("x")
    answer = []
    for i in splited:
        answer.append(len(i))
    return answer

def solution(myString):
    return [len(i) for i in myString.split("x")]

def solution(myString):
    return list(map(lambda x:len(x),myString.split("x")))