import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    num = int(input().rstrip())
    if not num:
        # heap리스트가 빈리스트가 되어 인덱스에러가 날 수 있다.
        # 미니힙은 0을 리스트에 미리 추가하게 되면 최소값이 0이 되어 삭제되는 값이 꼬인다.
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)