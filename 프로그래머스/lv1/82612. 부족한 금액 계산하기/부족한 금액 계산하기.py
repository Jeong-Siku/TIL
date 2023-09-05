def solution(price, money, count):
    a = sum(price*i for i in range(1,count+1))-money
    return a if a>=0 else 0