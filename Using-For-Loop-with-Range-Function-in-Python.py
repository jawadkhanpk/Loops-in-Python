# A simple Python Program demonstrating For Loops with Range Function
for number in range(1, 10):
    print(number)

# If we pass 3rd parameter in range it will count as step size in a loop
for step in range(1, 10, 2):
    print(step)


# Adding numbers from 1 upto 100
total = 0
for count in range(1 , 101):
    total += count
print(f"\nThe Sum of number from 1 upto 100 is: {total}")
