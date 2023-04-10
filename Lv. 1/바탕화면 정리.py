def solution(wallpaper):
    
    row_len = len(wallpaper)
    col_len = len(wallpaper[0])    
    
    a, b = [], []
    for i in range(row_len):
        for j in range(col_len):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]