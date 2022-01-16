a_file=open("practice2.txt","w")
print("Yoho~",file=a_file)
print("Heyo~",file=a_file)
# a_file is practice2.txt's file object
# file = a_file is practice2.txt's file descriptor
a_file.close()
# Note that open is a function but close is a method.
