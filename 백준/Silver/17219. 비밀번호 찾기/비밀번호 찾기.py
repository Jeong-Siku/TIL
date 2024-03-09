import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dic = {}
for _ in range(n):
    site, password = input().rstrip().split()
    dic[site] = password

for _ in range(m):
    print(dic[input().rstrip()])