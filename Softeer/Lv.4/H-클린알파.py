import sys

input = sys.stdin.readline

P, N = map(int, input().split())

A = list(map(int, input().split()))

virus = A[0]
for i in range(1, N):
    virus = (virus * P + A[i]) % 1000000007

print(virus) 