while True:
    a =list(map(int,input().split()))
    if set(a)=={0}:
        break
    if max(a)>=sum(a)-max(a):
        print("Invalid")
    elif len(set(a))==2:
        print("Isosceles")
    elif len(set(a))==1:
        print("Equilateral")
    else:
        print("Scalene")
    