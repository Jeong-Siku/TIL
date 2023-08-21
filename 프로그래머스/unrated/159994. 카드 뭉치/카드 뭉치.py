def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i in cards1[0]:
            cards1.pop(0)
        elif cards2 and i in cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"