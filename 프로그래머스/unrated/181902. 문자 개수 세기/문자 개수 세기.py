def solution(my_string):
    answer = []
    order = [0 for _ in range(52)]
    for i in my_string:
        if i.isupper():
            idx = ord(i)-65
        elif i.islower():
            idx = ord(i)-71
        order[idx]+=1
    return order