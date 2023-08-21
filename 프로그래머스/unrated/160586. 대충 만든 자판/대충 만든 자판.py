def solution(keymap, targets):
    answer = []
    
    # 딕셔너리를 초기화 할 때 가능한 모든 값을 넣을 것
    # 딕셔너리로 각 알파벳 누르는 횟수를 저장하고 최종적으로 최소의 횟수만 남긴 뒤 타겟에서 해당 값을 더해서 구하려고 함
    # 딕셔너리 값이 최종 keymap의 것만 남음. 최소값을 어떻게 비교하지?
    prev = {i:100 for i in "".join(keymap)} 

    for k in keymap:
        for alp in k:
            if prev[alp] and prev[alp]>=k.index(alp)+1:
                prev[alp] = k.index(alp) + 1
            
    result=[]
    for tar in targets:
        cnt=0
        for a in tar:
            if a not in prev:
                cnt=-1
                # break는 해당 for문에만 영향을 끼친다.
                break
            else:
                cnt+=prev[a]
        if cnt:
            result.append(cnt)
    return result