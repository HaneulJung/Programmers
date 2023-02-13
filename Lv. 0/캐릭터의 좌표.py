def solution(keyinput, board):
    position = [0, 0]
    
    for key in keyinput:
        if key == "left":
            if position[0] > -(board[0] // 2):
                position[0] -= 1
        elif key == "right":
            if position[0] < (board[0] // 2):
                position[0] += 1    
        elif key == "up":
            if position[1] < (board[1] // 2):
                position[1] += 1    
        else:
            if position[1] > -(board[1] // 2):
                position[1] -= 1    
                
    return position