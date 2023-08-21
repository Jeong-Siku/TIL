def solution(rsp):
    answer = ''
    win = {"2":"0","0":"5","5":"2"}
    for i in rsp:
        answer+=win[i]
    return answer