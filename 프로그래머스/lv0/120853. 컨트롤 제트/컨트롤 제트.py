def solution(s):
    answer = 0
    a = s.split()
    for idx,i in enumerate(a):
        if i =="Z":
            answer-=int(a[idx-1])
        else:
            answer+=int(i)
    return answer