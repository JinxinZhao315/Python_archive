# Find the max and min mileage of cars in the epaData file

def create_mileage_list(a_file):           # To create a list in which each element is a tuple consisting of mileage,car manufacturer and car model.
    mileage_list=[]
    for line in a_file:
        if line[0:5] == 'CLASS' or\
               'VAN' in line or\
               'PICKUP' in line:
            continue                                       #This ignores the rest of lines in the suite and continues the iteration from the next iterable
        line_list = line.split(',')
        car_tuple = (int(line_list[9]),line_list[1],line_list[2])
        mileage_list.append(car_tuple)                     # Remember every item in the list is still string. Convert them to int
    return mileage_list


def find_max_min_mileage(a_list,max_value,min_value):    # To find which car has the max/min mileage
    max_mileage_list = []
    min_mileage_list = []
    for car_tuple in a_list:
        if car_tuple[0] == max_value:                     
            max_mileage_list.append(car_tuple)
        if car_tuple[0] == min_value:
            min_mileage_list.append(car_tuple)
    return max_mileage_list, min_mileage_list

    
epa_file = open('epaData.csv','r')
mileage_list = create_mileage_list(epa_file)

max_mileage = max(mileage_list)[0]                        # Note that if we want to use max/min function to compare the mileage in tuples,which have other items, we need to put the mileage value at the first element of tuple
min_mileage = min(mileage_list)[0]                        # Because max and min use the first element to compare collections

max_mileage_list, min_mileage_list = find_max_min_mileage(mileage_list,max_mileage,min_mileage)

print('The max mileage is',max_mileage)
print('The min mileage is',min_mileage)
print()

print('Max mileage cars:')
for car_tuple in max_mileage_list:
    print(' ',car_tuple[1], car_tuple[2])
    
print('Min mileage cars:')
for car_tuple in min_mileage_list:
    print(' ',car_tuple[1], car_tuple[2])






