"""
37. Create a list and check palindrome list.
"""
lst1 = input("Enter a list elements = ")
lst = list(map(int,lst1.split()))


rev_lst = lst[::-1]

if lst == rev_lst:
    print("This List is Palindrome.")
else:
    print("This List is not Palindrome.")