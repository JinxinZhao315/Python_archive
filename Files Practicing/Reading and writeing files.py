# To open a file, read its lines, and reverse all lines then write the reversed lines into a new file.
# To reverse lines, we add each character of the old line to the LEFT of the new line.

#Creating file objects
input_file=open("input1.txt","r")  # for reading, the file must exsist already.
output_file=open("output1.txt","w") # for writing, you can create it here. 


# Iterate through the lines in the input file
for line in input_file: # Note that for loop can only be used in reading mode! Or unreadable error will occur.
    line = line.strip() 
    new_line = ''        
    for char in line:   
        new_line = char + new_line    # Concatenation. Note that SEQUENCE MATTERS in concatenation! If you want to add old characters to the LEFT, put it first!
    print(new_line,file = output_file)
    print('Line:{:15s} Reversed is: {:s}'.format(line,new_line))
    # Note these are in the indentation of the first for loop.
    # if these are out of the for loop, only the second line will be printed (i.e. the line before the loop normally exits)

input_file.close()
output_file.close()
     
    
