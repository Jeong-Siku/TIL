def solution(s):
    for i in s:
        if i.isalpha() or len(s) not in [4,6]:
            return False
    return True