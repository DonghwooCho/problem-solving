import sys


N = int(sys.stdin.readline().rstrip())
raw_words = []
for i in range(N):
    raw_words.append(sys.stdin.readline().rstrip())

col_words = []
for i in range(N):
    col_word = ""
    for raw_word in raw_words:
        col_word = col_word + raw_word[i]

    col_words.append(col_word)

for i in range(N):
    if raw_words[i] != col_words[i]:
        print("NO")
        break
else:
    print("YES")
