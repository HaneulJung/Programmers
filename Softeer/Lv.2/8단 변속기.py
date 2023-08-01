import sys

l = list(map(int, sys.stdin.readline().split()))

ascending = True
descending = True

for i in range(1,9):
    if i != l[i-1]:
        ascending = False
        break

for i in range(1,9):
    if (9-i) != l[i-1]:
        descending = False
        break

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")