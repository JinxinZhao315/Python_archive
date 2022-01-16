def merge_sort(to_sort):
    ''' Input a list of numbers. Output the sorted list'''
    
    if len(to_sort)>1:
        mid = len(to_sort)//2
        left = to_sort[:mid]
        right = to_sort[mid:]

        merge_sort(left)
        merge_sort(right)

        head_left = 0
        head_right = 0
        tracker = 0

        while (head_left < len(left) and head_right < len(right) ):
            if left[head_left] < right[head_right]:
                to_sort[tracker] = left[head_left]
                head_left += 1
            else:
                to_sort[tracker] = right[head_right]
                head_right += 1
            tracker += 1


        # Dealing the situation in which left/right is longer than the other. In
        # this situation, just add whatever left onto to the tail of the merged list. 
        for i in range(head_left, len(left)):
            to_sort[tracker] = left[i]
            tracker += 1


        for i in range(head_right, len(right)):
            to_sort[tracker] = right[i]
            tracker += 1

    return to_sort


            
            
            
            
