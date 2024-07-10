"""
K(Q) : Q 문자열이 K번 반복, K는 한 자리 정수


input_S = 53(8)    # input_S 길이 <= 50

5+3(8) = 5 + 888 = 5888

output 4 (문자열 길이)
"""
""" EX
S = 11(18(72(7)))

72(7) = 7 + 2(7) = 777
S = 11(18(777))

18(777) = 1 + 8(777) = 25자리 수
S = 11(25자리 수) = 1 + 1(25자리 수)

output 26
"""

#### 함수
# 문자열 유효한지 확인
def is_VPS(S):
    length = len(S)
    list_S = []
    for i in range(length):
        if S[i] == '(': list_S.append(1)
        elif S[i] == ')': list_S.append(-1)
        else : list_S.append(0)

        if sum(list_S) < 0:
            return False
    if sum(list_S) != 0:
        return False
    return True
# print('test is_VPS')
# print(is_VPS('456())(145'))
# print('------------')

# K(Q) >>> Q를 K번 반복하는 문자열로 반환
def K_repeat(S):
    # S = K(Q)
    # K는 한 자리 수, Q를 K번 반복
    K = int(S[0])
    S_Q = S[2:-1]
    # print(f'{type(K)} K is {K}, {type(S_Q)} Q is {S_Q}')
    # return K * len(S_Q)
    return S_Q * K

# 가장 큰  단위의 () 추출
# 반환값은 첫번째 ( 인덱스, 마지막 ) 인덱스, 숫자로 표현된 input_S 
def extract_bracket(S):
    length = len(S)

    list_S = []
    idx_open = []
    idx_close = []
    for i in range(length):
        if S[i] == '(': 
            list_S.append(1)
            idx_open.append(i)
        elif S[i] == ')': 
            list_S.append(-1)
            idx_close.append(i)
            bracket_S = S[max(idx_open)-1:max(idx_close)+1]
            K = bracket_S[0] # str
            Q = bracket_S[2: len(bracket_S)-1]
            print(f'{bracket_S}, K is {K}, Q is {Q}')
            return S.replace(bracket_S, Q*int(K))

        else : list_S.append(0)

        if sum(list_S) < 0:
            print(f"{S} is not VPS.")
            break
        # if len(idx_open) > 0 and sum(list_S) == 0:
        #     print('here!')
        #     bracket_S = S[min(idx_open)-1:max(idx_close)+1]
        #     K = bracket_S[0] # str
        #     Q = bracket_S[2: len(bracket_S)-1]
        #     print(f'{bracket_S}, K is {K}, Q is {Q}')
        #     return S.replace(bracket_S, Q*int(K))

    # if sum(list_S) != 0:
    #     print(f"----{S} is not VPS.----")

    # print(f'list_S is {list_S}')
    # print(f'location of open/close bracket {idx_open}, {idx_close}')
    # return min(idx_open), max(idx_close), list_S
# S = '3(82)' 
# extract_bracket(S)

####------------------

S = '13(42(7))8'

new_S = extract_bracket(S)
print(f'second is {new_S}')
new_S = extract_bracket(new_S)
print(f'third is {new_S}')



# idx_open = extract_bracket(S)[0]
# idx_close = extract_bracket(S)[1]
# new_S = S[idx_open+1:idx_close]
# print(f'second S is {new_S}')
# idx_open = extract_bracket(new_S)[0]
# idx_close = extract_bracket(new_S)[1]
# new_S = new_S[idx_open+1:idx_close]
# print(f'third S is {new_S}')




""" 함수 extract_bracket으로 필요없어짐
# '(' 만나면 +1, ')' 만나면 -1
stack = 0

length = len(S)
for i in range(length):
    if S[i] == '(': stack += 1
    elif S[i] == ')': stack -= 1

    if stack < 0:
        print('not VPS')
        break
"""
    