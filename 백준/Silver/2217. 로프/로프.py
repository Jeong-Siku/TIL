import sys
input = sys.stdin.readline
n = int(input())
w_arr = []
for _ in range(n):
    w_arr.append(int(input()))

w_arr.sort(reverse=True)

total = []

while w_arr:
    len_w = len(w_arr)
    total.append(w_arr.pop()*len_w)

print(max(total))
    