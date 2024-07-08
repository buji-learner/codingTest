#### 함수 정의
# 정수 >>> list로 변환
def toList(test):
    numList = []
    while test != 0:
        numList.insert(0, test%10)
        test = int(test//10)
        # print(numList,test)
    return numList

# sorted _ list를 구성하는 숫자로 가장 큰 수
def biggest(sorted_list):
    # print(len([1, 2, 3]))   
    length = int(len(sorted_list))
    # print('length of sorted: ', length)
    biggest = 0
    for i in range(length):
        # print(sorted_list[i], pow(10,(i)))
        biggest += sorted_list[i]*pow(10,(i))

    print (f'biggest number with {sorted_list} is {biggest}')
    return biggest

# sorted _ list를 구성하는 숫자로 가장 작은 수
def smallest(list):
    # print(len([1, 2, 3]))   
    length = int(len(list))
    # print('length of sorted: ', length)
    smallest = 0
    for i in range(length):
        # print(list[i], pow(10,(length-i-1)))
        smallest += list[i]*pow(10,(length-i-1))

    print (f'smallest number with {list} is {smallest}')
    return smallest

def yes_biggest(sorted_list, original_list):
    length = len(original_list)

    idx = sorted_list.index(original_list[0])
    print(f'{idx}, the first num would be {sorted_list[idx+1]}')

    result = sorted_list[idx+1] * pow(10,length-1)

    del sorted_list[idx+1]
    
    result += smallest(sorted_list)
    return result

# 해당 자릿 수 아래 숫자가 가장 큰 수 인지 확인
# def check_biggest(input_num, original_list, sorted_list):
#     length = len(original_list)
#     test_num = input_num%pow(10, length-1)  # 64

#     print(f'to test {sorted(toList(test_num))}')  # to test [4, 6]
def check_biggest(test_num, original_list, sorted_list):
    length = len(original_list)
    if test_num == biggest(sorted(toList(test_num))):  # biggest number with [4, 6] is 64
        print('Yes!')
        return yes_biggest(sorted_list, original_list)
    else :
        # test_num = test_num%pow(10, length-1)
        first_num = original_list[0] * pow(10,length-1)
        print("No-")
        length -= 1
        test_num = input_num%pow(10, length-1)
        original_list = original_list[1:]
        sorted_list = sorted(original_list)
        print(f'new original is {original_list}, new sorted is {sorted_list}') 
        return first_num + check_biggest(test_num, original_list, sorted_list)

#### --------------------------------------------------

input_num = 4151

original_list = toList(input_num)
sorted_list = sorted(original_list)
print(f'original is {original_list}, sorted is {sorted_list}') 

length = len(original_list)
test_num = input_num%pow(10, length-1)  

print(f'test number 1 : {test_num} to test {sorted(toList(test_num))}')  

result = 0
result = check_biggest(test_num, original_list, sorted_list)


print(result)