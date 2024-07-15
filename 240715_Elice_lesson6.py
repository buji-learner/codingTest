import sys
import heapq

n = 5
graph = {i: [] for i in range(1, n+1)}
# 오호, dictionary를 이렇게...!
print(f' 1 graph is {graph}')

m = 4
# for _ in range(m):
#     print(_)
#     a, b, c = map(int, input().split())
#     print(a, b, c)
#     # graph[a].append((b, c))

start = 1
priority_queue = [(0, start)]
print(priority_queue)

distances = {vertex: sys.maxsize for vertex in graph}
distances[start] = 0
print(distances)

# while priority_queue:
current_distance, current_vertex = heapq.heappop(priority_queue)

# if current_distance > distances[current_vertex]:
#     continue

for neighbor, weight in graph[current_vertex]:
    distance = current_distance + weight
    
if distance < distances[neighbor]:
    distances[neighbor] = distance
    heapq.heappush(priority_queue, (distance, neighbor))