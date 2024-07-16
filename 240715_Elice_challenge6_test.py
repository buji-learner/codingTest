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
    # print(f'The length of dictionary is {length}.')

    result = []

    # 시간 복잡도 해결하기!
    for i in range(1, length+1):
        # print(f'i is {i}')
        for j in range(i, length):
            # print(f'j is {j}')
            if dict[i][j] == 1:
                result.append([i, j+1])
                # print(result)
    
    return result

def select_connected(N):
    graph = {i: [] for i in range(1, N+1)}
    for i in range(i, N):
        


# 1, 2
def make_connected(graph, i, j):
    graph[i][j-1] = 0
    graph[j][i-1] = 0
    # print(f'Trial 1 graph is {graph}')
    return graph

# find_unconnected({1: [0, 1, 0, 1], 2:[1, 0, 0, 0], 3:[0, 0, 0, 0], 4:[1, 0, 0, 0]})


#----------------------------

# 연결된 것 0, 연결 안된 것 1
graph = {i: [0 if i-1==j else 1 for j in range(N)] for i in range(1, N+1)}
print(f'Initial graph is {graph}')
# ---- {1: [0, 0, 0, 0, 0], 2: [], 3: [], 4: [], 5: []}

# trial 1
# graph[1][1] = 1
# graph[1+1][1-1] = 1
# print(f'Trial 1 graph is {graph}')
# >>>
graph = make_connected(graph, 1, 4)


# for i in range(len(orders)):    