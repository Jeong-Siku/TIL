import heapq
n = int(input())
cards = sorted([int(input()) for _ in range(n)])

result = 0
while cards:
    if len(cards)>2:
        two_sum = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, two_sum)
        result += two_sum
    elif len(cards)==2:
        two_sum = heapq.heappop(cards) + heapq.heappop(cards)
        result += two_sum
    else:
        result=0
        break

print(result)