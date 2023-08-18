def solution(a, b, c, d):
    l1 = {a,b,c,d}
    l2 = sorted([a,b,c,d],reverse=True)
    # d = dict()
    d1 = {i:l2.count(i) for i in l2}
    # for i in l2:
    #     d[i] = 1
    # for i in l2:
    #     if d[i]:
    #         d[i]+=1
            
    d2 = sorted(d1.items(),key=lambda x: x[1],reverse=True)
    
    if len(l1)==1:
        score = 1111*l2[0]
        
    elif len(l1) == 2 and 3 in d1.values():
        score = (10*d2[0][0]+d2[1][0])**2
        
    elif len(l1) == 2 :
        if len(set(d1.values()))==1:
            score = (d2[0][0]+d2[1][0])*abs(d2[0][0]-d2[1][0])
    elif len(l1) ==3 :
        score = (d2[1][0]*d2[2][0])
        
    else:
        score = l2[3]
        
    return score

