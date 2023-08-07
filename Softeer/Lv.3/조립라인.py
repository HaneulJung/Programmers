import sys

input = sys.stdin.readline

N = int(input())

A = []
B = []
move_AB = []
move_BA = []

for _ in range(N-1):
    a, b, ab, ba = map(int, input().split())
    A.append(a)
    B.append(b)
    move_AB.append(ab)
    move_BA.append(ba)

a, b = map(int, input().split())
A.append(a)
B.append(b)

dp_A = [0] * N
dp_A[0] = A[0]

dp_B = [0] * N
dp_B[0] = B[0]

for i in range(1, N):
    dp_A[i] = min(dp_A[i-1], dp_B[i-1] + move_BA[i-1]) + A[i]
    dp_B[i] = min(dp_B[i-1], dp_A[i-1] + move_AB[i-1]) + B[i]

print(min(dp_A[-1], dp_B[-1]))