def solution(priorities, location):
    answer = 0
    position = [0 for _ in range(len(priorities))]
    position[location] = 1
    
    while priorities:
        if priorities[0] >= max(priorities):
            priorities.pop(0)
            answer += 1
            if position.pop(0) == 1:
                return answer
        else:
            temp = priorities[0]
            priorities[:-1] = priorities[1:]
            priorities[-1] = temp
            
            temp2 = position[0]
            position[:-1] = position[1:]
            position[-1] = temp2