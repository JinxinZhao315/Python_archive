# Palindrome test using the string module and replace method.

import string

test = input ("Type the phrase you want to check:").lower()

bad_chars = string.whitespace + string.punctuation

for char in test:
    if char in bad_chars:  # the "in" means checking for membership
        test = test.replace(char,'') # means replacing all such characters with empty
        

reverse = test[::-1]

if test == reverse:
    print(\
        "The modified string is:{} \n\
        the reversal is:{} \n\
        String is a palindrome.".format(test,reverse))
# \n means "return" i.e. change line; \ is put at the end of each line to indicate continuity onto the next line.
else:
    print(\
        "The modified string is:{} \n\
        the reversa; is:{} \n\
        The phrase is not a palindrome.".format(test,reverse))


# string.replace('old','new',[count])
# default of count is "all", means all 'old' characters will be replaced with 'new' characters
# count = 1 means only the first 'old' character found will be replaced, =2 means only the first two, and so on. 

