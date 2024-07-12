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
3) initial = [0, 1]
"""
import math

# N 찾는 함수
def find_N(list):
    length = len(list)
    length = 8
    N = int(math.log2(length))
    return N

# L = [0, 1, 2, 3, 4, 5, 6, 7]
# print(find_N(L))


# ------------

# input
N = int(input())
input_list = input().split(' ')
L = [int(i) for i in input_list]
print(f'given list is {L}') 

sorted_L = sorted(L)
ini_2_elem = [sorted_L[0], sorted_L[1]]
print(f'The 2 smallest elements are {ini_2_elem}')