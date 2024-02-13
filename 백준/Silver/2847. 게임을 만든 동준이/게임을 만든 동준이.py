n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
reverse_scores = scores[::-1]

cnt = 0
point = reverse_scores[0]-1
for score in reverse_scores[1:]:
    if point <= score:
        cnt+=score-point
        point-=1 
    elif point > score:
        point=score-1
print(cnt)
