def solution(s):
    answer=""
    dict = {i:s.count(i) for i in s}
    print(dict)
    for idx,i in enumerate(dict):
        if dict[i]==1:
            answer+=i
    return "".join(sorted(answer))

def solution(s):
    return "".join(sorted(i for i in s if s.count(i) ==1))