def solution(land):
    for l in range(1,len(land)):
        land[l][0] += max(land[l-1][1], land[l-1][2], land[l-1][3])
        land[l][1] += max(land[l-1][2], land[l-1][3], land[l-1][0])
        land[l][2] += max(land[l-1][3], land[l-1][0], land[l-1][1])
        land[l][3] += max(land[l-1][0], land[l-1][1], land[l-1][2])
    return max(land[-1])