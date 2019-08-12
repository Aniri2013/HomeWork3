G = int(input('Введи год - '))
if G % 4 == 0 and G % 100 != 0:
    print("Високосный")
elif G % 400 == 0:
        print("Високосный")
else:
    print("Обычный")

