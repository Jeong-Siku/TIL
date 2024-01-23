# 한수
n = int(input())

h = []
if n < 100:
    print(n)
else:
    cnt=99
    for i in range(100,n+1):
        gap=int(str(i)[1]) - int(str(i)[0])
        for j in range(2,len(str(i))):
            if int(str(i)[j])-int(str(i)[j-1]) == gap:
                cnt+=1
                continue
    print(cnt)