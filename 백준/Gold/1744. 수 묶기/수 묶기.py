n = int(input())
p_arr = []
m_arr = []
z_arr = []
o_arr = []
for _ in range(n):
    num = int(input())
    if num>1:
        p_arr.append(num)
    elif num<0:
        m_arr.append(num)
    elif num==1:
        o_arr.append(1)
    else:
        z_arr.append(0)
    
p_arr.sort()
m_arr.sort()

# 양수 : 개수 짝,홀인지 최소값이 1인지
# 음수 : 개수 짝,홀인지 0이 존재하는지
ans = 0
if len(p_arr)<2:
    ans+=sum(p_arr)
elif len(p_arr)%2==0 :
    for i in range(0,len(p_arr),2):
        ans += p_arr[i]*p_arr[i+1]
elif len(p_arr)%2==1 :
    ans+=p_arr[0]
    for i in range(1,len(p_arr),2):
        ans += p_arr[i]*p_arr[i+1]

ans+=sum(o_arr)

if len(m_arr)<2 and z_arr:
    pass
elif len(m_arr)<2 and not z_arr:
    ans+=sum(m_arr)
elif len(m_arr)%2==0 :
    for i in range(0,len(m_arr),2):
        ans += m_arr[i]*m_arr[i+1]
elif len(m_arr)%2==1 and z_arr:
    for i in range(0,len(m_arr)-1,2):
        ans += m_arr[i]*m_arr[i+1]
elif len(m_arr)%2==1 and not z_arr:
    ans+=m_arr[-1]
    for i in range(0,len(m_arr)-1,2):
        ans += m_arr[i]*m_arr[i+1]

print(ans)