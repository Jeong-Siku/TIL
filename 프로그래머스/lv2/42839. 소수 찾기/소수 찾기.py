from itertools import permutations
def solution(numbers):
    arr = []
    result = 0
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            num = "".join(j)
            arr.append(int(num))
    for i in list(set(arr)):
        if i <=1:
            continue
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            result+=1
            print(i)
    return result