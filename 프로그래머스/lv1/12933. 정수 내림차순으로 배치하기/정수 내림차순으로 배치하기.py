def solution(n):
    answer = 0
    return int("".join(sorted(list(str(n)),reverse=True)))