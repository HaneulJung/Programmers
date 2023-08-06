import sys

K, P, N = map(int, sys.stdin.readline().split())

def function(value, n):
    if n == 1:
        return value
    
    if n % 2 == 0:
        tmp = function(value, n/2)
        return tmp * tmp % 1000000007
    else:
        tmp = function(value, (n-1)/2)
        return tmp * tmp * value % 1000000007
        
print(K * function(P, 10*N) % 1000000007)