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
            return False, list_S
    if sum(list_S) != 0:
        return False, list_S
    
    return True, list_S
# print(is_VPS('13(42(7))8'))
# print(is_VPS('13((42(7))8'))
# print(is_VPS('13())42(78'))

        
# S = K(Q)
# K는 한 자리 수, Q를 K번 반복
def K_repeat(S):
    K = int(S[0])
    S_Q = S[2:-1]

    # return K * len(S_Q)
    return S_Q * K
# print(K_repeat('3(8)'))


# 가장 큰  단위의 () 추출
# 반환값은 첫번째 ( 인덱스, 마지막 ) 인덱스, 숫자로 표현된 input_S 
def extract_bracket(S):
    length = len(S)
    list_S = []
    idx_open = []
    idx_close = []
    
    for i in range(length):
        if S[i] == '(': 
            idx_open.append(i)
        elif S[i] == ')':
            idx_close.append(i)
            bracket_S = S[max(idx_open)-1:max(idx_close)+1]
            new_S = S.replace(bracket_S, K_repeat(bracket_S))
            return new_S
        else : list_S.append(0)

        if sum(list_S) < 0:
            print(f"{S} is not VPS.")
            break

    return ''

#-----------------------------
# S = '13(42(7))8'
S = input()

while True:
    result = S
    S = extract_bracket(S)

    if len(S) == 0:
        break

print(result)