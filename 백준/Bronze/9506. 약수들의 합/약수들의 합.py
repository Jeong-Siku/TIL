while True:
    num = int(input())
    if num == -1:
        break
    
    mod = []
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            mod.append(i)
            if i**2 == num:
                continue
            else:
                mod.append(num//i)
    mod.sort()
    if sum(mod[:-1]) == num:
        mod = list(map(str,mod))
        add_num = " + ".join(mod[:-1])
        print(f"{num} = {add_num}")
    else:
        print(f'{num} is NOT perfect.')
