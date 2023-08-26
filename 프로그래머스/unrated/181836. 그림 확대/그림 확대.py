def solution(picture, k):
    answer=[]
    for i in picture:
        elem = ""
        for j in i:
            elem+=j*k
        for _ in range(k):
            answer.append(elem)
    return answer