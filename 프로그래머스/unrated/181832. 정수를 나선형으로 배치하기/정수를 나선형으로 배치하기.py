def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    dy= [0,1,0,-1]
    dx= [1,0,-1,0]
    y,x = 0,0
    direc = 0
    for i in range(1,n*n+1):
        answer[y][x]=i
        
        ny = y + dy[direc]
        nx = x + dx[direc]
        
        if ny>=n or nx >=n or ny<0 or nx<0 or answer[ny][nx]!=0:
            
            direc = (direc+1)%4
            ny = y + dy[direc]
            nx = x + dx[direc]
        y = ny
        x = nx
    return answer