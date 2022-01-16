str_list = ['hi','mom','dad',['grandma','grandpa']]
new_list = str_list
copy_list = str_list[:]

str_list[0] = 'bye'  # Output: ['bye', 'mother', 'dad', ['nanna', 'grandpa']]
new_list[1] = 'mother' # Output: same as str_list
copy_list[2] = 'father'
copy_list[-1][1] = 'nanna'  # Output ['hi', 'mom', 'father', ['nanna', 'grandpa']]

'''
Why does changing copy_list[2] does not change 'dad' in str_list
but changing copy_list[-1][1] changes the 'grandma' in str_list?

Because copy_list != str_list
but copy_list[-1] == str_list[-1]
'''

'''
This is the peril of a list within a list:
when the list-within-list is copied, what copied is the reference,
not the elements themselves ( shallow copy).
Thus when you change the list-within-list in the copy, the original list-within-list is also changed.
'''

import copy
str_list_two = ['hi','mom','dad',['grandma','grandpa']] # Output: ['hi', 'mom', 'dad', ['grandma', 'grandpa']]
copy_list_two = copy.deepcopy(str_list_two)
copy_list_two[2] = 'father'
copy_list_two[-1][0]= 'nanna'  # Output: ['hi', 'mom', 'father', ['nanna', 'grandpa']]
