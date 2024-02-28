n = int(input())
dir_name = [input() for _ in range(n)]
global_alp = list(dir_name[0])
for name in dir_name[1:]:
    for idx, alp in enumerate(name):
        if global_alp[idx] == alp:
            continue
        else:
            global_alp[idx] = '?'
print(''.join(global_alp))