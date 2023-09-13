def solution(a, b):
    answer = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    calender = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    total_day=0
    for i in range(1,a):
        total_day+=calender[i]
    total_day+=b
    return answer[total_day%7-1]