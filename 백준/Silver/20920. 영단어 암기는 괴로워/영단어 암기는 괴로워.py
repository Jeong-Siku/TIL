from collections import defaultdict
import sys

input = sys.stdin.readline
n, m = map(int,input().rstrip().split())

dic = defaultdict(int)

for _ in range(n):
    word = input().rstrip()
    if len(word)<m:
        continue
    else:
        dic[word]+=1

mod_dic = [k for k,v in sorted(dic.items(),key = lambda x: (-x[1],-len(x[0]),x[0]))]
for i in mod_dic:
    print(i)