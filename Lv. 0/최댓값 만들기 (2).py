def solution(numbers):
    s = sorted(numbers)
    return max(s[0]*s[1], s[-2]*s[-1])