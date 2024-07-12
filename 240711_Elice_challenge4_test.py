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
def make_dictionary(N):
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

def winner(list):
    if list[0] >= list[1]:
        return 1
    return 0

#-------------------------
N = int(input())
dictionary = make_dictionary(N)
# print(f'dictionary is {dictionary}')

for i in range(1,N+1):
    initial = i
    turns = 1
    former, later = i, 0
    print(f'try {i} : [{former}, {later}]')
    # print(dictionary[i])

    while len(dictionary[i]) > 0:
        print(f'turns : {turns}')
        M = max(dictionary[i])
        if turns%2 == 0: former += M
        else : later += M
        # print(f'test before {dictionary[i]}')
        # dictionary[i].remove(M)
        # print(f'test after {dictionary[i]}')
        if M == initial:
            break
        i = M
        turns += 1

    print(f'The result is {[former, later]}')
    print(winner([former, later]))

""" dictionary test
dictionary = {1:[1, 2, 3], 2:[4, 5]}
print(dictionary)
print(dictionary[2])
print(len(dictionary[2]))
"""

# node 1에서 출발
# i = 1
# former, later = 0, 0
# former += i
# print(f'try1 {former}, {later}')

# if len(dictionary[i]) > 0:
#     M = max(dictionary[i])
#     later += M
#     i = M
#     print(f'try1 {former}, {later}')
    
# if len(dictionary[i]) > 0:
#     M = max(dictionary[i])
#     former += M
#     i = M
#     print(f'try1 {former}, {later}')
# else : print('No more turns')
