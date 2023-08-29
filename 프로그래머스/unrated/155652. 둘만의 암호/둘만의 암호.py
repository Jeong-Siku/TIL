def solution(s, skip, index):
    alp_pos = [chr(i) for i in range(ord("a"),ord("z")+1) if chr(i) not in skip]
    
    dic={string:idx for idx,string in enumerate(alp_pos)}
    
    result = []
    for alp in s:
        pos = (dic[alp]+index)%len(alp_pos)
        result.append(alp_pos[pos])
    return  "".join(result)