# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")

required_letters = int(input("How Many Letters You Would Like in Your Password? \n"))
required_numbers = int(input("How Many Numbers You Would Like in Your Password? \n"))
required_symbols = int(input("How Many Symbols You Would Like in Your Password? \n"))

# Easy Way to do it

# password = ""
# for char in range(1, required_letters + 1):
#     random_char_letters = random.choice(letters)
#     password += random_char_letters
#
# for char in range(1, required_numbers + 1):
#     random_char_number = random.choice(numbers)
#     password += random_char_number
#
# for char in range(1, required_symbols + 1):
#     random_char_symbols = random.choice(symbols)
#     password += random_char_symbols
# print(password)


# Hard Way to do it

password_list = []
for char in range(1, required_letters + 1):
    random_char_letters = random.choice(letters)
    password_list.append( random_char_letters)

for char in range(1, required_numbers + 1):
    random_char_number = random.choice(numbers)
    password_list.append(random_char_number)

for char in range(1, required_symbols + 1):
    random_char_symbols = random.choice(symbols)
    password_list.append(random_char_symbols)

# This line of code will shuffle the password which is stored in "password_list"
random.shuffle(password_list)

password_as_string = ""
for char in password_list:
    password_as_string += char
print(f"Your Randomized Password Should be: {password_as_string}")