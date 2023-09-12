def solution(s, n):
    answer = ''
    for i in s:
        if ord(i)>=97:
            answer+=chr(97+(ord(i)+n-97)%26)
        elif i==" ":
            answer+=" "
        else:
            answer+=chr(65+(ord(i)+n-65)%26)
    return answer