def solution(dots):
    x = []
    y = []
    for d in dots:
        x.append(d[0])
        y.append(d[1])
    return (max(x) - min(x)) * (max(y) - min(y))