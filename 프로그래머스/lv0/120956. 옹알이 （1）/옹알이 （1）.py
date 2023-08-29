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

import re
def solution(babbling):
    # []와 ()는 다르다. []는 해당 위치에서 일치할 수 있는 문자들의 집합
    # ()는 일치하는 문자열을 묶어서 서브그룹으로 만들거나, 정규식을 그룹화하여 일치 여부를 확인하는 데 사용된다.
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for i in babbling:
        if regex.match(i):
            cnt+=1
    return cnt