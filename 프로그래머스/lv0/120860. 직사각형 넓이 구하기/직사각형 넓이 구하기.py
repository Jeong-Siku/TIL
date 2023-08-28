def solution(dots):
    dots.sort(key=lambda x:x[0])
    x = abs(dots[0][1]-dots[1][1])
    y = abs(dots[0][0]-dots[2][0])
    
    return x*y