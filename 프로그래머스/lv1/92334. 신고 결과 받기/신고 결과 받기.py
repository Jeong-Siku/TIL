from collections import defaultdict
def solution(id_list, report, k):
    # 조건 : 신고 횟수 1번, 한번에
    # 길이가 길다
    # dict
    answer=[]
    report_id = defaultdict(list)
    result = defaultdict(int)
    for i in report:
        reporter,reported=i.split()
        report_id[reporter].append(reported)
    for i in report_id:
        report_id[i]=list(set(report_id[i]))
    for i in report_id:
        for j in report_id[i]:
            result[j]+=1
    for i in id_list:
        cnt=0
        for j in report_id[i]:
            if result[j]>=k:
                cnt+=1
        answer.append(cnt)
    return answer