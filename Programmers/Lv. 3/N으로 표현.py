def solution(N, number):
    tmp = [set() for i in range(9)]
    
    for i in range(1,9):
        tmp[i].add(int(str(N)*i))    # 나열
        for j in range(1,i):
            for n1 in tmp[j]:
                for n2 in tmp[i-j]:
                    tmp[i].add(n1 + n2)    # 더하기
                    tmp[i].add(n1 - n2)    # 빼기
                    tmp[i].add(n2 - n1)    # 빼기
                    if n1 != 0:
                        tmp[i].add(n2 // n1)    # 나누기
                    if n2 != 0:
                        tmp[i].add(n1 // n2)    # 나누기
                    tmp[i].add(n1 * n2)    # 곱하기

        if number in tmp[i]:
            return i
                    
    return -1