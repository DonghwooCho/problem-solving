N = int(input())
words = set()
for i in range(N):
    words.add(input())

for e in words:
    if e[::-1] in words:
        print(len(e), e[len(e) // 2])
        break
