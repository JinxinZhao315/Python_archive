import numpy

def make_data_set(file_name):
    training_set_list = []
    training_file = open(file_name)
    for line_str in training_file:
        line_list = line_str.strip().split(',')
        id_str,a1,a2,a3,a4,a5,a6,a7,a8,a9,diagnosis_str = line_list
        if diagnosis_str == '4':
            diagnosis_str = 'm'
        else:
            diagnosis_str = 'b'
        patient_tuple=id_str,diagnosis_str,int(a1),int(a2),int(a3),int(a4),\
                       int(a5),int(a6),int(a7),int(a8),int(a9)
        training_set_list.append(patient_tuple)
    return training_set_list

def train_classifier(training_set_list):
    benign_count = 0
    malignant_count = 0
    benign_sums_list = [0]*9
    malignant_sums_list = [0]*9
    for patient_tuple in training_set_list:
        if patient_tuple[1] == 'b':
            benign_count += 1
            benign_sums_list = list(numpy.array(benign_sums_list)+numpy.array(patient_tuple[2:]))
        else:
            malignant_count += 1
            malignant_sums_list = list(numpy.array(malignant_sums_list)+numpy.array(patient_tuple[2:]))
            
    benign_ave_array = numpy.array(benign_sums_list)/benign_count
    malignant_ave_array = numpy.array(malignant_sums_list)/malignant_count
    classifier_list = list((benign_ave_array+malignant_ave_array)/2)
    
    return classifier_list

def classify_test_set_list(test_set_list,classifier_list):
    result_list = []
    for patient_tuple in test_set_list:
        benign_count = 0
        malignant_count = 0
        id_str,diagnosis_str = patient_tuple[:2]
        for index in range(9):
            if patient_tuple[index+2]>classifier_list[index]:
                malignant_count += 1
            else:
                benign_count += 1
        result_tuple = (id_str,benign_count,malignant_count,diagnosis_str)
        result_list.append(result_tuple)
    return result_list

def report_results(result_list):
    total_count = 0
    accurate_count = 0
    for result_tuple in result_list:
        total_count += 1
        diagnosis_str = result_tuple[3]
        prediction_str = ''
        if result_tuple[1] > result_tuple[2]:
            prediction_str = 'b'
        else:
            prediction_str = 'm'
        if prediction_str == diagnosis_str:
            accurate_count += 1
    accuracy_rate = accurate_count / total_count
    print('Out of {} patients,there are {} inaccuracies'.format(total_count,total_count-accurate_count))
    print('The accuracy rate of the classifier is {:.2%}'.format(accuracy_rate))


print('Reading in training data...')
training_file_name = 'cancer_training.txt'
training_set_list = make_data_set(training_file_name)
print('Done reading training data.\n')

print('Training classifier...')
classifier_list = train_classifier(training_set_list)
print('Done training classifier.\n')

print('Reading in test data...')
test_file_name = 'cancer_test.txt'
test_set_list = make_data_set(test_file_name)
print('Done reading test data.\n')

print('Classifying test data...')
result_list = classify_test_set_list(test_set_list,classifier_list)
print('Done classifying.\n')

report_results(result_list)

print('program finished.')
