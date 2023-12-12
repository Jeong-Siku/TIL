arr= input()
bomb = input()
len_bomb = len(list(bomb))

s= []
for i in arr:
    s.append(i)
    while list(bomb) == s[-len_bomb:]:
        del s[-len_bomb:]

print("".join(s) if s else "FRULA")