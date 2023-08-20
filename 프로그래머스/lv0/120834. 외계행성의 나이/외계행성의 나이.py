def solution(age):
    age = str(age)
    answer=''
    for i in age:
        answer+=chr(ord(i)+49)
    return answer

def solution(age):
    age = str(age)
    return "".join(chr(int(i)+97) for i in age)