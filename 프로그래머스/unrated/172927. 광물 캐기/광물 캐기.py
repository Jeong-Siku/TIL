def solution(picks, minerals):
    # 5개씩 나눠서 다이아가 가장 많은 곳을 분류하는 과정이 필요
    # 다이아가 가장 많은 집합에 다이아 곡괭이를 사용
    answer = 0
    
    m_dic = {"diamond":0,"iron":0,"stone":0}
    array = []
    # 최대로 캐는 횟수
    min_cnt = min(sum(picks)*5,len(minerals))
    # 5개 집합별로 다이아몬드, 철, 돌의 개수를 파악
    for i in range(min_cnt):
        m_dic[minerals[i]]+=1
        if i%5==4 or i == len(minerals)-1:
            array.append([m_dic["diamond"],m_dic["iron"],m_dic["stone"]])
            m_dic["diamond"],m_dic["iron"],m_dic["stone"] = 0, 0, 0
    
    # 다이아몬드, 철, 돌의 개수별로 정렬
    array.sort(key = lambda x : (x[0],x[1],x[2]),reverse=True)
    
    print(array)
    # 피로도 구하기
    dic = {0:[1,1,1],1:[5,1,1],2:[25,5,1]}
    for dia, iron, stone in array:
        for i in range(3):
            if picks[i]:
                picks[i] -=1
                answer+=dic[i][0]*dia +dic[i][1]*iron+dic[i][2]*stone 
                break

    return answer