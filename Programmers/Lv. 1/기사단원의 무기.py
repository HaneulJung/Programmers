def get_divisor_count(n):
    count = 0

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            count += 1
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        c = get_divisor_count(i)
        if c > limit:
            answer += power
        else:
            answer += c
            
    return answer