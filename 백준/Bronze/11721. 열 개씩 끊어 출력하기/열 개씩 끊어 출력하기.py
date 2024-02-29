s = input()
ans = ''
while True:
    cnt=0
    for alp in s:
        ans += alp
        cnt+=1
        if cnt==10:
            print(ans)
            ans=''
            cnt=0
            
    break
print(ans)