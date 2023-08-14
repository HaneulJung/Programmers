import sys
from pprint import pprint
from string import ascii_uppercase
from collections import deque

input = sys.stdin.readline

msg = deque(list(input().strip()))
key = input().strip()

alphabets = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Make Table
table = []
for k in key:
    if k not in table:
        table.append(k)
for alpha in alphabets:
    if alpha not in table:
        table.append(alpha)

key_table = [[0] * 5 for _ in range(5)]
for i in range(25):
    key_table[i//5][i%5] = table[i]

# 2글자씩 나누기
pair = []
check = []
while msg:    
    if msg[0] in check:
        if 'X' in check:
            check.append('Q')
        else:
            check.append('X')
    else:
        check.append(msg.popleft())    
    
    if len(check) == 2:
        pair.append(check)
        check = []

if check:
    check.append('X')
    pair.append(check)

# 암호화
answer = ''
for p in pair:    
    a, b = table.index(p[0]), table.index(p[1])

    ac, ar = a // 5, a % 5
    bc, br = b // 5, b % 5

    if ac == bc:
        answer += (key_table[ac][(ar+1)%5] + key_table[bc][(br+1)%5])
    elif ar == br:
        answer += (key_table[(ac+1)%5][ar] + key_table[(bc+1)%5][br])
    else:
        answer += (key_table[ac][br] + key_table[bc][ar])

print(answer)