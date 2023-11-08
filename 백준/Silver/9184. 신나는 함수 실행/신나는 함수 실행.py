arr = [[[0 for _ in range(-50,51)] for _ in range(-50,51)] for _ in range(-50,51)]

for a in range(-50,51):
    for b in range(-50,51):
        for c in range(-50,51):
            if a <= 0 or b <= 0 or c <= 0 :
                arr[a][b][c] = 1
            
            elif a > 20 or b > 20 or c > 20 :
                arr[a][b][c] = 1048576
            
            elif a < b and b < c :
                arr[a][b][c] = arr[a][b][c-1] + arr[a][b-1][c-1] - arr[a][b-1][c]

            else :
                arr[a][b][c] = arr[a-1][b][c] + arr[a-1][b-1][c] + arr[a-1][b][c-1] - arr[a-1][b-1][c-1]

while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {arr[a][b][c]}')