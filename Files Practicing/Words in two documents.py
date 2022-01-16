import string

def process_line(a_file):
    word_set = set()
    for line in a_file:
        line_list = line.strip().split()    # the strip() here strips carriage returns
        for word in line_list:
            word = word.strip().strip(string.punctuation).lower()   # the strip() here strips spaces
            word_set.add(word)   # You have to add words to another empty set instead of just use set(line_list). Merely operating on the words does not change the line_list
    return word_set

def sort_set(a_set):
    set_list = list(a_set)
    set_list.sort()     # Note that you cannot nest functions and methods together
    return set_list
 


getty_file = open('Gettysburg Address.txt','r')
inde_file = open('Declearation of Independence.txt','r')

getty_set = process_line(getty_file)
inde_set = process_line(inde_file)


common_word_set = getty_set & inde_set
unique_word_getty = getty_set - inde_set
unique_word_inde = inde_set - getty_set


print('Number of: \n\
Common words: {} \n\
Unique words in the first: {} \n\
Unique words in the second: {} \n\
'.format(len(common_word_set),len(unique_word_getty),len(unique_word_inde)))


common_sorted_list = sort_set(common_word_set)
print('Common words used by both documents are:')

# The entire part means 'change line for every five words printed'
count = 0
for word in common_sorted_list:
    if count % 5 == 0:
        print()     # This equals 'carriage return'
    print('{:^10s}'.format(word),end=' ' )
    count += 1

