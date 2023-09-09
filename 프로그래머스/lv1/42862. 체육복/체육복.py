def solution(n, lost, reserve):
    # 배열: 원소별 체육복 개수 만들기
    uniform_num = [1 for _ in range(n+2)]
    lost.sort()
    reserve.sort()
    for i in lost:
        uniform_num[i]=0
    for i in reserve:
        uniform_num[i]+=1

    for i in lost:
        if uniform_num[i] == 0 and uniform_num[i-1]==2:
            uniform_num[i]+=1
            uniform_num[i-1]-=1
        elif uniform_num[i] == 0 and uniform_num[i+1]==2:
            uniform_num[i]+=1
            uniform_num[i+1]-=1

    return len([i for i in uniform_num if i>=1]) -2