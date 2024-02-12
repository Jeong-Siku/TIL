n = int(input())
sorted_weight = sorted(list(map(int,input().split())))
sum_weight = [sorted_weight[0]]
for weight in sorted_weight[1:]:
    sum_weight.append(sum_weight[-1]+weight)
    
for i in range(1,n):
    if sorted_weight[0]!=1:
        print(1)
        break
    if sorted_weight[i]>sum_weight[i-1]+1:
        print(sum_weight[i-1]+1)
        break
else:
    if n == 1:
        if sorted_weight[0] !=1:
            print(1)
        else:
            print(2)
    else:
        print(sum_weight[-1]+1)