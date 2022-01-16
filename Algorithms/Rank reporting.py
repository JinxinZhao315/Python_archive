ranks=[3,4,3,0,2,2,3,0]

def solution(ranks):
    ranks = sorted(ranks)
    ranks_count_dict = {}
    report_count_dict = {}
    for number in ranks:
        if number in ranks_count_dict:
            ranks_count_dict[number] += 1
        else:
            ranks_count_dict[number] = 1
    keys_list = sorted(ranks_count_dict.keys())
    for m in range(0,len(keys_list)):
        if keys_list[m]+1 in keys_list:
            report_count_dict[keys_list[m]] = ranks_count_dict[keys_list[m]]
        else:
            report_count_dict[keys_list[m]] = 0
    return sum(report_count_dict.values())
        
    
    
            
            
        
