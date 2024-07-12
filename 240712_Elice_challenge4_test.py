"""
N개의 원소, 수열 {a}
부분 수열 2^N개
의 합이 주어진 리스트에서
원래의 수열을 찾아라.

input
3 (= N)
1 4 7 3 0 6 5 2

output
1 2 4
"""

"""
1) N 찾기
2) 정렬 = [0 1 2 3 4 5 6 7]
3) initial = [1]
"""
import math
from itertools import combinations

# N 찾는 함수
def find_N(list):
    length = len(list)
    length = 8
    N = int(math.log2(length))
    return N

# L = [0, 1, 2, 3, 4, 5, 6, 7]
# print(find_N(L))

# 부분집합 합 구하기
def sum_lists(input_list):
    length = len(input_list)
    result = []
    for l in range(length+1):
        temp_list = list(combinations(input_list, l))
        for i in range(len(temp_list)):
            result.append(sum(temp_list[i]))
        # print(temp_list)
        # print(f'result {result}')
    return result
 
test_list = [1, 2, 4]
print(sum_lists(test_list))


#--------------
# print(set([1, 1, 2, 2]) - set([1, 2, 0]))
#--------------

# input
# N = int(input())
# input_list = input().split(' ')
# L = [int(i) for i in input_list]
# print(f'given list is {L}') 

# sorted_L = sorted(L)[1:]
# ini_elem = sorted_L[0]
# ini_list = [ini_elem]
# print(f'The smallest element is {ini_elem}')

# curr_list = ini_list
# sorted_L = sorted_L[1:]
# print(f'The current list is {curr_list}')
# print(f'The sorted list is {sorted_L}')
# if len(curr_list) == N:
#     print("It's over!")
# else :
#     if sorted_L[0] >= sum(curr_list):
#         curr_list.append(sorted_L[0])
#         sorted_L = sorted_L[1:]
#     print(f'The current list is {curr_list}')
#     print(f'The sorted list is {sorted_L}')

    

# 종결코드 : sum(list) == max(input_list)