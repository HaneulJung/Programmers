def solution(tickets):
    answer = []
    routes = {}

    for d, a in tickets:
        if d not in routes.keys():
            routes[d] = []
        routes[d].append(a)
    
    for rv in routes.values():
        rv.sort(reverse=True)
        
    
    st = ["ICN"]
    while st:
        place = st[-1]
        if (place not in routes) or (not routes[place]):
            answer.append(st.pop())   
        else:
            st.append(routes[place].pop())
    
    return answer[::-1]
