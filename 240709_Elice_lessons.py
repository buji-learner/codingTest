# Sieve of Eratosthenes  에라토스테네스의 체
N = 12

# is_prime 은 bool 자료형 배열
# 처음 디폴트 True
is_prime = []
is_prime = [True for i in range(N)]
is_prime[0] = False

for i in range(2, N):
    if is_prime[i]:
        print(f'i is {i}')
        for j in range(i*2, N, i):
            print(f'j is {j}', is_prime[j])
            if is_prime[j]: is_prime[j] = False
            print('and now', is_prime[j])

print(is_prime)