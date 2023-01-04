import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

queue = []
command = ""
for i in range(N):
    command = sys.stdin.readline().rstrip()
    
# 2. 큐 구현
    if "push" in command:
        queue.insert(0, int(command.split()[1]))
    elif "pop" == command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    elif "size" == command:
        print(len(queue))
    elif "empty" == command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif "front" == command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])