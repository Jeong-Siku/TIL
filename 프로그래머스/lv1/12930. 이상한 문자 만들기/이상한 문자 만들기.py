def solution(s):
    answer = ''
    for k in s.split(" "):
        for idx,i in enumerate(k):
            if not idx%2:
                answer+=i.upper()
            else:
                answer+=i.lower()
        answer+=" "
    return answer[:-1]