import pandas as pd
import pickle





def move_boxes(box_stacks, quantity, starting_stack, ending_stack, part_1 = True):
    crane_list = box_stacks[starting_stack][len(box_stacks[starting_stack]) - quantity::]
    del box_stacks[starting_stack][len(box_stacks[starting_stack]) - quantity::]
    if part_1:
        crane_list.reverse() #Remove This Line and Run Again for Part 2
    box_stacks[ending_stack] = box_stacks[ending_stack] + crane_list
    return box_stacks
    


def format_command(value):
    blacklist = ['move', 'from', 'to']
    value = value.split(' ')
    value = [int(v) for v in value if v not in blacklist]
    return value


box_stacks = {
    1 : ['T', 'D', 'W', 'Z', 'V', 'P'],
    2 : ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    3 : ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    4 : ['R', 'S', 'J'],
    5 : ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    6 : ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    7 : ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    8 : ['P', 'T', 'B', 'Q'],
    9 : ['H', 'G', 'Z', 'R', 'C']
    }



file = pickle.load(open('crane_commands.p', 'rb'))
data = file.split('\n')
command_list = [format_command(value) for value in data]
for command in command_list:
    box_stacks = move_boxes(box_stacks, command[0], command[1], command[2])


final_string = ''
for stack in box_stacks.keys():
    try:
        final_string += box_stacks[stack][len(box_stacks[stack]) - 1]
    except:
        continue


print('Final String of Boxes at Top of Stacks: ' + final_string)



#Part 2

box_stacks = {
    1 : ['T', 'D', 'W', 'Z', 'V', 'P'],
    2 : ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    3 : ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    4 : ['R', 'S', 'J'],
    5 : ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    6 : ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    7 : ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    8 : ['P', 'T', 'B', 'Q'],
    9 : ['H', 'G', 'Z', 'R', 'C']
    }


file = pickle.load(open('crane_commands.p', 'rb'))
data = file.split('\n')
command_list = [format_command(value) for value in data]
for command in command_list:
    box_stacks = move_boxes(box_stacks, command[0], command[1], command[2], part_1 = False)


final_string = ''
for stack in box_stacks.keys():
    try:
        final_string += box_stacks[stack][len(box_stacks[stack]) - 1]
    except:
        continue


print('Final String of Boxes at Top of Stacks: ' + final_string)

