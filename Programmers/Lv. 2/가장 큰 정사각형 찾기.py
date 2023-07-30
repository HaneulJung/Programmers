def solution(board):
    height = len(board)
    width = len(board[0])
    
    for h in range(1, height):
        for w in range(1, width):
            if board[h][w] == 1:
                board[h][w] = min([board[h][w-1], board[h-1][w], board[h-1][w-1]]) + 1 
    
    m = 0
    for i in range(height):
        if max(board[i]) > m:
            m = max(board[i])
    
    return m ** 2