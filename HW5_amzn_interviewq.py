"""
Create a function that will take a string as input and will return the 1st unique letter of the string.
If there is no unique string return an empty string.
"""

random_word = input("Enter a random word to find 1st unique letter:  ")
# def unique_letter(string):   # Simple Solution but not ideal because its time complexity is O(n^2)
#     string = string.lower()
#     for l in string:                      # O(n)
#         if string.count(l) == 1:    #O(n)
#             return l
#
# print(unique_letter(random_word))

def unique_ltr(string: str):
    string = string.lower()
    d = {}

    for letter in string:    # will iterate thru each letter
        if letter not in d:    # condition to check the letter in dic or not
            d[letter] = 1       # the letter will be added to dict like --> d = { 'g': 1, 'o':1}
        else:
            d[letter] += 1          # here if the letter already in dict then will add 1 like --> d = {'g': 1, 'o':2, }

        # print(d)   # {'g': 1} {'g': 1, 'o': 1} {'g': 1, 'o': 2} {'g': 2, 'o': 2} {'g': 2, 'o': 2, 'l': 1} {'g': 2, 'o': 2, 'l': 1, 'e': 1}
    for k, v in d.items():
        if v == 1:
            return k


print(unique_ltr(random_word))



