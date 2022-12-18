import pandas as pd
import pickle



def number_range(value):
    value = value.split('-')
    return [num for num in range(int(value[0]), int(value[1]) + 1)]


def is_subset(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    if l1.issubset(l2):
        return 1
    if l2.issubset(l1):
        return 1
    return 0



file = pickle.load(open('elf_assignments.p', 'rb'))
data = file.split('\n')

df = {'elf_1' : [], 'elf_2' : []}

for value in data:
    value = value.split(',')
    df['elf_1'].append(number_range(value[0]))
    df['elf_2'].append(number_range(value[1]))



df = pd.DataFrame(df)
df = df.reset_index()

df['subset_check'] = df['index'].apply(lambda x: is_subset(df['elf_1'][x], df['elf_2'][x]))

print('Total Subset Assignments Amoung Pairs : ' + str(df['subset_check'].sum()))


#Part 2

df['similarity_check'] = df['index'].apply(lambda x: 1 if len(set(df['elf_1'][x]) & set(df['elf_2'][x])) >= 1 else 0)
print('Total Assignments Overlapping Amoung Pairs : ' + str(df['similarity_check'].sum()))
