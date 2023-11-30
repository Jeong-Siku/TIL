n = int(input())
arr = [0 for _ in range(10)]
num = 1 # 자릿수
# 자릿수가 늘어날수록 *10
def make_nine(n):
    while n%10 != 9 :
        for i in str(n):
            arr[int(i)] += num
        n-=1
    return n
    
while n>0:
    n = make_nine(n)
    if n < 10:
        for i in range(n+1): #가장 높은 자리 수
            arr[i] += num
    else:
        for i in range(10):
            arr[i] += (n//10+1) * num
    arr[0] -= num # 가장 높은 자리수는 0이 없다. 
    num *= 10
    n //=10
print(*arr)