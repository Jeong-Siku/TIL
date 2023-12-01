import sys
input = sys.stdin.readline
n = int(input())

distance = 1
total_sum = [0]
total =0
while total<=2147483648:
    total+=distance
    total_sum.append(total)
    total+=distance
    total_sum.append(total)
    distance+=1
    
for _ in range(n):
    x,y = map(int,input().split())
    goal_distance = y-x
    print(total_sum.index(list(filter(lambda x:x>=goal_distance,total_sum))[0]))