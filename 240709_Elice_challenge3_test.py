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
# def is_VPS:

def K_repeat(S):
    # S = K(Q)
    # K는 한 자리 수, Q를 K번 반복
    K = int(S[0])
    S_Q = S[2:-1]
    # print(f'{type(K)} K is {K}, {type(S_Q)} Q is {S_Q}')
    # return K * len(S_Q)
    return S_Q * K

S = '3(82)'
S = '34)'
# print(K_repeat(S))

# '(' 만나면 +1, ')' 만나면 -1
stack = 0

length = len(S)
for i in range(length):
    if S[i] == '(': stack += 1
    elif S[i] == ')': stack -= 1

    if stack < 0:
        print('not VPS')
        break
    
