def solution(my_string, is_suffix):
    answer = 0
    a = [my_string[i:] for i in range(len(my_string))]
    return int(is_suffix in a)

def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    return 0
