"""
28. Count the number of words in a sentence.
"""

sentence = input("Enter a Sentence = ")
words = sentence.split()
count = len(words)
print("Total Number of words = ",count)