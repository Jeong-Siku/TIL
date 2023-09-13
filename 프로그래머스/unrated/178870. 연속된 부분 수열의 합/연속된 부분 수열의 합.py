def solution(sequence, k):
    # 그리드
    # 근데 원소가 너무 많은데?
    # 두개 인덱스 : 투포인트
    # 조건: min값 구하기, 정렬합, 수열
    s,e,total = 0,0,sequence[0]
    min_s,min_e=1000000,2000000
    sequence+=[0]
    while e<len(sequence)-1:
        if total<=k:
            if total==k and e-s < min_e-min_s:
                min_s,min_e=s,e
            # 이 부분 때문에 sequence 배열을 하나더 추가
            e+=1
            total+=sequence[e]
        else:
            # 그리드로 하면 시간초과
            s+=1
            # total=sequence[s]
            # e=s
            total-=sequence[s-1]
    return min_s,min_e
            

        