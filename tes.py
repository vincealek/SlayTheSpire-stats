import json
import os

# directory_path = "DEFECT"
# directory_path = "THE_SILENT"

# List all files in the directory

def isHeartRun(data) :
    return data['damage_taken'][-1]['enemies'] == 'The Heart';

def calculate_card_count(data, count) :
    for s in data['master_deck'] :
        if(s[-2] == '+') :
            s = s[:-2]
        if(s in count) :
            count[s] = count[s]+1
        else :
            count[s] = 1

def calculate_relic_count(data, count) :
    for s in data['relics'] :
        if(s in count) :
            count[s] = count[s]+1
        else :
            count[s] = 1

# Iterate through the files and read each one

def calculate_data(directory_path, winning_card_count, winning_relic_count) :
    files = os.listdir(directory_path)
    
    total_win = 0;
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r') as file:
            
            data = json.load(file)
            if data['victory'] and isHeartRun(data) :
                # print(file_name,end = ' ')
                # print(data['ascension_level'])
                total_win += 1
                calculate_card_count(data, winning_card_count);
                calculate_relic_count(data, winning_relic_count);

winning_card_counts = [{}, {}, {}, {}]
winning_relic_counts = [{}, {}, {}, {}]
directory_path = ["IRONCLAD", "THE_SILENT", "DEFECT", "WATCHER"]

for i in range(len(winning_card_counts)) :
    calculate_data(directory_path[i], winning_card_counts[i], winning_relic_counts[i])
    winning_card_counts[i] = dict(sorted(winning_card_counts[i].items(),  key=lambda x: x[1], reverse=True))
    winning_relic_counts[i] = dict(sorted(winning_relic_counts[i].items(), key=lambda x: x[1], reverse=True))
    print(winning_card_counts[i])

winning_relic_count = {}
for key in set(winning_relic_counts[0].keys()).union(winning_relic_counts[1].keys()).union(winning_relic_counts[2].keys()).union(winning_relic_counts[2].keys()):
    winning_relic_count[key] =  winning_relic_counts[0].get(key,0)
    winning_relic_count[key] += winning_relic_counts[1].get(key,0) 
    winning_relic_count[key] += winning_relic_counts[2].get(key,0) 
    winning_relic_count[key] += winning_relic_counts[3].get(key,0)

winning_relic_count = dict(sorted(winning_relic_count.items(), key=lambda x: x[1], reverse=True))
print(winning_relic_count)





