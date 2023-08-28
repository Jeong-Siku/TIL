def solution(keyinput, board):
    answer = [0,0]
    idx_x =board[0]
    idx_y = board[1]
    x =(board[0]-1)//2
    y = (board[1]-1)//2 
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    for i in keyinput:
        if i =="up":
            nx = x+dx[0]
            ny = y+dy[0]
            if nx<0 or ny<0 or nx>=idx_x or ny>=idx_y:
                continue
            else:
                answer[0] = answer[0]+dy[0]
                answer[1] = answer[1]+dx[0]
                x = nx
                y = ny
        elif i =="down":
            nx = x+dx[1]
            ny = y+dy[1]
            if nx<0 or ny<0 or nx>=idx_x or ny>=idx_y:
                continue
            else:
                answer[0] = answer[0]+dy[1]
                answer[1] = answer[1]+dx[1]
                x = nx
                y = ny
        elif i =="left":
            nx = x+dx[2]
            ny = y+dy[2]
            if nx<0 or ny<0 or nx>=idx_x or ny>=idx_y:
                continue
            else:
                answer[0] = answer[0]+dy[2]
                answer[1] = answer[1]+dx[2]
                x = nx
                y = ny
        else:
            nx = x+dx[3]
            ny = y+dy[3]
            if nx<0 or ny<0 or nx>=idx_x or ny>=idx_y:
                continue
            else:
                answer[0] = answer[0]+dy[3]
                answer[1] = answer[1]+dx[3]
                x = nx
                y = ny
    return answer[::-1]