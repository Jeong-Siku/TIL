def solution(my_strings, parts):
    answer = ''
    # 문자열끼리 병합하는 건 가능
    for s,e in enumerate(parts):
        answer+=my_strings[s][e[0]:e[1]+1]
    return answer