fib1 = 1
fib2 = 1

N = input("Число Фибоначчи: ")
N = int(N)

i = 0
while i < N - 2:
    sum = fib1 + fib2
    fib1 = fib2
    fib2 = sum
    i = i + 1

print (fib2)
