def solution(spell, dic):
    answer = 0
    for word in dic:
        cnt=0
        for alp in spell:
            if alp in word:
                cnt+=1
        if cnt==len(spell):
            return 1
    return 2