def solution(s):
    # 짝 맞추기, 스택
    stack = []
    if s[0]==")":
        return False
    for i in s:
        if i=="(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False
    