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

def solution(board, moves):
    result=[]
    answer=0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                # 끝난 보더라인은 초기화시킨다.
                board[j][i-1]=0
                
                if len(result)>1 and result[-1]==result[-2]:
                    result=result[:-2]
                    answer+=2
                break
    return answer