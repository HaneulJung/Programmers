def solution(numbers, k):
    p = 2 * (k-1)
    while p > len(numbers):    
        p -= len(numbers)
    return numbers[p]

def solution(numbers, k):
    return numbers[(2 * (k-1)) % len(numbers)]