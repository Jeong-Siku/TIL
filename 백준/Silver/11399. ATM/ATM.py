n = int(input())
time = list(map(int,input().split()))
time.sort()
min_time = [0]
for i in range(len(time)):
    min_time.append(time[i]+min_time[i])
print(sum(min_time))
    
