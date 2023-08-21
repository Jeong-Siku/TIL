def solution(balls, share):
    a = 1
    for i in range(balls+1-share,balls+1):
        a*=i
        
    b = 1
    for i in range(1,share+1):
        b*=i
    return  a/b