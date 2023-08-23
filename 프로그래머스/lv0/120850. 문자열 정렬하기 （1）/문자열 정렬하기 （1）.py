def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    return sorted(answer)

import re
def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))