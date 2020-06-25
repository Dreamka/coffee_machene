number = int(input().strip())

i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1

print(factorial)