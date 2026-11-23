"""
Mini Project 1: Text Analyzer System
"""

print("====================Text Analyzer System=====================")
string = input("Enter Your Text = ")
clean_text = string.strip()

print("Original String = ",string)
print("Clean Text = ",clean_text)

count_char = len(clean_text)
words = clean_text.split()
count_words = len(words)

print("Total Characters = ",count_char)
print("Total Words = ",count_words)

count_sentence = clean_text.count(".") + clean_text.count("?") + clean_text.count("!")
print("Total Sentence = ",count_sentence)

count_vowel = 0
count_consonant =0
count_digit = 0
count_spe_char =0

for i in clean_text:
    if i.lower() in 'aeiou':
        count_vowel = count_vowel + 1
    elif i.isalpha():
        count_consonant = count_consonant + 1

    elif i.isdigit():
        count_digit = count_digit + 1

    elif not i.isspace():
        count_spe_char = count_spe_char + 1

print("Vowel Count = ",count_vowel)
print("Consonant Count = ",count_consonant)
print("Digit Count = ",count_digit)
print("Special Character Count = ",count_spe_char)

upper_text = clean_text.upper()
print("Uppercase Text = ",upper_text)

lower_text = clean_text.lower()
print("Lowercase Text = ",lower_text)

search_word = input("Enter a word to Searched = ")

if search_word.lower() in clean_text.lower().split():
    print("Word Found 😊")
else:
    print("Word not Found ")

words= clean_text.lower().split()

frequency = {}

for word in words :
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word Frequency = ",frequency)

clean_text = " ".join(clean_text.split())

print("Text after removing extra spaces = ",clean_text)

# clean_text = ""
# while True:

#     print("====================Text Analyzer System=====================")
#     print("1.Enter Text")
#     print("2. Count Characters")
#     print("3.Count Words")
#     print("4.Count Sentences")
#     print("5.Count Vowels ")
#     print("6. Count Consonants")
#     print("7. Count Digits ")
#     print("8.Special Characters")
#     print("9.Convert to Uppercase")
#     print("10. Convert to Lowercase")
#     print("11.Search a Word")
#     print("12.Word Frequency")
#     print("13. Remove Extra Spaces")
#     print("0.Exit")

#     choice = int(input("Enter a Choice ="))

#     if choice == 1:
#         string = input("Enter Your Text = ")
#         clean_text = string.strip()
#         print("Text Saved Successfully ")

#     elif choice == 2:
#         if clean_text == "":
#             print("Please Enter a Text.")
#         else:
#             count_char = len(clean_text)
#             print("Character Count = ",count_char)

#     elif choice == 3:
#         words = clean_text.split()
#         count_words = len(words)
#         print("Word Count =",count_words)

#     elif choice == 4:
#         count_sentence = clean_text.count(".") + clean_text.count("?") + clean_text.count("!")
#         print("Sentence Count = ",count_sentence)

#     elif choice == 5:
#         vowel_count = 0
#         for i in clean_text:
#             if i.lower() in 'aeiou':
#                 vowel_count = vowel_count + 1

#         print("Vowel count is = ",vowel_count)
        
#     elif choice == 6:
#         consonant_count = 0
#         for i in clean_text:
#             if i.isalpha() and i.lower() not in 'aeiou':
#                 consonant_count = consonant_count + 1

#         print("Consonant count is = ",consonant_count)

#     elif choice == 7:
#         digit_count= 0
#         for i in clean_text:
#             if i.isdigit():
#                 digit_count = digit_count + 1
        
#         print("Digits Count is =",digit_count)

#     elif choice == 8:
#         spe_char_count =0

#         for i in clean_text:
#             if not i.isalnum() and not i.isspace():
#                 spe_char_count = spe_char_count + 1 
#         print("Special Character Count is = ",spe_char_count)

#     elif choice == 9:
#         upper_case = clean_text.upper()
#         print("Uppercase Text = ",upper_case)

#     elif choice == 10:
#         lower_case = clean_text.lower()
#         print("Lower Text = ",lower_case)

#     elif choice == 11:
#         search_word = input("Enter a word to Searched = ")
#         if search_word.lower() in clean_text.lower().split():
#             print("Word Found 😊")
#         else:
#            print("Word not Found ")

#     elif choice == 12 :
#         words= clean_text.lower().split()

#         frequency = {}

#         for word in words :
#             if word in frequency:
#                 frequency[word] = frequency[word] + 1
#             else:
#                 frequency[word] = 1

#         print("Word Frequency = ",frequency)

#     elif choice  == 13:
#         clean_text = " ".join(clean_text.split())
#         print("Text after removing extra spaces = ",clean_text)

#     elif choice == 0:
#         print("Thank You For Visiting.")
#         break
#     else:
#         print("Invalid Choice!")

