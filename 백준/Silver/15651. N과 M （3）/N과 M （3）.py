n,m = map(int,input().split())
arr = []
def back_tracking():
    if len(arr)== m :
        print(*arr)
        return
    else:
        for i in range(1,n+1):
            # 조건을 안넣음
            arr.append(i)
            back_tracking()
            arr.pop()
            
back_tracking()