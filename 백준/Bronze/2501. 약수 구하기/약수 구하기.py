n,k= list(map(int,input().split()))
약수 = []
for i in range(1,n+1):
    if not n%i:
        약수.append(i)
if len(약수) < k:
    print(0)
else:
    print(약수[k-1])