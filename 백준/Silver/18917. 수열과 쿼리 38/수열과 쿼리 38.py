import sys

M = int(sys.stdin.readline().rstrip())

hap = 0
xor = 0
for i in range(M):
    query = sys.stdin.readline().rstrip()
    if query[0] == '1':
        x = int(query[2:])
        hap += x
        xor ^= x
    elif query[0] == '2':
        x = int(query[2:])
        hap -= x
        xor ^= x
    elif query[0] == '3':
        print(hap)
    else:
        print(xor)
