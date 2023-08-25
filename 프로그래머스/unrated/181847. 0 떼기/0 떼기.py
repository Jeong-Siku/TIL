def solution(n_str):
    for idx,i in enumerate(n_str):
        if i != "0": 
            return n_str[idx:]
            