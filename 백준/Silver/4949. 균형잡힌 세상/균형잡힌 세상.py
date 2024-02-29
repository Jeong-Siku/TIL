while True:
    s = input()
    if s =='.':
        break
    bal = []
    for alp in s:
        if alp == '(':
            bal.append('(')
        if bal and bal[-1] == '(' and alp ==')':
            bal.pop()
        elif alp==")":
            bal.append(')')
        if alp == '[':
            bal.append('[')
        if bal and bal[-1] == '[' and alp ==']':
            bal.pop()
        elif alp=="]":
            bal.append(']')
    if not bal:
        print('yes')
    else:
        print('no')