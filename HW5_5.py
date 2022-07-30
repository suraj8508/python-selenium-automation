

random_word = input("Enter a word of your choice:  ")
def find_unique_letter(word):
    chars = list(word)
    # letter[:] = letter
    print(chars)
    unique_letter = {}
    for i in chars:
        #print(i)
        if i not in unique_letter.keys():
            unique_letter[i] = 1
        else:
            unique_letter[i] = unique_letter[i] + 1
    for key in unique_letter:
        if (unique_letter[key] == 1):
            return key

print(find_unique_letter(random_word))