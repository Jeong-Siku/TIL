n,m = map(int,input().split())
arr = []
def back_tracking():
    if len(arr)==m:
        print(*arr)
        return
    else:
        for i in range(1,n+1):
            if i not in arr and all([True if i>k else False for k in arr]):
                arr.append(i)
                back_tracking()
                arr.pop()

back_tracking()