# To count the frequency of a word's appearance in a file.

import string

filename = input('Type the name of the file you want to open:')
while True:
    try:
        the_file = open(filename,'r')
        break
    except IOError:
        print("The file you required is not found.")
        filename = input('Type the name of the file you want to open:')

'''Revision: How to keep asking for a file name until a valid one is given.
remember do not put open() in the except suite: or 'when handling this exception another exception occurred'
Put the filename = input('...') out of the try-except suite and only ask for filename in the except suite.
'''
        

        
count_dict = {}
'''Note that you MUST NOT put the initialisation in the for loop,
or at the start of every loop the dictionary is initialised again to empty!
Put all initialisation in MAIN PROGRAM! '''



for line in the_file:
    line_list=line.strip().split()
    for word in line_list:
        word = word.lower().strip().strip(string.punctuation)
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
            
'''An alternative for adding words as keys & adding frequency: 
count_dict[word] = count_dict.get(word,0) + 1
        # a_dict.get(key,deault) method: Output the value of the key if the key exists, 
        # output the default value if the key does not exist.(no error reported)
        # This line means "the value of the key is the current value +1 if key exist, and is 0+1 if key does not exist"'''
        

target_word = input("Which word's frequency do you want to check? \
Type 'all' if you want to see the entire list: ")

if target_word == 'all':
    print("{:^15s}{:^15s}".format('Word','Count'))
    print("-"*30)
    
    value_key_list = []
    for key,value in count_dict.items():
        value_key_list.append((value,key))
    value_key_list.sort()
    for value,key in value_key_list:
        print("{:^15s}{:^15d}".format(key,value))
        
        '''this entire part is to sort the order of key-value pairs. Since there is literally no order
        in dictionary, to get a pretty output we can convert the key-value pairs into a list of tuples,
        then sort the list. However when dealing with tuples/lists, .sort() method sorts according to the first
        element, thus we put the tuple as (value,key). But after sorting when we print, we
        still print (key,value)'''

else:
    try:
        word_frequency = count_dict[target_word]
        print("The frequency of the word is",word_frequency)
    except KeyError:
        print("The word does not exist in the file")



