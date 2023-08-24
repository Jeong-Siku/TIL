def solution(my_string):
    answer = ''
    for i in my_string:
        if i in answer:
            continue
        answer+=i
    return answer

def solution(my_string):
    # dict.fromkeys(iter,values)는 dict생성 메소드
    return "".join(dict.fromkeys(my_string,0))