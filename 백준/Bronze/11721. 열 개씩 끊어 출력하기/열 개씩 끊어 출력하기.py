word = input()

for i in range(len(word) // 10):
    print(word[i * 10:(i + 1) * 10])

if len(word) % 10 != 0:
    print(word[-(len(word) % 10):])
