length = list(map(int,input().split()))
length.sort(reverse=True)
if max(length)>=sum(length)-max(length):
    result = sum(length)-max(length)+sum(length)-max(length)-1
else:
    result = sum(length)
print(result)
