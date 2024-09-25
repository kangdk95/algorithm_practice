import math

# 소수 판별 
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True 

print(is_prime_number(1)) 
print(is_prime_number(8)) 