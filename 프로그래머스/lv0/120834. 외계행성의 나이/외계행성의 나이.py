def solution(age):
    age = str(age)
    answer=''
    for i in age:
        answer+=chr(ord(i)+49)
    return answer