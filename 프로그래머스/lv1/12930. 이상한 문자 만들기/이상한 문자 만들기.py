def solution(s):
    answer = ''
    # split()와 split(" ")는 다른 리스트를 반환한다.
    for k in s.split(" "):
        for idx,i in enumerate(k):
            if not idx%2:
                answer+=i.upper()
            else:
                answer+=i.lower()
        answer+=" "
    return answer[:-1]