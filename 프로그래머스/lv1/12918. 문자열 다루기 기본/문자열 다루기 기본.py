def solution(s):
    for i in s:
        if i.isalpha() or len(s) not in [4,6]:
            return False
    return True

def solution(s):
    return len(s) in [4,6] and s.isdigit()