import random


# input_data = str(input("Write 3 words: "))
# password_length = int(input("Numbers of elements from password: "))
#
# upper_characters = list(input_data.upper())
# lower_characters = list(input_data.lower())
# upper_lower = upper_characters + lower_characters
# declaring_frase = "".join(upper_lower)
# print(declaring_frase)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# symbols = list("!@#$%^&*()|/")
#
# print(input_data)
# print(upper_characters)
# print(lower_characters)
#
# creator = str(upper_characters + lower_characters + numbers + symbols)
#
# print(creator)
# final_pass = "".join(random.sample(creator, password_length))
#
# print(final_pass)

letters = str(input("input: "))
#letters = 'qwertyuiopasdfghjklzxcvbnm'
uppercase = list(letters.upper())
lowercase = list(letters.lower())
numbers = list("1234567890")
simbols = list("!@#$%^&*()")

all = uppercase+lowercase+numbers+simbols

print(random.shuffle(all))

password = "".join(all)

print(password[0:12])
print(type(letters))