def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split(".")))
    valid = {}
    for i in terms:
        a = i.split()
        valid[a[0]] = int(a[1])
        
    print("today",today)
    
    for i in range(len(privacies)):
        privacy = list(map(int,privacies[i][:-2].split(".")))
        add_mon = valid[privacies[i][-1]]
        # 동시에 진행하지 않으면 변경된 값으로 진행되기에 답이 틀리다.
        privacy[1],privacy[0] = (privacy[1]+add_mon)%12 if (privacy[1]+add_mon)%12 else 12, privacy[0] + (privacy[1]+add_mon)//12-1 if (privacy[1]+add_mon)%12 ==0 else privacy[0]+(privacy[1]+add_mon)//12
        
        print(privacy)
        
        if privacy <= today:
            answer.append(i+1)
    return answer