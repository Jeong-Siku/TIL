def solution(rny_string):
    return rny_string.replace("m","rn")

def solution(rny_string):
    answer=""
    for i in rny_string:
        if i=="m":
            answer+="rn"
        else:
            answer+=i
    return answer