goal = int(input())

n = 4000000
arr = [False, False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if arr[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            arr[j]=False
            
end=0
total_sum=0
cnt = 0
for start in range(len(primes)):
    while total_sum<goal and end<len(primes):
        total_sum+=primes[end]
        end+=1
    if total_sum == goal:
       cnt+=1
    total_sum-=primes[start]

print(cnt) 
