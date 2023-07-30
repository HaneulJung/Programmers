def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) != 0:
            if cards1[0] == g:
                cards1.remove(g)
                continue
        if len(cards2) != 0:
            if cards2[0] == g:
                cards2.remove(g)
                continue
        return "No"
    return "Yes"