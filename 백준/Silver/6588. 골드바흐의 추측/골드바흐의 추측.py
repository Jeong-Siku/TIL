import sys
input = sys.stdin.readline

n = 1000000
arr = [False,False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if arr[i]:
       primes.append(i)
       for i in range(2*i,n+1,i):
           arr[i] = False 

while True:
    n = int(input())
    if n == 0 :
        break
    
    for i in range(3,n):
        if arr[i] and arr[n-i] and i%2 !=0:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
        