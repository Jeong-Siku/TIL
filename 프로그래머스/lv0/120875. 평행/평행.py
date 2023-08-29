def solution(dots):
   #dots의 숫자를 직접 변수에 대입
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    gradient_12 = abs((y2 - y1) / (x2 - x1))
    gradient_34 = abs((y4 - y3) / (x4 - x3))
    
    gradient_14 = abs((y4 - y1) / (x4 - x1))
    gradient_23 = abs((y3 - y2) / (x3 - x2))
    
    gradient_13 = abs((y3 - y1) / (x3 - x1))
    gradient_24 = abs((y4 - y2) / (x4 - x2))
    if gradient_12 == gradient_34 or gradient_23 == gradient_14 or gradient_13 == gradient_24:
        return 1
    return 0
            