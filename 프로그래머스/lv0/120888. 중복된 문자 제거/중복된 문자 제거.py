def solution(my_string):
    answer = ''
    for i in my_string:
        if i in answer:
            continue
        answer+=i
    return answer