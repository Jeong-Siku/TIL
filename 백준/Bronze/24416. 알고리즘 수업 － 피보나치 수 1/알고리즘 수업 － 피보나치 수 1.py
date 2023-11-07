n = int(input())

cnt_1 = 1
cnt_2 = 0

def fib(n):
    global cnt_1
    if n==1 or n ==2 :
        return 1
    else:
        cnt_1+=1
        return fib(n-1)+fib(n-2)
def fibonacci(n):
    global cnt_2
    fibo = [0]+[0 for _ in range(n)]
    fibo[1], fibo[2] = 1, 1
    
    for i in range(3,n+1):
        cnt_2+=1
        fibo[i] = fibo[i-1]+fibo[i-2]
    return fibo[n]

print(fibonacci(n), cnt_2)