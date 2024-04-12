import json
import os

# directory_path = "DEFECT"
# directory_path = "THE_SILENT"

# List all files in the directory
directory_path = ["IRONCLAD", "THE_SILENT", "DEFECT", "WATCHER"]

def sort_dict(dic) :
    sorted_dic = dict(sorted(dic.items(),  key=lambda x: x[1], reverse=True))
    dic.clear()
    dic.update(sorted_dic)
    # print("SORT", dic)

def combine_dict(dict, dicts) :
    
    for key in set(dicts[0].keys()).union(dicts[1].keys()).union(dicts[2].keys()).union(dicts[2].keys()):
        dict[key] =  dicts[0].get(key,0)
        dict[key] += dicts[1].get(key,0) 
        dict[key] += dicts[2].get(key,0) 
        dict[key] += dicts[3].get(key,0)

def print_dict(dict) :
    for key, value in dict.items():
        print(f"{key}: {value}")
    print()

def delete_file(relative_path):
    try:
        os.remove(relative_path)
        print(f"File {relative_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting file {relative_path}: {e}")

def isHeartRun(data) :
    return data['damage_taken'][-1]['enemies'] == 'The Heart'

def isAscension20(data) :
    return data['ascension_level'] == 20

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

total_run = 0
total_win = 0
def filter_data(directory_path) :
    run, loss, win = 0, 0, 0
    files = os.listdir(directory_path) 
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        # print(file_path)
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            global total_win, total_run
            # if data['chose_seed']:
            #     delete_file(file_path)
            # if not isAscension20(data):
            #     delete_file(file_path)
            # if cnt == 0:
            #     delete_file(file_path)
            loss += 1
            run += 1
            total_run += 1
            if data['victory'] :
                win += 1
                total_win += 1
                print(directory_path, 'victory no', win)
                print('number of losses', loss-1)
                print('win rate',  str(win/run*100)+ "%")
                print()
                loss = 0
            # if cnt == 6 :
                # delete_file(file_path)
                
                
def calculate_data(directory_path, winning_card_count, winning_relic_count, killer_count, damage_taken) :
    files = os.listdir(directory_path)
    
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'r') as file:
            
            data = json.load(file)
            if data['victory'] :
                calculate_card_count(data, winning_card_count);
                calculate_relic_count(data, winning_relic_count);
            
            if(data.get('killed_by') is not None) :
                str = data['killed_by']
                if(killer_count.get(str) is None) :
                    killer_count[str] = 0
                killer_count[str] = killer_count[str] + 1
            
            for item in data['damage_taken'] :
                enemies = item['enemies']
                damage = item['damage']
                if(damage_taken.get(enemies) is None) :
                    damage_taken[enemies] = 0
                damage_taken[enemies] += damage

for i in range(4):
    filter_data(directory_path[i])

winning_card_counts = [{}, {}, {}, {}]
winning_relic_counts = [{}, {}, {}, {}]
killer_counts = [{}, {}, {}, {}]
damage_takens = [{}, {}, {}, {}]
print(total_win, total_run, str(total_win*100/total_run) + "%", '\n');

for i in range(len(winning_card_counts)) :
    calculate_data(directory_path[i], winning_card_counts[i], winning_relic_counts[i], killer_counts[i], damage_takens[i])
    sort_dict(winning_card_counts[i])
    sort_dict(winning_relic_counts[i])
    sort_dict(killer_counts[i])
    sort_dict(damage_takens[i])
    
    print_dict(winning_card_counts[i])
    print_dict(killer_counts[i])
    print_dict(damage_takens[i])

winning_relic_count = {}
combine_dict(winning_relic_count, winning_relic_counts)
sort_dict(winning_relic_count)

killer_count = {}
combine_dict(killer_count, killer_counts)
sort_dict(killer_count)

damage_taken = {}
combine_dict(damage_taken, damage_takens)
sort_dict(damage_taken)

print_dict(winning_relic_count)
print_dict(killer_count)
print_dict(damage_taken)






