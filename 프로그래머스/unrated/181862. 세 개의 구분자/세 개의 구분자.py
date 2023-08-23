# 문제파악 : 구분자가 3개여서 어떻게 하지? 구분자를 하나로 만들면 되지!
def solution(myStr):
    result = ""
    for a,i in enumerate(myStr):
        if i =="a" or i=="b" or i=="c":
            result+="A"
        else:
            result+=myStr[a]
    answer = [i for i in result.split("A") if i]
    return  answer if answer else ["EMPTY"]

def solution(myStr):
    result = myStr.replace("a"," ").replace("b"," ").replace("c"," ").split()
    return  result if result else ["EMPTY"]