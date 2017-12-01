# Not completed yet, still working on it.

# File:    bruteforce
# Project: gmap
# Product: IntelliJ IDEA
# User:    grant.stokley
# Date:    12/01/2017
# Time:    09:00
# Author   grant.stokley


import itertools
import string
import sys


def guess_password(real):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    attempts = 0
    for password_length in range(1, len(str) + 1):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)


str = input("Enter a password to crack: ")
print("I got: ", str)
print(guess_password(str))
