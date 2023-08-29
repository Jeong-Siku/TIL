def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i<j:
                if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                    return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        cur=phone_book[i]
        nex=phone_book[i+1]
        length=len(cur)
        if cur[0]!=nex[0]:
            continue
        if cur == nex[:length]:
            return False
    return True