s = list(input())
t = list(input())

while True:
    # 문자열 뒤에 "A" 삭제
    if t[-1] == "A":
        t.pop()
    # 문자열 뒤에 "B"를 삭제하고 문자열 뒤집기
    elif t[-1] == "B":
        t.pop()
        t = t[::-1]
        
    if t==s:
        print(1)
        break
    if not t:
        print(0)
        break