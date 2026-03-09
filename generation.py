from prompt import *
import secrets
import os

lowercase = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%&*?")

with open ("dictionary.txt") as file:
    word_list = file.read().split()


def generate_password(length, use_uppercase, use_numbers, use_symbols, use_words):
    password_chars = []
    allowed_chars = []
    allowed_chars.extend(lowercase)

    if use_numbers:
        allowed_chars.extend(numbers)
    if use_symbols:
        allowed_chars.extend(symbols)
    if use_uppercase:
        random_lower = secrets.choice(lowercase)
        password_chars.append(random_lower)

    for i in range(length - 1):
        random_character = secrets.choice(allowed_chars)
        password_chars.append(random_character)

    if use_uppercase and password_chars[0].isalpha():
        password_chars[0] = password_chars[0].upper()

    password = "".join(password_chars)
    return password

def generate_word_password():
    password_words = []
    
    for i in range(4):
        word = secrets.choice(word_list)
        password_words.append(word)

    password = "".join(password_words)
    return password


def password_generation():
    use_words = word_prompt()

    if use_words:
        password = generate_word_password()
    
    else:
        length = length_prompt()
        use_uppercase = upper_prompt()
        use_numbers = num_prompt()
        use_symbols = symbols_prompt()
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    return password
