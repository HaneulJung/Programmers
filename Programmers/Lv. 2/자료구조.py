# 리스트로 스택 선언
stack = []

# 스택에 데이터 push
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# 스택에서 데이터 pop
stack.pop()

print(stack)

from collections import deque

# 큐 선언
queue = deque()

# 큐에 데이터 enqueue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

# 큐에서 데이터 dequeue
data = queue.popleft()

print(queue)

import heapq

# 힙 선언 (기본은 최소힙)
heap = []

# 힙에 데이터 push
values = [2,5,6,1,3,7,4]
for value in values:
    heapq.heappush(heap, value)

print(heap)

# 최소값 얻기
data = heapq.heappop(heap)

print(data)
print(heap)

# 최대힙 만들기
# 힙 선언
heap = []

# 힙에 데이터 push
values = [2,5,6,1,3,7,4]
# 부호를 변경하여 push
for value in values:
    heapq.heappush(heap, -value)

print(heap)

# 최대값 얻기
# 부호를 다시 변경하여 원래 숫자 얻기
data = -heapq.heappop(heap)

print(data)
print(heap)