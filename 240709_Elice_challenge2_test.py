input1 = '8 3'
N, tries = int(input1[0]), int(input1[-1])
# print(f'N is {N}, tries is {tries}') 

input2 = '1 7 6 8 1 6 4 5'
ori_list = [int(i) for i in input2.split(' ')]
# print(f'ori_list is {ori_list}')
ori_tuple = tuple(ori_list)  #
# print(f'ori_tuple is {ori_tuple}')

input3 = '1 5 3'
try_list = [int(i) for i in input3.split(' ')]
# print(f'try_list is {try_list}')

new_list = list(ori_list[try_list[0]-1: try_list[1]])
# print(f'new_list is {new_list}')
sorted_list = sorted(new_list)
print(f'sorted_list is {sorted_list}')

result = sorted_list[try_list[2]-1]
print(f'result is {result}')
