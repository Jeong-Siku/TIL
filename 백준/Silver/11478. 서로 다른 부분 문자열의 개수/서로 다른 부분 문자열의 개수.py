s = input()
part_s = []
for num in range(1,len(s)+1):
    for idx in range(len(s)-num+1):
       if s[idx:idx+num]:
           part_s.append(s[idx:idx+num])

print(len(set(part_s)))