def parse_individual_char(individual_char):
    element_str = ''
    quantity_str = ''   # put initialisation inside the loop means re-initialise every round of the loop
    for char in individual_char:
        if char.isalpha():
            element_str = element_str + char
        if char.isdigit():
            quantity_str = quantity_str + char
    if quantity_str == '':
        quantity_str = '1'
    return element_str,int(quantity_str)


# ========== Main =========

import sys

# Read the file
import csv
periodic_file = open("Periodic-Table.csv","r",encoding="windows-1252")
reader = csv.reader(periodic_file)

# create a dictionary
periodic_dict = {}
for line in reader:
    if line[0].isdigit():
        periodic_dict[line[1]] = line[:]

# Ask for input
compound_str = input('Type the hyphenated chemical formula of the compound.e.g. H2-S-O4: ')
compound_list = compound_str.split("-")

# Calculating atomic mass
atomic_mass = 0.0
print('The compound is made up of:',end=' ')


for individual_char in compound_list:
    element_str, quantity_int = parse_individual_char(individual_char)
    element_name = periodic_dict[element_str][5]
    print(element_name,end=',')
    element_mass = float(periodic_dict[element_str][6])*quantity_int
    atomic_mass += element_mass  # put initialisation outside of for loop means the value is accumulative
 

print('\nTotal atomic mass is',atomic_mass)
periodic_file.close()

    
    


















    
