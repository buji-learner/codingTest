# list = [0, 1]
# K = 4
# def meetK(list, K):
#     if len(list) > K:
#         return [i for i in range(K)]

    # for i in range(10):
    #     # print(f'i is {i}')
    #     if len(list) == K:
    #         break
    #     if i not in list:
    #         list.append(i)
    # return list


def smallestNum1(list):
    sorted_list = sorted(list)
    length = len(list)

    result = 0
    while True:
        # base
        if len(sorted_list) < 1:
            # print('break')
            break

        # initial
        if result == 0 and sorted_list[0] == 0:
            result += sorted_list[1]
            sorted_list.pop(1)
        
        result = result * 10 + sorted_list[0]
        sorted_list.pop(0)
  
    return result


def smallestNum0(list):
    sorted_list = sorted(list)
    length = len(list)

    result = 0
    while True:
        # base
        if len(sorted_list) < 1:
            # print('break')
            break
        
        result = result * 10 + sorted_list[0]
        sorted_list.pop(0)
        
    return result

# --------------
N, K = input().split(' ')
# print(N, K)

list_N = [int(N[i]) for i in range(len(N))]
sorted_list = sorted(list_N)햐
# print(set_N)
int_N, K = int(N), int(K)

numbers = [i for i in range(K)]
# print(f'numbers {numbers}')
# print(f'smallest1 {smallestNum1(numbers)}')

if int_N > smallestNum1(numbers):
    # numbers.remove(sorted_list[1])
    # print(int_N + smallestNum0(numbers))
    print(pow(10, (len(N))) + smallestNum0(numbers[2:]))
else: print(smallestNum1(numbers))