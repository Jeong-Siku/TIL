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