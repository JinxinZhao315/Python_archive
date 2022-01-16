# A function to check if two words are anagrams i.e.made up of same letters of different order
def test_anagram(word1,word2):
    word_set_one = sorted(word1)
    word_set_two = sorted(word2)
    return word_set_one == word_set_two

valid_input_bool = True   # This is called a boolean sentinel
while valid_input_bool:
    try:
        two_words = input("input two space-seperated words:")
        word1, word2 = two_words.split()
        valid_input_bool = False
    except ValueError:
        print("The input is not valid.")

# Method to keep asking for input until a correct one:
# put a boolean sentinel True, put a while loop on the sentinel, use try-except suit,and at the end of
# the try suit (i.e. got a good input), turn the boolean sentinel False to terminate while loop
        

if test_anagram(word1,word2):    #The rationale here is, you already made the function return True / False
    print('The two words are anagrams.') 
else:
    print('The two words are not anagrams.')

