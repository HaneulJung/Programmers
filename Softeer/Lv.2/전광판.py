import sys

digit = {'0':0b1111110, '1':0b0011000, '2':0b0110111, '3':0b0111101, '4':0b1011001, \
            '5':0b1101101, '6':0b1101111, '7':0b1111000, '8':0b1111111, '9':0b1111101, 'x':0b0000000}

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = sys.stdin.readline().split()

    if len(A) != 5:
        A = 'x'*(5-len(A)) + A

    if len(B) != 5:
        B = 'x'*(5-len(B)) + B

    cnt = 0
    for i in range(5):
        cnt += (bin(digit[A[i]]^digit[B[i]]).count('1'))
    
    print(cnt)
