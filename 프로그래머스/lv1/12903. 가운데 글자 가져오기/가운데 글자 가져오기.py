def solution(s):
    answer = ''
    if not len(s)%2:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
    return answer