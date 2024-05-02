# Way1 using step size
total = 0
for number in range(2, 101, 2):
    total += number
print(total)


# Way 2 using calculation
total2 = 0
for number2 in range(1, 101):
    if number2 %2 == 0:
        total2 += number2
print(total2)