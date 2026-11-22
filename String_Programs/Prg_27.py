"""
27. Check whether a word exists in a sentence.
"""

sentence = input("Enter a Sentence = ")
word = input("Enter a word = ")
words = sentence.split()

if word in words :
    print("Word Exits in a Sentence.")
else:

    print("Word not Exits in Sentence.")
