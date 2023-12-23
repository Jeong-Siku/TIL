import sys
input = sys.stdin.readline
n, m = map(int, input().split())

not_listen = []
for _ in range(n):
    not_listen.append(input().rstrip())
    
not_see = []
for _ in range(m):
    not_see.append(input().rstrip())

sorted_inter = sorted(list(set(not_listen).intersection(set(not_see))))

print(len(sorted_inter))
for i in sorted_inter:
    print(i)
