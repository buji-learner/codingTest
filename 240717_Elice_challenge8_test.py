input_list = input().split(' ')
input_list = '11 3 2 2'.split(' ')
[time_N, prayer_M, friends_K, min_T] = [int(i) for i in input_list]
# print(f'input: {time_N}, prayer_M, friends_K, min_T')



dict = {}
for i in range(time_N):
    dict[i] = 0

# for i in range(prayer_M):
input_duration = '3 12'.split(' ')
[start, end] = [int(i) for i in input_duration]
print(f'duration, {start}, {end}')
for i in range(start, end+1):
    dict[i] += 1
print(dict)