def hanoi(start, mid, end, answer, n):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(start, end, mid, answer, n - 1)
    answer.append([start, end])
    hanoi(mid, start, end, answer, n - 1)
    return answer
def solution(n):
    return hanoi(1, 2, 3, [], n)