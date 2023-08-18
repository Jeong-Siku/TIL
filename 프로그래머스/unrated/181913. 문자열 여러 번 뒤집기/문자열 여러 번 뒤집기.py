def solution(my_string, queries):
    answer = ''
    for i in range(len(queries)):
        start_idx = queries[i][0]
        end_idx = queries[i][1]+1
        before = my_string[start_idx:end_idx:]
        after = before[::-1]
        
        my_string = my_string[:start_idx] + after + my_string[end_idx:]
        
    return my_string

def solution(my_string, queries):
    # 문자열의 순서는 바꿀 수 없다. 새로 초기화해야함
    answer = list(my_string)
    # 문자열을 리스트화시키면 한글자씩 원소로 만들어진다.
    for s,e in queries:
        answer[s:e+1] = answer[s:e+1][::-1]
    return "".join(answer)