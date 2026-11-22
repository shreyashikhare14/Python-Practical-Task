"""
38. Find the shortest word in a sentence.
"""

sentence = input("Enter a Sentence =")
words = sentence.split()
shortest = words[0]

for word in words:
    if len(word)<len(shortest):
        shortest = word

print("Shortest Word is =",shortest)