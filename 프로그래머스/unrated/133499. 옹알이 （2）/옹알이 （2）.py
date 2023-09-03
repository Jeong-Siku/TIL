def solution(babbling):
    answer = 0
    word = ["aya","ye","woo","ma"]
    for i in babbling:
        for j in word:
            if j*2 in i:
                continue
            i = i.replace(j,"1")
        if i.isdigit():
            answer+=1
    return answer