""" question

{1 7 6 8 1 6 4 5}
input : 1 5 3
1st ~ 5th >>> {1 7 6 8 1} 
sorted >>> {1 1 6 7 8}
3th num >>> 6

"""

""" input EX
8 3
1 7 6 8 1 6 4 5
1 5 3
2 6 2
4 8 3
"""

""" output
6
6
5
"""

#### 함수 정의


#### ---------

# 첫번째 input: 
# 배열 크기(N), 일하는 횟수(tries)
print('Input for length of array(N) and number of tries(tries)')
input1 = input().split(' ')    # input1 = input()
N, tries = int(input1[0]), int(input1[-1])

# 두번째 input:
# 랜덤 배열
print('Input random array')
input2 = input()
ori_list = [int(i) for i in input2.split(' ')]
# print(f'ori_list is {ori_list}')
ori_tuple = tuple(ori_list)  #
# print(f'ori_tuple is {ori_tuple}')

# input 일하기
for i in range(tries):
    print(f'input try{i+1} numbers :start end k')
    input_try = input()
    try_list = [int(i) for i in input_try.split(' ')]

    new_list = list(ori_list[try_list[0]-1: try_list[1]])
    # print(f'new_list is {new_list}')
    sorted_list = sorted(new_list)
    # print(f'sorted_list is {sorted_list}')

    result = sorted_list[try_list[2]-1]
    print(result)