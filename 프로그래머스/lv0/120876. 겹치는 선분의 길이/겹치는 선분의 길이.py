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

def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    # 집합의 교집합과 합집합을 이용할 것
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))