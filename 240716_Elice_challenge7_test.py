# list = [7, 8]
# K = 4
def meetK(list, K):
    for i in range(10):
        # print(f'i is {i}')
        if len(list) == K:
            break
        if i not in list:
            list.append(i)
    # print(list)
    return list
# print(meetK(list, K))

def smallestNum1(list):
    sorted_list = sorted(list)
    length = len(list)

    result = 0
    while True:

        # base
        if len(sorted_list) < 1:
            print('break')
            break

        # initial
        if result == 0 and sorted_list[0] == 0:
            result += sorted_list[1]
            sorted_list.pop(1)
        
        result = result * 10 + sorted_list[0]
        sorted_list.pop(0)
        # print(f'sorted_list {sorted_list}, result {result}')
        
    return result

# print(smallestNum(list))

def smallestNum0(list):
    sorted_list = sorted(list)
    length = len(list)

    result = 0
    while True:

        # base
        if len(sorted_list) < 1:
            print('break')
            break
        
        result = result * 10 + sorted_list[0]
        sorted_list.pop(0)
        # print(f'sorted_list {sorted_list}, result {result}')
        
    return result

#-------------------------
N = '10'
K = 3
int_N = int(N)
set_N = [0, 1]

numbers = meetK(set_N, K)
print(f'numbers {numbers}')
print(f'smallest {smallestNum1(numbers)}')

if int_N > smallestNum1(numbers):
    numbers.remove(1)
    print(int_N + smallestNum0(numbers))
else: print(smallestNum1(numbers))