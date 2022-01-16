# Counting total hands, and number of Paris ( rank 1).
# WARNING: THE FILE YOU ARE ABOUT TO CHECK HAS 1 MILLION LINES


filename = input('Enter the name of the poker file:')
while True:
    try:
        a_file = open(filename,'r')
        break
    except IOError:
        print('Invalid file name entered')
        filename = input('Enter the name of the poker file:')
        
# Keep requiring for file name until a valid one is entered.

hand_count = 0
nothing = 0
one_pair= 0
two_pairs = 0
three = 0
straight = 0
flush = 0
full_house=0
four=0
straight_flush=0
royal_flush=0


for line in a_file:
    hand_count += 1
    rank = int(line.split(',')[-1])  # line.split(',') gives a list each character seperated by comma. [-1] asks for the last one of them. All list items are strings, so convert them to integers to do math.
    if rank == 0:
        nothing += 1
    if rank == 1 :
        one_pair += 1
    if rank == 2:
        two_pairs += 1
    if rank == 3:
        three += 1
    if rank == 4:
        straight += 1
    if rank == 5:
        flush += 1
    if rank ==6:
        full_house += 1
    if rank == 7:
        four += 1
    if rank == 8:
        straight_flush += 1
    if rank == 9:
        royal_flush += 1

print('Total hand count is',hand_count)
print("Nothing count is",nothing,",probability is {:8.5%}".format(nothing/hand_count))
print("One-pair count is",one_pair,",probability is {:8.5%}".format(one_pair/hand_count))
print("Two-pairs count is",two_pairs,",probability is {:8.5%}".format(two_pairs/hand_count))
print("Three-of-a-kind count is",three,",probability is {:8.5%}".format(three/hand_count))
print("Straight count is",straight,",probability is {:8.5%}".format(straight/hand_count))
print("Flush count is",flush,",probability is {:8.5%}".format(flush/hand_count))
print("Full-house count is",full_house,",probability is {:8.5%}".format(full_house/hand_count))
print("Four-of-a-kind count is",four,",probability is {:8.5%}".format(four/hand_count))
print("Straight Flush count is",straight_flush,",probability is {:8.5%}".format(straight_flush/hand_count))
print("Royal Flush count is",royal_flush,",probability is {:8.5%}".format(royal_flush/hand_count))
   




# Format of poker file:
# C1-suit, C1-rank, C2-suit, C2-rank, C3-suit, C3-rank, C4-suit, C4-rank, C5-suit, C5-rank, hand rank
# Thus for hand rank, checking the last number is enough.


# while True is an infinite loop.You have to break it when you find what you want! 
# This structure can always be used for "keeping requiring until a valid value is entered":

# while True:
#    try:
#        # The right thing to do
#        break
#    except Error:
#        print(Warning)
#        # The right thing to do
