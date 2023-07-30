def solution(cacheSize, cities):
    answer = 0
    
    cities = list(map(lambda x: x.lower(), cities))
    
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if city in cache:
            answer += 1
        else:
            answer += 5
            
        if len(cache) >= cacheSize:
            if city in cache:
                cache.remove(city)
            else:
                cache.pop(0)
                
        cache.append(city)
    
    return answer