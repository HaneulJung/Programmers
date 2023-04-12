def solution(n, wires):
    answer = []
    
    for i in range(len(wires)):
        new_wires = wires[:i] + wires[i+1:]
        wire_set = set(new_wires[0])
        check = [False for i in range(len(new_wires))]
        check[0] = True
        while True:
            stop = True
            for w in range(len(new_wires)):
                if check[w] == False:
                    if new_wires[w][0] in wire_set or new_wires[w][1] in wire_set:    
                        check[w] = True            
                        wire_set.add(new_wires[w][0])
                        wire_set.add(new_wires[w][1])
                        stop = False
            if stop:
                break
        answer.append(abs(2 * len(wire_set) - n))
    
    return min(answer)