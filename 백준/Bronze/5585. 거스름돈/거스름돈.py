n = int(input())

changes = 1000-n
result = 0
for i in [500,100,50,10,5,1]:
    result+=changes//i
    changes%=i
print(result)