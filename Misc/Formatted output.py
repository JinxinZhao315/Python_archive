#Formatted output

number= int(input("Input an integer:"))
for a_number in range(0,number+1):
    new = a_number / 3 + 1
    print("{:10d} ---> {:>10.4f}".format(a_number,new))



'''Notes:
1.Remember there is a COLON!!
2.Remember, by default strings are left justified, numbers are right justified. if you
only type the spacing nubmer but no sign, it will be default justification.
3.descriptor: s for strings; d for integers; f for floats. 
3.Alignment + width + .precision + descriptor
'''
      
