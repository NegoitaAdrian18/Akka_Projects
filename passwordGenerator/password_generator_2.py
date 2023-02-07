import random


class PasswordCreator:
    def __init__(self):
        self.symbols = None
        self.numbers = None
        self.lowercase = None
        self.uppercase = None
        self.input_words = str(input("Enter a few words: "))

    def password_generator(self):
        self.uppercase = list(self.input_words.upper())
        self.lowercase = list(self.input_words.lower())
        self.numbers = list("1234567890")
        self.symbols = list("!@#$%^&*()")
        add_all_characters = self.uppercase + self.lowercase + self.numbers + self.symbols
        random.shuffle(add_all_characters)
        return "".join(add_all_characters)


final_password = PasswordCreator()

print(f"Your password is: {final_password.password_generator()[1:13]}")
