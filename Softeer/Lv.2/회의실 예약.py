import sys

N, M = map(int, sys.stdin.readline().split())

rooms = {}
for _ in range(N):
    name = sys.stdin.readline().strip()
    rooms[name] = [0]*18 + [1]

for _ in range(M):
    tmp = list(sys.stdin.readline().split())
    room_name = tmp[0]
    s, e = int(tmp[1]), int(tmp[2])
    for i in range(s, e):
        rooms[room_name][i] = 1

rooms = sorted(rooms.items(), key=lambda x : x[0])

for index, room in enumerate(rooms):
    print("Room {}:".format(room[0]))
    available_time = []
    isStarted = False
    for i in range(9, 19):
        if room[1][i] == 0 and not isStarted:
            start = i
            isStarted = True
        elif room[1][i] == 1 and isStarted:
            end = i
            isStarted = False
            available_time.append([start, end])

    if len(available_time) == 0:
        print("Not available")
    else:
        print("{} available:".format(len(available_time)))
        for time in available_time:            
            print("{0:02d}-{1}".format(time[0], time[1]))

    if index != len(rooms) - 1:
        print("-----")