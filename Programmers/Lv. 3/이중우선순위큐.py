import heapq

def solution(operations):
    answer = []
    
    maxHeap = []
    minHeap = []
    
    for operation in operations:
        cmd, num = operation.split(" ")
        
        if cmd == "I":
            heapq.heappush(maxHeap, -int(num))
            heapq.heappush(minHeap, int(num))
        else:
            if num == "1" and maxHeap:
                tmp = -heapq.heappop(maxHeap)
                minHeap.remove(tmp)
                
                
            elif num == "-1" and minHeap:
                tmp = -heapq.heappop(minHeap)
                maxHeap.remove(tmp)
                
    maxValue = -heapq.heappop(maxHeap) if maxHeap else 0
    minValue = heapq.heappop(minHeap) if minHeap else 0
    
    return [maxValue, minValue]