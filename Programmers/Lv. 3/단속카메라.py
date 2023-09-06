def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    cam = -30001
    
    for route in routes:
        s, e = route
        if s > cam:
            cam = e
            answer += 1
    return answer