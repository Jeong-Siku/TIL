def solution(num, total):
    return list(range(int(total//num)-int(num/2)+1,int(total//num)+int(num/2)+1)) if total%num else list(range(int(total//num)-int(num/2),int(total//num)+int(num/2)+1))