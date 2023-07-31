import sys

A, B = map(int, sys.stdin.readline().split())

if A < B:
    print('B')
elif A > B:
    print('A')
else:
    print('same')