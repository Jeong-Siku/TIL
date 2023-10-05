result = []
for _ in range(5):
    result.append(int(input()))
    
result.sort()

print(round(sum(result)/5))
print(result[2])