def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

from itertools import permutations

def solution(numbers):
    answer = set()
    
    for i in range(1,len(numbers)+1):
        temp = list(permutations(numbers, i))
        for t in temp:
            if isPrime(int(''.join(t))):
                answer.add(int(''.join(t)))
        
    return len(answer)