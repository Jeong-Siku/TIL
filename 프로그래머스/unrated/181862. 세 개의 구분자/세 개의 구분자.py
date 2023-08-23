def solution(myStr):
    splited = myStr
    std = ["a","b","c"]
    result = []
    
    for i in std:
        for j in splited.split(i):
            if "a" in j or "b" in j or "c" in j or not j:
                continue
            result.append(j)
        splited="".join(splited.split(i))
        
    return result if result else ["EMPTY"]

def solution(myStr):
    result = ""
    for a,i in enumerate(myStr):
        if i =="a" or i=="b" or i=="c":
            result+="A"
        else:
            result+=myStr[a]
    answer = [i for i in result.split("A") if i]
    return  answer if answer else ["EMPTY"]