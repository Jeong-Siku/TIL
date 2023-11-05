n = int(input())
def fibonacci(a):
    if a==0:
        return 0
    if a==1:
        return 1
    return fibonacci(a-1)+fibonacci(a-2)

print(fibonacci(n))
    