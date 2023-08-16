import sys

input = sys.stdin.readline

N, B = map(int, input().split())

# 현재 최고, 최저 성능 확인
computers = list(map(int, input().split()))
min_power = min(computers)

def check(num):
    s = 0
    for c in computers:
        if c < num:
            s += (num-c)**2

    if s <= B:
        return True
    else:
        return False

def bSearch(start, end):
    if start == end:
        return start
        
    middle = (start + end + 1) // 2

    if check(middle):
        return bSearch(middle, end)
    else:
        return bSearch(start, middle-1)

print(bSearch(min_power, 2*10**9))