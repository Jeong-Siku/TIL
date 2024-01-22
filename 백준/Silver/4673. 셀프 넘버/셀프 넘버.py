def make_selfnumber(n):
    sum_num = sum([int(i) for i in str(n)])+n
    return sum_num

self_number = [False]*20000
for i in range(1,10001):
    self_number[make_selfnumber(i)] = True
    
for i in range(1,10001):
    if self_number[i] == False:
        print(i)
