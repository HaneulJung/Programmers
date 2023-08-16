import sys

# 서 -> 동 점점 높은 돌 밟다가 낮은 돌
# 밟을 수 있는 돌의 최대 개수

input = sys.stdin.readline

N = int(input())

rocks = list(map(int, input().split()))

def bSearch(arr, start, end, num):
    if start == end:
        return start
    mid = (start + end) // 2

    if arr[mid] < num:
        return bSearch(arr, mid+1, end, num)
    else:
        return bSearch(arr, start, mid, num)

dp_up = [rocks[0]]
cnt_up = [1] * N
for i in range(1, N):
    if rocks[i] > dp_up[-1]:
        dp_up.append(rocks[i])
        cnt_up[i] = len(dp_up)
    else:
        idx = bSearch(dp_up, 0, len(dp_up)-1, rocks[i])
        dp_up[idx] = rocks[i]
        cnt_up[i] = idx+1
    
    

dp_down = [rocks[-1]]
cnt_down = [1] * N
for i in range(N-2, -1, -1):
    if rocks[i] > dp_down[-1]:
        dp_down.append(rocks[i])
        cnt_down[i] = len(dp_down)
    else:
        idx = bSearch(dp_down, 0, len(dp_down)-1, rocks[i])
        dp_down[idx] = rocks[i]
        cnt_down[i] = idx+1
        
result = 0
for i in range(N):
    result = max(result, cnt_up[i]+cnt_down[i]-1)

print(result)