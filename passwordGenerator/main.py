import random

password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*():?|/"
lenght_pass = int(input("Enter the length of the password: "))
result = "".join(random.sample(password, lenght_pass))

print(f"The final password is: {result}")

