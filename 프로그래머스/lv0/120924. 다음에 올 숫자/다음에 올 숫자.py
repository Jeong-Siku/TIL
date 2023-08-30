def solution(common):
    a,b,c=common[:3] 
    if c-b==b-a:
        return common[-1]+(b-a)
    else:
        return common[-1]*(b//a)