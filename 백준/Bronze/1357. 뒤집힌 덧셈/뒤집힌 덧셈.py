def rev(x=str):
    x=x[::-1]
    return x
x, y = input().split()
print(int(rev(str(int(rev(x))+int(rev(y))))))