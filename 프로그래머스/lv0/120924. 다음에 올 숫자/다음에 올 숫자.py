def solution(common):
    q,w,e= common[-3],common[-2],common[-1]
    if e-w==w-q:
        return e+w-q
    else:
        return e+(e-w)*(e-w)//(w-q)