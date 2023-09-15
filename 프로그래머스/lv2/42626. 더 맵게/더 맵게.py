# 정렬 상관없이 수시로 변화하는 리스트에 사용
from collections import deque
# 루트의 값이 가장 작은 값을 갖는 리스트
import heapq
def solution(scoville, K):    
    # 개수가 2개이상, 변경된 뒤에 값이 k보다 높으면 제외
    # 개수가 1개면 -1을 반환
    # 최소횟수
    
    # heapq형식으로 변환
    heapq.heapify(scoville)
    now = scoville[0]
    answer = 0
    while now<K and len(scoville)>=2:
        # heapq에서 루트 값 반환 후 삭제
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first+second*2
        heapq.heappush(scoville,new)
        answer+=1
        now = scoville[0]
        
    if min(scoville)<K:
        return -1
    return answer
