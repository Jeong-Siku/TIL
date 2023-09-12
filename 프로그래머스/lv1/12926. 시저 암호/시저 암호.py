def solution(s, n):
    answer = ''
    for i in s:
        if ord(i)>=97:
            answer+=chr(97+(ord(i)+n-97)%26)
        else:
            answer+=chr(65+(ord(i)+n-65)%26)
    return answer

def solution(s, n):
    answer=""
    for i in s:
        if i.isupper():
            answer+=chr((ord(i)-ord("A")+n)%26+ord("A"))
        elif i.islower():
            answer+=chr((ord(i)-ord("a")+n)%26+ord("a"))
        else:
            answer+=i
    return answer