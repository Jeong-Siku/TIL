def solution(str_list):
    answer = []
    if "l" in str_list and "r" in str_list:
        l_idx = str_list.index("l")
        r_idx = str_list.index("r")
        if l_idx > r_idx:
            answer = str_list[r_idx+1:]
        else:
            answer = str_list[:l_idx]
    elif "l" in str_list and "r" not in str_list:
        l_idx = str_list.index("l")
        answer = str_list[:l_idx]
    elif "r" in str_list and "l" not in str_list:
        r_idx = str_list.index("r")
        answer = str_list[r_idx+1:]
    else:
        answer= []
    return answer