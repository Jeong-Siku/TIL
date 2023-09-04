def solution(X, Y):
    # 공통
    # 배열
    # 길이가 길다.
    same = []
    for i in X:
        if i in Y:
            same.append(i)
            Y = Y.replace(i,"",1)
    if same and same[0] == "0":
        return "0"
    return "".join(sorted(same,reverse=True)) if same else "-1"

from collections import Counter
def solution(X, Y):
    X_cnt = Counter(X)
    Y_cnt = Counter(Y)
    answer = ""
    
    for i in range(9,-1,-1):
        cnt = min(X_cnt[str(i)],Y_cnt[str(i)])
        answer+=str(i)*cnt
    if not answer:
        return "-1"
    if answer[0]=="0":
        return "0"
    return answer
