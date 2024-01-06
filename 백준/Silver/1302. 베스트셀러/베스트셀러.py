from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

cnt_dict = Counter(arr)
print(sorted(cnt_dict.most_common(),key=lambda x:(-x[1],x[0]))[0][0])