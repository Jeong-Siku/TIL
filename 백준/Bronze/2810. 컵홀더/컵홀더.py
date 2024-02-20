n = int(input())
seat = list(input())
holder = n+1-seat.count('L')//2
print(min(n,holder))