n = int(input())
x = []
y = []
for _ in range(n):
    x_element, y_element = list(map(int,input().split()))
    x.append(x_element)
    y.append(y_element)
len_x = max(x)-min(x)
len_y = max(y)-min(y)
print(len_x*len_y)