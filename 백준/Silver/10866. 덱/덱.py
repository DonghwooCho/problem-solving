import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

deque = []
command = ""
for i in range(N):
    command = sys.stdin.readline().rstrip()
    
# 2. 덱 구현
    if "push_back" in command:
        deque.insert(0, int(command.split()[1]))
    elif "push_front" in command:
        deque.append(int(command.split()[1]))
    elif "pop_back" == command:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            del deque[0]
    elif "pop_front" == command:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif "size" == command:
        print(len(deque))
    elif "empty" == command:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif "front" == command:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])