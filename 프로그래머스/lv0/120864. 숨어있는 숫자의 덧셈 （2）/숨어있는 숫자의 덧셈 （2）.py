def solution(my_string):
    answer=''
    for i in my_string:
        if not i.isdigit():
            answer+="a"
        else:
            answer+=i
    answer = sum(list(map(int,[i for i in answer.split("a") if not i==""])))
    return answer