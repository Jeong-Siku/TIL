def solution(s):
    answer = 0
    sub_str = {"zero":"0",
               "one":"1",
              "two":"2",
              "three":"3",
              "four":"4",
              "five":"5",
              "six":"6",
              "seven":"7",
              "eight":"8",
              "nine":"9"}
    for i in sub_str:
        s = s.replace(i,sub_str[i])
    return int(s)