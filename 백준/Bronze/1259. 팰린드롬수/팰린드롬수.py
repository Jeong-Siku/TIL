while True:
    s = list(input())
    if s==['0']:
        break
    while len(s)>1:
        if s[0] == s[-1]:
            s.pop()
            s.pop(0)
        else:
            break
    if len(s)==1 or not s:
        print('yes')
    else:
        print('no')