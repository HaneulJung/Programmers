import sys

N, K = map(int, sys.stdin.readline().split())

grades = list(map(int, sys.stdin.readline().split()))

for _ in range(K):
    A, B = map(int, sys.stdin.readline().split())
    print("{0:.2f}".format(sum(grades[A-1:B])/(B-A+1)))