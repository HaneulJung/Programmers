import sys

input = sys.stdin.readline

N, T = map(int, input().split())


for _ in range(T):
    
    C = []
    D = []

    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        if i % 2 == 0:
            C.append(tmp[i])
        else:
            D.append(tmp[i])
    
    def check(cnt):
        S = [0] * N
        S[0] = C[0]
        for i in range(N-1):
            if S[i] >= cnt:
                S[i+1] = C[i+1] + D[i]
            elif S[i] + D[i] >= cnt:
                S[i+1] = C[i+1] + (S[i]+D[i]-cnt)
            else:
                return False
        if S[N-1] >= cnt:
            return True
        else:
            return False

    def bSearch(start, end):
        if start == end:
            return start
        mid = (start + end + 1) // 2
        if check(mid):
            return bSearch(mid, end)
        else:
            return bSearch(start, mid-1)

    print(bSearch(0, 2*10**12))