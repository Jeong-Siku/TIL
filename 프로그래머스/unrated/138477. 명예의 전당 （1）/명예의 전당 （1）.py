def solution(k, score):
    answer = []
    score_list= []
    # 상위 점수
    # 커트라인
    for i in score:
        score_list.append(i)
        score_list.sort()
        answer.append(score_list[-k:][0])
    return answer