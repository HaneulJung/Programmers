def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
    	if num % i == 0:		
        	return False
    return True
    
    
def solution(n, k):
    answer = 0
    
    temp = ''
    while n // k != 0:
        temp += str(n % k)
        n //= k
    temp += str(n % k)
    
    for t in temp[::-1].split("0"):
        if t != "":
            if isPrime(int(t)):
                answer += 1
                
    return answer