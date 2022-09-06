from string import punctuation, ascii_uppercase, ascii_lowercase, digits, ascii_letters
from random import choices
import argparse


def my_pass_maker(length=8, upper=False, lower=False, digit=False, punc=False):
    pool = ""
    if upper:
        pool += ascii_uppercase
    if lower:
        pool += ascii_lowercase
    if digit:
        pool += digits
    if punc:
        pool += punctuation
    if pool == "":
        pool = ascii_letters
    return "".join(choices(pool, k=length))


def print_pass():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int, help="length of the password")
    parser.add_argument("-u", "--upper", help="Use uppercase letters", action="store_true")
    parser.add_argument("-l", "--lower", help="Use lowercase letters", action="store_true")
    parser.add_argument("-d", "--digit", help="Use digits letters", action="store_true")
    parser.add_argument("-p", "--punc", help="Use punctuations letters", action="store_true")
    args = parser.parse_args()
    print(my_pass_maker(args.length, args.upper, args.lower, args.digit, args.punc))


print_pass()
