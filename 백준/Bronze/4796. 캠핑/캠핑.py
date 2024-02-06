l, p, v= 1, 1, 1
ans = 0
case_num = 0
while True:
    l, p, v = map(int,input().split())
    if not (l != 0 or p != 0 or v != 0):
        break
    ans += v//p*l # 연속되는 경우
    if v%p >= l: # 남은 일수
        ans+=l
    else:
        ans += v%p 
    case_num +=1
    print('Case {0}: {1}'.format(case_num, ans))
    ans = 0