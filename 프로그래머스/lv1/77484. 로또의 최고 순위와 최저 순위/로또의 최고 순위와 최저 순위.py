def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = 0
    cnt_0 = 0
    for i in lottos:
        if i in win_nums:
            answer+=1
        elif i == 0:
            cnt_0 +=1
    print(answer,cnt_0)
    return rank[answer+cnt_0],rank[answer]