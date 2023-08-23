def solution(my_string):
    answer = 0
    return sum(int(i) for i in my_string if i.isdigit())