def solution(arr):
    # copy()를 안하면 a값이 변경되면 리스트에 모든 값들이 변경된다. 주의할 것
    arr_list = [arr.copy()]
    a = arr.copy()
    for j in range(20):
        for i in range(len(a)):
            if a[i] >=50 and a[i]%2==0:
                a[i] = a[i]/2
            elif a[i] <50 and a[i]%2==1:
                a[i] = a[i]*2+1
        arr_list.append(a.copy())
        if arr_list[-1] == arr_list[-2]:
            return j