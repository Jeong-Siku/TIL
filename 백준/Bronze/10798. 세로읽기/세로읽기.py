matrix = [["" for _ in range(15)] for _ in range(5)]
max_num = 0
for i in range(5):
    for idx,j in enumerate(input()):
        matrix[i][idx]=j

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        print(matrix[j][i],end="")
    