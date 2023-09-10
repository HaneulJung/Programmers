def solution(distance, rocks, n):
    '''
    출발지점부터 distance만큼 떨어진 곳에 도착지점
    사이에는 바위들이 있는데 몇개 제거하려고 함
    바위를 n개 제거 후 각 지점 사이의 거리의 최솟값 중 가장 큰 값을 return
    ''' 
    
    # 바위 순서대로 정렬
    rocks.append(distance)
    rocks.sort()
    
    answer = 0
    
    s, e = 0, distance
    
    while s <= e:
        m = (s + e) // 2
        
        cur, cnt = 0, 0
        minValue = 1000000001
        for rock in rocks:
            dis = rock - cur
            if dis < m:
                cnt += 1
            else:
                cur = rock
                minValue = min(minValue, dis)
        
        if cnt > n:
            e = m - 1
        else:
            answer = minValue
            s = m + 1
        
    return answer