def solution(arr):
    global answer
    answer = [0, 0]
    
    check(arr, [0, 0], len(arr))
    
    return answer
    
def check(arr, position, n):
    x, y, target = position[0], position[1], arr[position[0]][position[1]]
    
    for i in range(n):
        for j in range(n):
            if arr[x+i][y+j] != target:
                check(arr, [x,y], n//2)
                check(arr, [x,y+n//2], n//2)
                check(arr, [x+n//2,y], n//2)
                check(arr, [x+n//2,y+n//2], n//2)
                return
    
    answer[target] += 1