import sys

M, N, K = map(int, sys.stdin.readline().split())
code = ''.join(sys.stdin.readline().split())
ipt = ''.join(sys.stdin.readline().split())

if code in ipt:
    print('secret')
else:
    print('normal')