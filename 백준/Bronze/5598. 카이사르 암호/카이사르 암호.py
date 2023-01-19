plain = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
encrypt = "D E F G H I J K L M N O P Q R S T U V W X Y Z A B C".split()

S = list(input())

for i in S:
    print(plain[encrypt.index(i)], end = '')