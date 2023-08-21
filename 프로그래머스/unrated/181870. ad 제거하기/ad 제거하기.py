def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" in i:
            continue
        answer.append(i)
    return answer

def solution(strArr):
    return [i for i in strArr if "ad" not in i]