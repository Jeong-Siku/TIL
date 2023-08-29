def solution(numlist, n):
    dist=[]
    numlist.sort(reverse=True)
    for i in numlist:
        dist.append(abs(n-i))
    
    dic = {numlist[idx]:dis for idx,dis in enumerate(dist)}
    
    # 정렬 기준에 -를 붙이면 reverse 기준이 붙는다.
    ordered_dic = sorted(dic.items(),key=lambda x:(x[1],-x[0]))
    
    return [i for i,a in ordered_dic]

def solution(numlist, n):
    return sorted(numlist,key=lambda x : (abs(x-n),n-x))