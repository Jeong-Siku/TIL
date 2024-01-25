n = int(input())
arr = list(map(int, input().split()))
formula_num = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

def bt(start, result, plus, minus, multy, divide):
    global max_result, min_result
    if start == n :
        max_result = max(result,max_result)
        min_result = min(result,min_result)
        return
    
    if plus :
        bt(start+1,result+arr[start],plus-1,minus,multy,divide)
    if minus :
        bt(start+1,result-arr[start],plus,minus-1,multy,divide)
    if multy :
        bt(start+1,result*arr[start],plus,minus,multy-1,divide)
    if divide :
        bt(start+1,result//arr[start] if result>=0 else (abs(result)//arr[start])*-1,plus,minus,multy,divide-1)
        
bt(1, arr[0], formula_num[0], formula_num[1], formula_num[2], formula_num[3])
print(max_result)
print(min_result)