from collections import defaultdict
def solution(board, moves):
    dic = defaultdict(list)
    
    for i in board:
        for idx,j in enumerate(i):
            if j==0:
                continue
            else:
                dic[idx+1].append(j)
    result = []
    answer = 0
    for i in moves:
        if dic[i]:
            result.append(dic[i].pop(0))
        else:
            continue
        if len(result)>=2 and result[-1]==result[-2]:
            result.pop()
            result.pop()
            answer+=2
    return answer