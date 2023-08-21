def solution(myString, pat):
    answer = 0
    word = []
    for i in range(len(myString)-len(pat)+1):
        word.append(myString[i:i+len(pat)])
    for i in word:
        if i==pat:
            answer+=1
    return answer

def solution(myString, pat):
    
    return sum(myString[i:i+len(pat)]==pat for i in range(len(myString)))