def solution(people, limit):
    people.sort(reverse=True)
    
    s = 0
    e = len(people) - 1
    c = 0
    
    while s <= e:
        if people[s] + people[e] <= limit:
            e -= 1
            
        s += 1
        c += 1    
        
    return c
            