def solution(my_string, n):
    return "".join([my_string[i]*n for i in range(len(my_string))])