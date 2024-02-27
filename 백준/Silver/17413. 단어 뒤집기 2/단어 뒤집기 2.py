s = input()
stack = []
ans = ''
for alp in s: # if elif를 안쓴 이유는 조건과 상관없이 스택에 alp를 쌓아야하기 때문이다. 
    if alp == '<':
        for _ in range(len(stack)):
            ans += stack.pop() # pop으로 인해 자연스럽게 뒤집힌다.
    stack.append(alp) 
    if alp == '>': 
        for _ in range(len(stack)):
            ans += stack.pop(0)
    
    if alp == ' ' and '<' not in stack:
        stack.pop()
        for _ in range(len(stack)):
            ans += stack.pop()
        ans += ' '

if not stack:
    print(ans)
else:
    print(ans+''.join(stack)[::-1])