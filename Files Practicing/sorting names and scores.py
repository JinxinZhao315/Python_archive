
def final_score(score_list):
    final_score = int(score_list[0])*0.3+\
    int(score_list[1])*0.3+\
    int(score_list[2])*0.4
    return final_score


score_file = open(input('Type the name of the file you want to open:'),'r')

print('{:>13s}{:>13s}'.format('Name','Grade'))

for line in score_file:
    line_list = line.strip().split(',')
    name_str = line_list[1] + ' ' +line_list[0]
    score_list = line_list[2:]
    grade_score = final_score(score_list)
    print('{:>13s}{:>13.2f}'.format(name_str,grade_score))
