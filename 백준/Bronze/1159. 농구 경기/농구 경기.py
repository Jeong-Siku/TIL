from collections import defaultdict
n = int(input())

dic = defaultdict(int)
for _ in range(n):
    dic[input()[0]]+=1

sorted_dic = sorted(list(dic.items()),key=lambda x:x[0])

ans = ""
for alp, cnt in sorted_dic:
    if cnt>=5:
        ans+=alp
print(ans if ans else "PREDAJA" )