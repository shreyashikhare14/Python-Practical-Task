"""
37. Find the longest word in a sentence.
"""

sentence = input("Enter a Sentence = ")

words = sentence.split()

longest = ""

for word in words :
    if len(word)> len(longest):
        longest = word

print("Longest Word = ",longest)