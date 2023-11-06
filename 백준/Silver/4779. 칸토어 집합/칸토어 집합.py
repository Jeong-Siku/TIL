def conto(arr,s,e):
    if e-s<3:
        return
    for i in range(s+(e-s)//3,s+(e-s)*2//3):
        arr[i]=" "
    conto(arr,s,s+(e-s)//3)
    conto(arr,s+(e-s)*2//3,e)

while True:
    try:
        n = int(input())
        arr =  ["-"] * (3 ** n)
        conto(arr,0,3**n)
        print("".join(arr))
    except:
        break