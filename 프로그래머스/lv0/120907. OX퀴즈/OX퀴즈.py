def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.replace("=","==")):
            answer.append("O")
        else:
            answer.append("X")
    return answer