# Find words containing 'aeiou' in that order
# Use functions

data_file = open("wordlist.txt", "r")

def clean_word(word):
    return word.strip().lower()   # In dictionary, there is a carriage return after every word, though you don't see.Thus we strip the words, and convert them all to lowercase for consistency.

def get_vowels(word):
    vowels= "aeiou"
    vowels_in_word = ""    # Make a collection of vowels in the word
    for char in word:
        if char in vowels:      # If there is a vowel in the word, add it to the collection
            vowels_in_word += char
    return vowels_in_word   # And return that collection


print("Find words containing 'aeiou' in that order:")
for word in data_file:
    word = clean_word(word)
    if len(word) <= 6:    # Since there are five vowels, words of length below 6 need not be considered
        continue
    vowels_str = get_vowels(word)
    if vowels_str == 'aeiou':  # If the collection matches aeiou EXACTLY i.e. in order, then print the word. 
        print(word)



