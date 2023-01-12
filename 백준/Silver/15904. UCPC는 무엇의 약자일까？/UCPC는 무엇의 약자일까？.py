# 1. 입력 받기
s = input()

# 2. 축약 여부 출력 하기
count = 0
for target in ['U', 'C', 'P', 'C']:
    try:
        s = s[s.index(target) + 1:]
        count += 1
    except:
        break

print("I love UCPC" if count == 4 else "I hate UCPC")