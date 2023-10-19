x,y,w,h=list(map(int,input().split()))
left_x,left_y = 0,0
print(min(x-left_x,y-left_y,w-x,h-y))