def solution(my_string, m, c):
    answer = [my_string[i:i+m] for i in range(0,len(my_string),m)]
    word = []
    for i in answer:
        word.append(i[c-1])
    return "".join(word)

def solution(my_string,m,c):
    return my_string[c-1::m]