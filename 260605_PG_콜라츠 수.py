"""
1937년 Collatz란 사람에 의해 제기된 이 추측은, 
어진 수가 1이 될 때까지 다음 작업을 반복하면,
모든 수를 1로 만들 수 있다는 추측입니다.
작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

"""

num1 = 16
num2 = 626331    # -1
num3 = 1

def OddOrEven (num):
    # If the num is even, return True.
    # Otherwise, return False
    if num%2 == 0:
        return True
    return False

# print(OddOrEven(num1+1))

""" 1차 시도 While Loop

num_test = num2
count = 0
while (num_test > 1):
    print(f'This is {count}th start')
    if count >= 10:
        print('-1')
        break

    if OddOrEven(num_test) == True:
        print("It is Even.")
        num_test = int(num_test/2)
    elif OddOrEven(num_test) == False:
        print("It is Odd.")
        num_test = 3*num_test +1

    print(f'This is {count}th end. Current num_test is {num_test}.')
    count += 1

print('Result:', count)
"""

""" 2차시도 회귀 함수
"""
num_test = 1
count = 0

def Loop(num_test, count):
    print(f'This is {count}th start')
    if num_test == 1:
        return count
    if count >= 10:
        print('-1')
        return -1
    

    if OddOrEven(num_test) == True:
        print("It is Even.")
        num_test = int(num_test/2)
    elif OddOrEven(num_test) == False:
        print("It is Odd.")
        num_test = 3*num_test +1

    print(f'This is {count}th end. Current num_test is {num_test}.')
    count += 1

    return Loop(num_test, count)

Loop(num_test, count)
print(Loop(num_test, count))