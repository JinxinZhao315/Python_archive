def process_line(line_str):
    line_final_list =[]
    line_list = line_str.strip().split(',')
    for word in line_list:
        word = word.strip().strip(' ')
        line_final_list.append(word)
    return line_final_list



    
def count_income(train_data_file):
    greater_count = 0
    lesser_count = 0
    for line_str in train_data_file:
        if '?' in line_str:
            continue
        line_list = process_line(line_str)
        income = line_list[14]
        if income == '>50K':
            greater_count += 1
        else:
            lesser_count += 1
    return greater_count,lesser_count



def get_frequency(line_list,count_dict):
    for attribute in line_list:
        if not attribute.isdigit():
            if attribute in count_dict:
                count_dict[attribute] += 1
            else:
                count_dict[attribute] = 1   # Now you have a dictionary of all discrete attributes : their frequency 
    return count_dict



def give_values_to_attributes(numeric_dict):
    a2 = numeric_dict[a2]
    a6 = numeric_dict[a6]
    a7 = numeric_dict[a7]
    a8 = numeric_dict[a8]
    a9 = numeric_dict[a9]
    a10 = numeric_dict[a10]
    return a2,a6,a7,a8,a9,a10
   


def make_numeric_data_set(greater_count,lesser_count,data_file):
    numeric_data_set_list = []
    greater_count_dict = {}
    lesser_count_dict = {}
    for line_str in data_file:
        if '?' in line_str:
            continue
        line_list = process_line(line_str)
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,income = line_list
        if income == '>50K':
            greater_count_dict = get_frequency(line_list,greater_count_dict)
        else:
            lesser_count_dict = get_frequency(line_list,lesser_count_dict)
    greater_attribute_numeric_dict = {attribute:frequency/greater_count for attribute,frequency in greater_count_dict.items()}
    lesser_attribute_numeric_dict = {attribute:frequency/lesser_count for attribute,frequency in lesser_count_dict.items()}

    for line_str in data_file:
        if '?' in line_str:
            continue
        line_list = process_line(line_str)
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,income = line_list
        if income == '>50K':
            a2,a6,a7,a8,a9,a10 = give_values_to_attributes(greater_attribute_numeric_dict)
        else:
            a2,a6,a7,a8,a9,a10 = give_values_to_attributes(lesser_attribute_numeric_dict)
        person_tuple = int(a1),float(a2),int(a5),float(a6),float(a7),float(a8),float(a9),float(a10),income
        numeric_data_set_list.append(person_tuple)
    return numeric_data_set_list


def train_classifier(numeric_train_set_list):
    return []

def classify_test_set_list(test_set_list,classifier_list):
    return []

def report_results(result_list):
    return []




def main():
    print('Reading in training data...')
    train_data_file = open('adult_train.txt')
    train_greater_count,train_lesser_count = count_income(train_data_file)
    numeric_train_set_list = make_numeric_data_set(train_greater_count,train_lesser_count,train_data_file)
    print('Done reading training data.\n')

    print('Training classifier...')
    classifier_list = train_classifier(numeric_train_set_list)
    print('Done training classifier.\n')

    print('Reading in test data...')
    test_data_file = open('adult_test.txt')
    test_greater_count,test_lesser_count = count_income(test_data_file)
    numeric_test_set_list = make_numeric_data_set(test_greater_count,test_lesser_count,test_data_file)
    print('Done reading test data')

    print('Classifying test data...')
    result_list = classify_test_set_list(numeric_test_set_list,classifier_list)
    print('Done classifying test data')

    report_results(result_list)

    print('Program finished')

