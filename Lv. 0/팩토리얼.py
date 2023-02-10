def solution(n):
    answer = 1
    i = 1
    for i in range(1, 100):
        if answer * i <= n:
            answer *= i
            i += 1
        else:
            return i-1