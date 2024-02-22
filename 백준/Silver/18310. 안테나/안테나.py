n = int(input())
antennas = sorted(list(map(int, input().split())))

if n%2==1:
    length = []
    print(antennas[n//2])
else:
    length_1 = []
    for antenna in antennas:
        length_1.append(abs(antennas[n//2-1]-antenna))
    
    length_2 = []
    for antenna in antennas:
        length_2.append(abs(antennas[n//2]-antenna))
    
    if sum(length_1) <= sum(length_2):
        print(antennas[n//2-1])
    else:
        print(antennas[n//2])