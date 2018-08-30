import string
import random

from nltk.corpus import words

def password_generator(size=8, strength=2):
    switch = {
        1: string.ascii_letters,
        2: string.ascii_letters + string.digits,
        3: string.ascii_letters + string.digits + string.punctuation,
    }
    chars = switch.get(strength)
    password = ''
    for i in range(size):
        password += random.choice(chars)
    return password

def username_generator(digits=3, word=2):

    # Generates a username with 2 words and 3 digits from a list of random words in the dictionary
    word_list = set(words.words())
    print(len(word_list))
    username = ''
    for i in range(word):
        username += word_list.get(random.randint(0, len(word_list)-1))
    for j in range(digits):
        username += random.choice(string.digits)
    return username

print("Select a password strength (1-3):")
str = int(input())
print("Select a password length")
len = int(input())
print(password_generator(len, str))

# print (username_generator())



