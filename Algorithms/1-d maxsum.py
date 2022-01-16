def maxsum(a_list):
    current_sum = 0
    max_sum = 0
    for i in range(len(a_list)):
        current_sum = max(0,current_sum)
        # why this? Since if the sum from start of the list to current position is negative,
        # adding this part from start of list to current position will make the
        # sum of the following part smaller. Thus this part from start of list to current position
        # should be dumped. i.e. reset current_sum to zero.
        current_sum += a_list[i]
        max_sum = max(current_sum,max_sum)
    return max_sum
