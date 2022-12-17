import pickle


data = pickle.load(open('elf_food.p', 'rb'))
data = data.split('\n')
master_list = []
static_list = []
for value in data:
    if value == '':
        master_list.append(sum(static_list))
        static_list = []
        continue
    static_list.append(int(value))

    
print('Maximum Calories Carried by any Elf: ' + str(max(master_list)))


#Part 2
master_list.sort()
print('Calories Carried by Top 3 Elves: ' + str(sum(master_list[::-1][:3])))
