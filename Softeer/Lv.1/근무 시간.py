import sys

def changeToMinute(time):
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    return hour * 60 + minute


work_time = 0

for _ in range(5):
    line = sys.stdin.readline().split()
    work_time += (changeToMinute(line[1]) - changeToMinute(line[0]))

print(work_time)