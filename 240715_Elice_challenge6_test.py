from itertools import combinations

N = 5
orders = '1 1 0 1'
orders = [int(i) for i in orders.split(' ')]
"""
N = int(input())
orders = [int(i) for i in input().split(' ')]
# print(N, orders)
"""

#----------------------------
# def make_combi2(list):
#     combi2 = list(combinations(list, 2))

def find_unconnected(dict):
    length = len(dict)
    print(f'The length of dictionary is {length}.')

    result = []

    for i in range(1, length+1):
        print(f'i is {i}')
        for j in range(i, length):
            print(f'j is {j}')
            if dict[i][j] == 0:
                result.append([i, j+1])
                print(result)

find_unconnected({1: [0, 1, 0, 1], 2:[1, 0, 0, 0], 3:[0, 0, 0, 0], 4:[1, 0, 0, 0]})


#----------------------------

graph = {i: [] for i in range(1, N+1)}
# print(f'Initial graph is {graph}')
# ---- {1: [], 2: [], 3: [], 4: [], 5: []}