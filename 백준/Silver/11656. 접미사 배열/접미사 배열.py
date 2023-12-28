s = input()

arr = []
for i in range(len(s)):
    arr.append(s[i:])

for i in sorted(arr):
    print(i)
