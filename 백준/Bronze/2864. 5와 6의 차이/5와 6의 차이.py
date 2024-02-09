a, b = input().split()
min_a = a
max_a = a
min_b = b
max_b = b
if '5' in a :
    max_a = a.replace('5','6')
if '6' in a:
    min_a = a.replace('6','5')

if '5' in b :
    max_b = b.replace('5','6')
if '6' in b:
    min_b = b.replace('6','5')

print(int(min_a)+int(min_b), int(max_a)+int(max_b))