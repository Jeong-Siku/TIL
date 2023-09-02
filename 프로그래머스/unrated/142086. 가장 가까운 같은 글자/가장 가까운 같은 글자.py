def solution(s):
    answer = []
    # 리스트
    # 인덱스
    # 같은 원소의 *마지막* 인덱스 값 => dict의 초기화 이용가능
    for idx,i in enumerate(s):
        if s.index(i) == idx:
            answer.append(-1)
        else:
            answer.append(s[:idx][::-1].index(i)+1)
    return answer

def solution(s):
    answer = []
    dic = {}
    for idx,j in enumerate(s):
        if j not in dic:
            answer.append(-1)
        else:
            answer.append(idx-dic[j])
        dic[j]=idx
    return answer