# Printing a line in a particular file
# Using try-except construct
# A good program: robustness

try:
    file = open(input("Input the file name:"),"r")  # potential error 1 : user provides a file name that does not exist
    target_nubmer = int(input("Input the number of the line you want to print:")) # potential error 2 : user does not provide an integer for line number
    line_count = 1
    for line in file:
        if line_count == target_nubmer:
            print("Line",target_nubmer,"in the file is",line)
            break
        line_count += 1
        # To find the line with the target line number, we just check if the target number equals to a line count, to which we add 1 for every iteration.
        # Total times of iteration (i.e. max line_count) is the total number of lines a file has.
        # i.e. we only check line number but do not check line content.
    else:
        print("The line number does not exist in the file")
        # Revision of for...else... loop with a break in for suite: else is only entered when for loop normally exists i.e. search fails
        
    file.close() # Remember this! 


except IOError:   # handling potential error 1
    print("The file you seek does not exist.")

except ValueError:  # handling potential error 2
    print("The line number input is not a legal integer.")


# This program actually handles three bad inputs
# The first two are the two potential errors.
# The third is when the user inputs a target number that exceeds the total line number of the file. See the for loop

    
