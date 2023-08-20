def solution(emergency):
    order = [i+1 for i in range(len(emergency))]
    modify = sorted(emergency,reverse=True)
    # zip는 객체로 list 등 형태를 정해줘야한다.
    grade = list(zip(modify,order))
    answer = []
    
    for i in emergency:
        for j in range(len(emergency)):
            if grade[j][0] == i:
                answer.append(grade[j][1])
    return answer

def solution(emergency):
    a = {l:i+1 for i,l in enumerate(sorted(emergency,reverse=True))}
    
    answer = []
    for i in emergency:
        answer.append(a[i])
    return answer