def solution(myString, pat):
    answer = 0
    a = myString
    a=a.replace("A","C")
    a=a.replace("B","D")
    a=a.replace("C","B")
    a=a.replace("D","A")
    return int(pat in a)