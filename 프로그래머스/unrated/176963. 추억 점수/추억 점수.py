def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]]=yearning[i]
    
    score_list = []
    for i in photo:
        photo_score = []
        for j in i:
            if j in score.keys():
               photo_score.append(score[j])
        score_list.append(sum(photo_score))
    return score_list