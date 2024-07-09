def toList(test):
    numList = []
    while test != 0:
        numList.insert(0, test%10)
        test = int(test//10)
        # print(numList,test)
    return numList

def biggest(list):
    # print(len([1, 2, 3]))   
    length = int(len(list))
    # print('length of sorted: ', length)
    biggest = 0
    for i in range(length):
        # print(list[i], pow(10,(i)))
        biggest += list[i]*pow(10,(i))

    print (f'biggest number with {list} is {biggest}')
    return biggest

def smallest(list):
    # print(len([1, 2, 3]))   
    length = int(len(list))
    print('length of sorted: ', length)
    smallest = 0
    for i in range(length):
        print(list[i], pow(10,(length-i-1)))
        smallest += list[i]*pow(10,(length-i-1))

    print (f'smallest number with {list} is {smallest}')
    return smallest

# --------------

input_num = 346

original_list = toList(input_num)
sorted_list = sorted(original_list)
print(f'original is {original_list}, sorted is {sorted_list}')  # original is [3, 6, 4], sorted is [3, 4, 6]
length = len(original_list)

#### 이걸 함수A로 만들면
test_num = input_num%pow(10, length-1)  # 64
# print(test_num)

print(f'to test {sorted(toList(test_num))}')  # to test [4, 6]

if test_num == biggest(sorted(toList(test_num))):  # biggest number with [4, 6] is 64
    print('Yes!')
    idx = sorted_list.index(original_list[0])
    print(f'{idx}, the first num would be {sorted_list[idx+1]}')

    result = sorted_list[idx+1] * pow(10,length-1)

    del sorted_list[idx+1]
    
    result += smallest(sorted_list)
    print(result)

else :
    print('No!')
    length -= 1
    original_list = original_list[1:]
    sorted_list = sorted(original_list)
    print(f'new original is {original_list}, new sorted is {sorted_list}') 
    
    test_num = test_num%pow(10, length-1)
    print(f'test number 2 : {test_num} to test {sorted(toList(test_num))}') 
    if test_num == biggest(sorted(toList(test_num))): 
        print('Yes!')
        idx = sorted_list.index(original_list[0])
        print(f'{idx}, the first num would be {sorted_list[idx+1]}')

        result = sorted_list[idx+1] * pow(10,length-1)

        del sorted_list[idx+1]
    
        result += smallest(sorted_list)
        print(result)
    
    else :
        print('No!')
        length -= 1
        original_list = original_list[1:]
        sorted_list = sorted(original_list)
        print(f'new original is {original_list}, new sorted is {sorted_list}') 
        test_num = test_num%pow(10, length-1)
        print(f'test number 2 : {test_num} to test {sorted(toList(test_num))}') 
        if test_num == biggest(sorted(toList(test_num))): 
            print('Yes!')
            idx = sorted_list.index(original_list[0])
            print(f'{idx}, the first num would be {sorted_list[idx+1]}')

            result = sorted_list[idx+1] * pow(10,length-1)

            del sorted_list[idx+1]
        
            result += smallest(sorted_list)
            print(result)
    