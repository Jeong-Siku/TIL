def solution(absolutes, signs):
    answer = []
    for num,sig in zip(absolutes,signs):
        if sig:
            answer.append(num)
        else:
            answer.append(-num)
    return sum(answer)