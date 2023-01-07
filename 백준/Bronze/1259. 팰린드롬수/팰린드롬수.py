import sys

# 1. 입력 받고 팰린드롬수 여부 출력
target = sys.stdin.readline().rstrip()
while target != "0":
    if list(target) == list(reversed(list(target))):
        print("yes")
    else:
        print("no") 
    target = sys.stdin.readline().rstrip()