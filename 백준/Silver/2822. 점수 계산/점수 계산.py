score = sorted([[idx,int(input())] for idx,i in enumerate(range(8))], key=lambda x : (x[1]))
scores = []
idxs = []
for idx, i in score[3:]:
    scores.append(i)
    idxs.append(idx+1)

print(sum(scores))
print(*sorted(idxs))