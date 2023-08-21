def solution(wallpaper):
    answer = []
    x_idx = []
    y_idx = []
    for y,i in enumerate(wallpaper):
        for x,j in enumerate(i):
            if j=="#":
                x_idx.append(x)
                y_idx.append(y)
    x_idx.sort()
    y_idx.sort()
    
    print(x_idx)
    print(y_idx)
    
    lux,luy = x_idx[0],y_idx[0]
    rdx,rdy = x_idx[-1]+1,y_idx[-1]+1
    
    return luy,lux,rdy,rdx