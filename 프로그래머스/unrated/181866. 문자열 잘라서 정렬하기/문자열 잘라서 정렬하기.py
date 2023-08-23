def solution(myString):
    a = sorted(myString.split("x"))
    answer= []
    for i in range(len(a)):
        if a[i] =="":
            continue
        answer.append(a[i])
    return answer

def solution(myString):
    return sorted([i for i in myString.split("x") if i])