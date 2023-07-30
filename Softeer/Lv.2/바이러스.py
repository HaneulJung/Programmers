import sys

def virus_cnt(t):
    K, P, N = map(int, t.split())

    for i in range(N):
        K = (K * P) % 1000000007
    
    print(K)

t = sys.stdin.readline()
virus_cnt(t)