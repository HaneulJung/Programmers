from collections import deque

def solution(N, road, K):
    
    dict_distance = {1 : 0}
    
    root = deque()
    root.append((1, 0))
    
    while root:
        cur_pos, distance = root.popleft()
        
        for r in road:
            if distance + r[2] > K:
                continue
            
            if r[0] == cur_pos:
                if r[1] in dict_distance.keys():
                    if distance + r[2] > dict_distance[r[1]]:
                        continue   
                dict_distance[r[1]] = distance + r[2]
                root.append((r[1], distance + r[2]))
            elif r[1] == cur_pos:
                if r[0] in dict_distance.keys():
                    if distance + r[2] > dict_distance[r[0]]:
                        continue   
                dict_distance[r[0]] = distance + r[2]
                root.append((r[0], distance + r[2]))
    
    return len(dict_distance)