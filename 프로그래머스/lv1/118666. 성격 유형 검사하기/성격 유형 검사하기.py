from collections import defaultdict
def solution(survey, choices):
    answer = ''
    # 대치
    # 조건 : 4를 기준으로 점수를 더하는 대상이 바뀐다.
    survey_score = defaultdict(int)
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    for i in range(len(survey)):
        if choices[i]<=3:
            survey_score[survey[i][0]]+=score[choices[i]]
        elif choices[i]>=5:
            survey_score[survey[i][1]]+=score[choices[i]]
        
    answer+= "R" if survey_score["R"]>=survey_score["T"] else "T"
    print(survey_score["R"],survey_score["T"])
    answer+= "C" if survey_score["C"]>=survey_score["F"] else "F"
    answer+= "J" if survey_score["J"]>=survey_score["M"] else "M"
    answer+= "A" if survey_score["A"]>=survey_score["N"] else "N"
    return answer