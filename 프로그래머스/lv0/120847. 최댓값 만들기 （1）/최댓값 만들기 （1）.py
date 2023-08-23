def solution(numbers):
    sort_num = sorted(numbers)
    return sort_num[-1]*sort_num[-2]