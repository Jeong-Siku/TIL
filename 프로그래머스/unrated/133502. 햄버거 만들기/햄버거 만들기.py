def solution(ingredient):
    # 빵 야채 고기 빵 = 1 2 3 1
    # 정렬
    # 일치
    # 원소 크기 매우 크다
    # 스택
    answer=0
    i=ingredient.index(1)
    k=0
    cnt=sum(1 for j in ingredient if j == 1)
    while k!=cnt:
        if [1,2,3,1]==ingredient[i:i+4]:
            answer+=1
            ingredient=ingredient[:i]+ingredient[i+4::]         
            if 1 in ingredient:
                i = ingredient.index(1)
        else:
            i+=1
        k+=1
    return answer

def solution(ingredient):
    answer = 0
    cur = []
    for i in ingredient:
        cur.append(i)
        if cur[-4:]==[1,2,3,1]:
            answer+=1
            del cur[-4:]
    return answer