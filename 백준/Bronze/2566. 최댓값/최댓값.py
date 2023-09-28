matrix = []
for i in range(9):
    row = list(map(int,input().split()))
    matrix.append(row)

max_num = 0
idx = []
for i in range(9):
    for j in range(9):
        if max_num<=matrix[i][j]:
            max_num = matrix[i][j]
            idx = [i+1,j+1]

print(max_num)
print(*idx)