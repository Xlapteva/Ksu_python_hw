from statistics import mean
my_super_cool_list_of_dicts = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
{'school_class': '4b', 'scores': [8,7,6,5,4]}, 
{'school_class': '4c', 'scores': [5,6,5,6,5]}]

total_score_list = []

for dictionary in my_super_cool_list_of_dicts:
    overall = (sum(dictionary['scores']))/(len(dictionary['scores']))

    print(overall)

    total_score_list.append(overall)

   
  
print(sum(total_score_list)/len(total_score_list))

