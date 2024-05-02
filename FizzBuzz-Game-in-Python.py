# Logic:
# If a number is divisible by 3 it's a Fizz
# If a number is divisible by 5 it's a Buzz
# If a number is divisible by both 3 & 5, it's a FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
