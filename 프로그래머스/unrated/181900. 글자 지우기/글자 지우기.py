def solution(my_string, indices):
    result= list(my_string)
    indices.sort()
    
    a=0
    for i in indices:
        i-=a
        del result[i]
        a+=1
    return "".join(result)