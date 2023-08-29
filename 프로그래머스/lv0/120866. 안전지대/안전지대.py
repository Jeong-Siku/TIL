def solution(board):
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    loc_1=[]
    for y,i in enumerate(board):
        for x,j in enumerate(i):
            if j ==1:
                loc_1.append([y,x])
                
    for y,x in loc_1:
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>=len(board) or nx>=len(board):
                continue
            else:
                board[ny][nx]=1
      
    num_0 = 0
    for y,i in enumerate(board):
        for x,j in enumerate(i):
            if j ==0:
                num_0+=1
    
    return num_0