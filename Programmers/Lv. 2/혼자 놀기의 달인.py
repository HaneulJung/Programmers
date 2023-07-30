def solution(cards):
    
    visited = [False for _ in range(len(cards))]
    
    results = []
    for i in range(len(cards)):
        if not visited[i]:
            position = cards[i] - 1
            visited[i] = True
            answer = 1
            
            while True:
                if not visited[position]:
                    visited[position] = True
                    position = cards[position] - 1
                    answer += 1
                else:
                    results.append(answer)
                    break
    
    results.sort(reverse=True)
    
    if len(results) > 1:
        return results[0] * results[1]          
    else:
        return 0