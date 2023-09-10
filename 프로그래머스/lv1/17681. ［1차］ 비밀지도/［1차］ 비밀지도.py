def solution(n, arr1, arr2):
    # 조건 : 공백, 벽 " ", "#"
    answer = []
    map_1 = []
    map_2 = []
    for i,j in zip(arr1,arr2):
        if len(bin(i)[2:])<n:
            map_1.append((n-len(bin(i)[2:]))*"0"+bin(i)[2:])
        else:
            map_1.append(bin(i)[2:])       
        if len(bin(j)[2:])<n:
            map_2.append((n-len(bin(j)[2:]))*"0"+bin(j)[2:])       
        else:
            map_2.append(bin(j)[2:])
            
    final_map = []
    for i,j in zip(map_1,map_2):
        result = ""
        for idx in range(n):
            if i[idx] =="1" or j[idx] =="1":
                    result+="#"
            else:
                result+=" "
        final_map.append(result)
    return final_map

# 비트연산자
def solution(n, arr1, arr2):
    map_0 = [bin(i|j)[2:] for i,j in zip(arr1,arr2)]
    for idx , i in enumerate(map_0):
        if len(i)<n:
            map_0[idx] = "0"*(n-len(i)) + i
        map_0[idx] = "".join("#" if i=="1" else " " for i in map_0[idx])
    return map_0