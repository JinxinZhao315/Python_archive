import string

def make_word_list(a_file):
    speech_list = []
    for line in a_file:
        word_list = line.split()
        for word in word_list:
            word = word.lower().strip(string.punctuation)
            if word != '':
                speech_list.append(word)
    return speech_list

def find_unique_words(a_list):
    unique_words = []
    for word in a_list:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


the_file = open("Gettysburg Address.txt","r")

speech_list = make_word_list(the_file)
unique_words = find_unique_words(speech_list)

print("Word count of the speech is:",len(speech_list))
print("Number of unique words used in the speech is:",len(unique_words))
