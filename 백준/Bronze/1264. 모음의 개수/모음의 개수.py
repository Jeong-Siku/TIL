while True:
    s = input()
    if s=='#':
        break
    s = s.lower()
    cnt = 0
    for i in s:
        if i in 'aeiou':
            cnt+=1
    print(cnt)