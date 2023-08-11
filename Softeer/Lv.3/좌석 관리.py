import sys

input = sys.stdin.readline

def checkIn(cid):
    if cid in haveLunch.keys():
        if haveLunch[cid] == 'x':
            print(f'{cid} already ate lunch.')
        else:
            print(f'{cid} already seated.')
    else:
        findSeat(cid)

def checkOut(cid):
    if cid in haveLunch.keys():
        if haveLunch[cid] == 'x':
            print(f'{cid} already left seat.')
        else:
            x, y = haveLunch[cid]
            print(f'{cid} leaves from the seat ({x}, {y}).')
            haveLunch[cid] = 'x'
            seats[x][y] = 0
    else:
        print(f"{cid} didn't eat lunch.")

def checkEmpty(arr):
    for i in range(N+1):
        for j in range(1, M+1):
            if arr[i][j] > 0:
                return False
    return True

def findSeat(cid):
    if checkEmpty(seats):
        seats[1][1] = 1
        haveLunch[cid] = [1, 1]
        print(f'{cid} gets the seat (1, 1).')
    else:
        safety = [0, 0]
        max_safety = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if seats[i][j] or seats[i-1][j] or seats[i+1][j] or seats[i][j-1] or seats[i][j+1]:
                    continue
                else:
                    min_safety = 20*20
                    for axis in haveLunch.values():
                        if axis == 'x':
                            continue
                        x, y = axis
                        d = ((i-x)**2 + (j-y)**2)**0.5
                        if min_safety > d:
                            min_safety = d
                            temp = [i, j, d]
                if max_safety < temp[2]:
                    max_safety = temp[2]
                    safety = [temp[0], temp[1]]
        if safety == [0, 0]:        
            print('There are no more seats.')
        else:
            xx, yy = safety
            
            haveLunch[cid] = [xx, yy]
            seats[xx][yy] = 1
            print(f'{cid} gets the seat ({xx}, {yy}).')    


N, M, Q = map(int, input().split())

haveLunch = {}

seats = [[0] * (M+2) for _ in range(N+2)]

for _ in range(Q):
    state, cid = input().split()
    if state == 'Out':
        checkOut(cid)
    else:
        checkIn(cid)