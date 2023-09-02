def solution(s):
    answer = []
    # 리스트
    # 인덱스
    for idx,i in enumerate(s):
        if s.index(i) == idx:
            answer.append(-1)
        else:
            answer.append(s[:idx][::-1].index(i)+1)
    return answer