def solution(score):
    answer = []
    for eng,math in score:
        score=(eng+math)/2
        answer.append(score)
    
    sorted_result = sorted(enumerate(answer),key=lambda x : x[1],reverse=True)
    
    rank = []
    avg_score = []
    num = 1
    for order,avg in sorted_result:
        if avg not in avg_score:
            rank.append(num)
            avg_score.append(avg)
        elif avg in avg_score :
            rank.append(rank[-1])
            avg_score.append(avg)
        num+=1
        
    return [b for a,b in sorted(zip(sorted_result,rank),key=lambda x: x[0][0])]