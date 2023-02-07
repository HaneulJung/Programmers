def solution(n):
    array = []
    i = 1
    while len(array) <= 100:
        if i % 3 == 0:
            i += 1
        else:
            if '3' in str(i):
                i += 1
            else:
                array.append(i)
                i += 1
    return array[n-1]