def solution(my_string, n):
    return my_string[-1:-n-1:-1][::-1]