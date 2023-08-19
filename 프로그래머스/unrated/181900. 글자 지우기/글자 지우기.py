def solution(my_string, indices):
    result= list(my_string)
    indices.sort()
    
    a=0
    for i in indices:
        i-=a
        del result[i]
        a+=1
    return "".join(result)

def solution(my_string, indices):
    return "".join([my_string[i] for i in range(len(my_string)) if i not in indices])