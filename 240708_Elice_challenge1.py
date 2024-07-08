#### 함수 정의
# 정수 >>> list로 변환
def toList(test):
    numList = []
    while test != 0:
        numList.insert(0, test%10)
        test = int(test//10)

    return numList

# sorted _ list를 구성하는 숫자로 가장 큰 수
def biggest(sorted_list):
    length = int(len(sorted_list))
    biggest = 0
    for i in range(length):
        biggest += sorted_list[i]*pow(10,(i))

    return biggest

# sorted _ list를 구성하는 숫자로 가장 작은 수
def smallest(list):
    length = int(len(list))
    smallest = 0
    for i in range(length):
        smallest += list[i]*pow(10,(length-i-1))

    return smallest

def yes_biggest(sorted_list, original_list):
    length = len(original_list)
    idx = sorted_list.index(original_list[0])

    for i in range(length-idx):
        if sorted_list[idx+i] > sorted_list[idx]:
            first_num = sorted_list[idx+i]

    result = first_num * pow(10,length-1)

    sorted_list.remove(first_num)
    
    result += smallest(sorted_list)
    return result

# 해당 자릿 수 아래 숫자가 가장 큰 수 인지 확인
def check_biggest(test_num, original_list, sorted_list):
    length = len(original_list)
    if test_num == biggest(sorted(toList(test_num))):  
        print('Yes!')
        return yes_biggest(sorted_list, original_list)
    else :
        first_num = original_list[0] * pow(10,length-1)
        print("No-")
        length -= 1
        test_num = input_num%pow(10, length-1)
        original_list = original_list[1:]
        sorted_list = sorted(original_list)

        return first_num + check_biggest(test_num, original_list, sorted_list)

#### --------------------------------------------------

input_num = 1234

original_list = toList(input_num)
sorted_list = sorted(original_list)

# 이미 가장 큰 수 인 경우
if input_num == biggest(sorted_list):
    print('There would be no answer. You already solved as much as you can!')

else :

    length = len(original_list)
    test_num = input_num%pow(10, length-1)  

    result = 0
    result = check_biggest(test_num, original_list, sorted_list)

    print(result)