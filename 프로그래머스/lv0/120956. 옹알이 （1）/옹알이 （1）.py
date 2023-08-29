from itertools import permutations
def solution(babbling):
    answer = 0
    result = ["aya","ye","woo","ma"]
    possible=["aya","ye","woo","ma"]
    result+=["".join(i) for i in permutations(possible,4)]
    result+=["".join(i) for i in permutations(possible,3)]
    result+=["".join(i) for i in permutations(possible,2)]
    
    for i in babbling:
        if i in result:
            answer+=1
    return answer