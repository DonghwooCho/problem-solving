# 1. 입력 받기
while True:
    try:
        s, t = input().split()
# 2. 부분 문자열 여부 출력 하기       
        idx = -1
        for i in range(len(s)):
            if t.index(s[i]) >= 0:
                idx = t.index(s[i])
                t = t[idx + 1:]
            else:
                print("No")
                break
        print("Yes")
    except ValueError:
        print("No")
    except:
        break