def solution(dartResult):
    score_list = [0]
    for idx,i in enumerate(dartResult):
        if i=="S":
            # 문자열을 숫자로 바꾸는 것은 오류 발생
            if dartResult[idx-1]=="0" and dartResult[idx-2] =="1":
                score_list.append(10**1)      
            else:
                score_list.append(int(dartResult[idx-1])**1)
                                           
        elif i=="D":
            if dartResult[idx-1]=="0" and dartResult[idx-2] =="1":
                score_list.append(10**2)      
            else:
                score_list.append(int(dartResult[idx-1])**2)
                                                 
        elif i=="T":
            if dartResult[idx-1]=="0" and dartResult[idx-2] =="1":
                score_list.append(10**3)      
            else:
                score_list.append(int(dartResult[idx-1])**3)
                                                 
        if i=="*":
            score_list[-2] = score_list[-2]*2
            score_list[-1] = score_list[-1]*2
        elif i=="#":
            score_list[-1] = score_list[-1]*(-1)
        
    return sum(score_list)