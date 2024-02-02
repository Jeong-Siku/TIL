import sys
input = sys.stdin.readline

n, m = map(int,input().split())

package_money = float('inf')
one_money = float('inf')
for _ in range(m): 
    package, one = map(int,input().split())
    package_money = min(package_money,package)
    one_money = min(one_money,one)
   
print(min((n//6+1)*package_money, n//6*package_money+n%6*one_money, n*one_money))