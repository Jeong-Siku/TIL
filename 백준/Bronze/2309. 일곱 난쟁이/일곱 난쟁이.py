arr = []
for _ in range(9):
    length = int(input())
    arr.append(length)

arr.sort()
minus = sum(arr)-100

exc_num = []
for i in range(9):
    for j in range(i+1,9):
        if arr[i]+arr[j] == minus:
            exc_num.append(arr[i])
            exc_num.append(arr[j])    
            break
    if exc_num:
        break
for i in arr:
    if i not in exc_num:
        print(i)
