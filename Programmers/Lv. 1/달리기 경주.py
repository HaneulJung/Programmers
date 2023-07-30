def solution(players, callings):
    dict1 = {}
    dict2 = {}
    for i, player in enumerate(players):
        dict1[i] = player
        dict2[player] = i
        
    for calling in callings:
        pos = dict2[calling]
        temp = dict1[pos - 1]
        
        dict2[temp] = pos        
        dict2[calling] = pos - 1
        dict1[pos - 1] = calling
        dict1[pos] = temp
    
    return list(dict1.values())