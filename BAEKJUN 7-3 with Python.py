Z = input()

aToz = 'abcdefghijklmnopqrstuvwxyz'

for i in aToz:
    if i in Z:
        print(Z.index(i), end = ' ')
    else:
        print(-1, end = ' ')
