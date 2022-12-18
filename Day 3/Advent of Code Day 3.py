import string
import pandas
import pickle
import pandas as pd

def create_priority_index():
    ascii_alphabet = list(string.ascii_letters)
    priority_index = {}
    priority = 1
    for letter in ascii_alphabet:
        priority_index.update({letter : priority})
        priority += 1
    return priority_index


#Used Priority Index as Parameter to Increase Efficancy 
def prioritize_letters(string, priority_index):
    return [priority_index[s] for s in string]





file = pickle.load(open('elf_rugsacks.p', 'rb'))
data = file.split('\n')
priority_index = create_priority_index()
df = {'c_1' : [], 'c_2' : []}
for value in data:
    value = prioritize_letters(value, priority_index)
    half_point = int(len(value) / 2)
    df['c_1'].append(value[:half_point])
    df['c_2'].append(value[half_point:])

    
df = pd.DataFrame(df)
df['duplicate_value'] = df.reset_index()['index'].apply(lambda x: list(set(df['c_1'][x]) & set(df['c_2'][x]))[0])
print('Total Sum of Duplicate Items Priority: ' + str(df['duplicate_value'].sum()))


#Part 2
df = {'elf_1' : [], 'elf_2' : [], 'elf_3' : []}
iteration = 0
while True:
    if iteration >= len(data):
        break
    df['elf_1'].append(prioritize_letters(data[iteration], priority_index))
    df['elf_2'].append(prioritize_letters(data[iteration + 1], priority_index))
    df['elf_3'].append(prioritize_letters(data[iteration + 2], priority_index))
    iteration += 3

    
df = pd.DataFrame(df)
df['elf_1'].apply(lambda x: prioritize_letters(x))



df['duplicate_value'] = df.reset_index()['index'].apply(lambda x: list(set(df['elf_1'][x]) & set(df['elf_2'][x]) & set(df['elf_3'][x]))[0])
print('Total Sum of Duplicate Items Priority: ' + str(df['duplicate_value'].sum()))




