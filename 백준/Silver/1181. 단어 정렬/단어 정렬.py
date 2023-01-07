import sys

# 1. 입력 받기
N = int(sys.stdin.readline().rstrip())

words = [0] * N
for i in range(N):
    words[i] = sys.stdin.readline().strip()

# 2. 정렬 후 출력하기
words = list(sorted(set(words)))
words.sort(key = len)
for word in words:
    print(word)