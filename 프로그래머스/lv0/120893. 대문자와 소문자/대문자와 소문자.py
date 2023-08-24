def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer

def solution(my_string):
    return "".join(i.lower() if i.isupper() else i.upper() for i in my_string)

def solution(my_string):
    return my_string.swapcase()