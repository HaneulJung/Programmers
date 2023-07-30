def solution(m, n, board):
    checks = [[(0,1), (1,1), (1,0)], [(0,-1), (1,-1), (1,0)], \
             [(0,1), (-1,1), (-1,0)], [(0,-1), (-1,-1), (-1,0)]]
    
    answer = 0
    
    board_list = []
    for b in board:
        board_list.append(list(b))
    
    while True:
        delete = set()    
        for i in range(m):
            for j in range(n):
                for check in checks:
                    for k in range(3):
                        t = board_list[i][j]
                        if t == " ":
                            break
                        if (i+check[k][0] < 0 or i+check[k][0] >= m or\
                            j+check[k][1] < 0 or j+check[k][1] >= n):
                            break
                        if t != board_list[i+check[k][0]][j+check[k][1]]:
                            break
                    else:
                        delete.add((i, j))
        
        if len(delete) == 0:
            break
        
        answer += len(delete)
        
        for d in delete:
            board_list[d[0]][d[1]] = " "
        
        for i in range(n):
            for j in range(m-1, -1, -1):  
                if board_list[j][i] == " ":
                    for k in range(j-1,-1,-1):
                        if board_list[k][i] != " ":
                            board_list[j][i] = board_list[k][i]
                            board_list[k][i] = " "
                            break     
                
        
        
    return answer