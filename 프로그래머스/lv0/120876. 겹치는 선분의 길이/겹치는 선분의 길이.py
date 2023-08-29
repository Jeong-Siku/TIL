def solution(lines):
    range_line=[]
    for line in lines:
        range_line+=line
    min_point=min(range_line) 
    max_point=max(range_line)
    print(min_point,max_point)
    
    a,b,c = lines
    answer = 0
    for i in range(min_point,max_point+1):
        overrap_point=0
        if a[0]<=i<a[1]:
            overrap_point+=1
        if b[0]<=i<b[1]:
            overrap_point+=1
        if c[0]<=i<c[1]:
            overrap_point+=1
        if overrap_point>=2:
            answer+=1
    
    
    return answer