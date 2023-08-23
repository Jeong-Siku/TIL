def solution(myString):
    a = sorted(myString.split("x"))
    answer= []
    for i in range(len(a)):
        if a[i] =="":
            continue
        answer.append(a[i])
    return answer