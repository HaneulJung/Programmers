import sys

n = int(sys.stdin.readline())
offer = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp), 2):
        offer.append([tmp[j], tmp[j + 1], i + 1])
m = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))
scenarioes = []
for i in range(m):
    scenarioes.append([tmp[i], i + 1])

offer.sort()
scenarioes.sort()

total = 0
prev_pay = [0] * (n + 1)
s_index = 0
for i in range(len(offer)):
    size, payment, buyer = offer[i][0], offer[i][1], offer[i][2]
    if payment > prev_pay[buyer]:
        total += payment - prev_pay[buyer]
        prev_pay[buyer] = payment
    while s_index < len(scenarioes) and scenarioes[s_index][0] <= total:
        scenarioes[s_index].append(size)
        s_index += 1

scenarioes.sort(key=lambda x: x[1])
for i in scenarioes:
    if len(i) <= 2:
        print(-1, end=' ')
    else:
        print(i[2], end=' ')