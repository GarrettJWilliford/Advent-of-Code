import pandas as pd
import pickle

mapping_dict = {'Elf' : {'A' : 1, 'B' : 2, 'C' : 3},
'User' : {'X' : 1, 'Y' : 2, 'Z' : 3}}


rps_json = {1 : {3 : 6, 2 : 0, 1 : 3},
 3 : {2 : 6, 1 : 0, 3 : 3},
 2 : {1 : 6, 3 : 0, 2 : 3}}


file = pickle.load(open('rps_data.p', 'rb'))
raw_data = file.split('\n')
data = {'elf_input' : [], 'user_input' : []}
for value in raw_data:
    data['elf_input'].append(value[0])
    data['user_input'].append(value[2])


data = pd.DataFrame(data)
data['elf_input'] = data['elf_input'].apply(lambda x: mapping_dict['Elf'][x])
data['user_raw_input'] = data['user_input'] #Used for Part 2
data['user_input'] = data['user_input'].apply(lambda x: mapping_dict['User'][x])


data['outcome'] = data.reset_index()['index'].apply(lambda x: data['user_input'][x] + rps_json[data['user_input'][x]][data['elf_input'][x]])

    
    
print('Final RPS Score: ' + str(data['outcome'].sum()))


#Part 2
outcome_map = {'X' : {1 : 3, 2 : 1, 3 : 2},
               'Y' : {1 : 1, 2 : 2, 3 : 3},
               'Z' : {1 : 2, 2 : 3, 3 : 1}}

data = data[['elf_input', 'user_raw_input']]

data['user_input'] = data.reset_index()['index'].apply(lambda x: outcome_map[data['user_raw_input'][x]][data['elf_input'][x]])
data = data.drop(columns = ['user_raw_input'])

data['outcome'] = data.reset_index()['index'].apply(lambda x: data['user_input'][x] + rps_json[data['user_input'][x]][data['elf_input'][x]])

print('Final RPS Score: ' + str(data['outcome'].sum()))
