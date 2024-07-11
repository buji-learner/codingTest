# 트리 게임
"""
input
5
1 3
2 1
3 4
5 1

output
1
1
0
1
1
"""

#### 함수
#
def make_dictionary():
    N = int(input())
    dictionary = {}
    for i in range(N):
        dictionary[i+1] = []
    # print(f'initial dictionary {dictionary}')

    for i in range(N-1):
        input_list = input().split(' ')
        # print(f'input_list is {input_list}')
        input1, input2 = int(input_list[0]), int(input_list[1])
        # print(f'inputs are {input1}, {input2}')

        dictionary[input1].append(input2)
    # print(f'result of dictionary is {dictionary}')
    return dictionary

make_dictionary()


