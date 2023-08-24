def solution(rank, attendance):
    rank_att =  [] 
    for idx,(i,j) in enumerate(zip(rank,attendance)):
        if j:
            rank_att.append([idx,i])
    a,b,c = sorted(rank_att,key=lambda x: x[1])[:3]
    answer = 10000*a[0]+100*b[0]+c[0]
    print(a,b,c)
    return answer