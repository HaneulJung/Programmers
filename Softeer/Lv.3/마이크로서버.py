import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    service = list(map(int, sys.stdin.readline().split()))
    service.sort()

    start = 0
    end = N - 1

    server = 0

    # 메모리 600 이상이면 개별 서버 필요
    while start <= end and service[end] > 600:
        server += 1
        end -= 1
    
    # 메모리 300, 600 인 거 짝지어서 서버 배정
    while start < end and service[start] == 300 and service[end] == 600:
        server += 1
        start += 1
        end -= 1

    # 만약 짝지어지지 않은 300 남으면 카운트
    num300 = 0
    while start <= end and service[start] == 300:
        num300 += 1
        start += 1

    # 메모리 301 ~ 599 인 거 짝짓기 (남아있는 300 있으면 추가 고려)
    while start < end:
        if service[start] + service[end] <= 900:
            server += 1
            start += 1
            end -= 1
        elif num300 > 0:
            server += 1
            end -= 1
            num300 -= 1
        else:
            server += 1
            end -= 1

    if start == end:
        server += 1
        if num300 > 0:
            num300 -= 1

    server += (num300+2)//3
    print(server)


import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    service = list(map(int, sys.stdin.readline().split()))
    service.sort()

    num300 = 0
    for i in range(N):
        if service[i] == 300:
            num300 += 1

    server = 0
    start = num300
    end = N - 1

    while start <= end:
        server += 1
        if service[end] > 600:
            pass
        elif start != end and service[start] + service[end] <= 900:
            start += 1
        elif num300 > 0:
            num300 -= 1
        end -= 1

    server += (num300 + 2) // 3
    print(server)