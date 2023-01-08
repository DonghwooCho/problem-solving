from collections import deque

# 1. 입력 받기
T = int(input())

# 2. AC 수행 결과 출력
for i in range(T):
    p = input()
    n = int(input())
    arr = input()
    
    if len(arr) >= 2:
        arr = deque(list(arr[1:-1].split(',')))
    else:
        print('error')
        continue

    if p.count('D') > n:
        print('error')
    elif p.count('D') == n:
        print('[]')
        continue
    else:
        arrow = True
        for j in range(len(p)):
            if p[j] == 'R':
                arrow = not arrow
            else:
                if arrow:
                    arr.popleft()
                else:
                    arr.pop()

        if p.count('R') % 2 == 1:
            arr = deque(list(reversed(arr)))

        print('[', end = '')
        print(','.join(arr), end = '')
        print(']')