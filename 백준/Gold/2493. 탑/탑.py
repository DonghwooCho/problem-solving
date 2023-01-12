from collections import deque

# 1. 입력 받기

N = int(input())
height = deque(enumerate(list(map(int, input().split()))))

# 2. 수신한 탑 번호 출력
receiver = deque([(-1, -1)])
while height:
    if receiver[0][1] < height[0][1]:
        receiver.clear()
        receiver.append(height[0])
        print(0, end = ' ')
    elif receiver[-1][1] < height[0][1]:
        while receiver[-1][1] < height[0][1]:
            receiver.pop()
        print(receiver[-1][0] + 1, end = ' ')
        receiver.append(height[0])
    else:
        print(receiver[-1][0] + 1, end = ' ')
        receiver.append(height[0])
        
    height.popleft()