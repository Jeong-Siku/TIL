def solution(polynomial):
    answer = ''
    x_cnt = 0
    plus = 0
    splited = polynomial.split(" + ")
    for i in splited:
        if "x" in i:
            if i == "x":
                x_cnt+=1
            else:
                x_cnt+=int(i.replace("x",""))
        elif int(i):
            plus+=int(i)
    if x_cnt==1:
        x_cnt="x"
    elif x_cnt:
        x_cnt=str(x_cnt)+"x"
    else:
        x_cnt=""
        
    if plus:
        plus=str(plus)
    else:
        plus=""
        
    result = ""
    if x_cnt and plus:
        return x_cnt+" + "+plus
    else:
        return x_cnt+plus
    # append는 빈 값을 넣지 않는다.
    return result