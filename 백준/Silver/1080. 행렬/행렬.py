n, m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(input()))

b = []
for _ in range(n):
    b.append(list(input()))

# 뒤집기
def change(matrix_a, x, y):
    global ans
    ans+=1
    dx, dy = [0,1,2],[0,1,2]
    for nx in dx:
        for ny in dy:
            if matrix_a[x+nx][y+ny]=="0":
                matrix_a[x+nx][y+ny]="1"
            else:
                matrix_a[x+nx][y+ny]="0"

ans=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(a, i, j)
if a==b:
    print(ans)
else:
    print(-1)