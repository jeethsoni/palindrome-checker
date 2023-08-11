"""
A python script to check if a string is palindrome or not

@usage python3 check-palindrome.py "Dammit, I'm mad!"
"""

import re


def main():

    # empty lists 
    backward_phrase = []

    # welcome message
    print("Welcome to palindrome checker")
    print("It's stunning how forwards and backwards read the same :)\n")

    # user input string 
    phrase = input("Enter a string: ").lower()

    # removes punctuation from the string
    new_phrase = re.sub(r'[^\w\s]', '', phrase)

    # removes whitespace from the string
    new_word = list(new_phrase.replace(" ", ""))

    # flip the new word list back and append to the list variable
    for word in reversed(new_word):
        backward_phrase.append(word)

    # if both lists are exactly the same then it's palindrome
    if (new_word == backward_phrase):
        print("Woohoo, This phrase is palindrome")
    else:
        print("whoops, this string is not palindrome")


if __name__ == "__main__":
    main()
