def solution(my_string, is_prefix):
    answer = my_string[:len(is_prefix)]==is_prefix
    return int(answer)