s = input()
while '00' in s or '11' in s:
    s = s.replace('00','0')
    s = s.replace('11','1')
cnt_1 = s.count('1')
cnt_0 = s.count('0')
print(min(cnt_1,cnt_0))