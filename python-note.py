import sys
from math import *

# 길이가 10인 list 만들기
arr = list(range(0, 10))
print('길이가 10인 list:', arr)

# ------------------------------------------------------------------------

# 템플릿 리터럴
a, b = 1234, 5678
print(f'템플릿 리터럴: {str(a) + str(b)}')

# ------------------------------------------------------------------------

# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
map_test = list(map(int, ['1', '2', '3', '42']))
print('map: ', map_test)

# ------------------------------------------------------------------------

# 지정된 정수 인자의 최대 공약수를 반환합니다. 
print('gcd: ',gcd(12, 39)) # === 3

# ------------------------------------------------------------------------

# 음이 아닌 정수 n의 정수 제곱근을 반환합니다.
print('isqrt: ',isqrt(121)) # === 11

# ------------------------------------------------------------------------

# 공간 복잡도 신경 쓰기: int(N ** 0.5)
# 시간 복잡도 신경 쓰기: math.isqrt(N)

# ------------------------------------------------------------------------

# 약수 구하기
def getDivisonNums(num):
    check_divison_nums = []
    
    for i in range(1, isqrt(num) + 1):
        if ((num % i) == 0):
            check_divison_nums.append(i)
            if ((i**2) != num):
                check_divison_nums.append(num // i)
    check_divison_nums.sort()     
    return check_divison_nums
print('약수 구하기: ', getDivisonNums(100))

# ------------------------------------------------------------------------

# 소수인지 아닌지 판별하는 로직
def divisorCheck(num):
    for i in range(2, isqrt(num)+1):
        if(num % i) == 0 | i == 1: 
            return 
    return True
print('소수인가?', divisorCheck(100))

# ------------------------------------------------------------------------

# 소인수분해 함수
def factorization(x):
    d = 2
    basket = [1]
    while d <= x:
        if x % d == 0: 
            x = x // d
            basket.append(d)
        else:
            d = d + 1
    return basket
print('소인수 분해된 것들:',factorization(18))

# ------------------------------------------------------------------------

# 위 코드는 x[0]을 우선순위로 정렬하는 것이다.
# sort(key = lambda x : [x[0], x[1]]) 
# 위 코드는 x[0]을 우선 순위로 정렬하고, x[0]이 같으면 x[1]을 확인한다.
# 더 작은 수부터 큰 수로 정렬한다.
sort_test_1 = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
sort_test_1.sort(key = lambda x : x[0])
sort_test_2 = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
sort_test_2.sort(key = lambda x : x[0])
print('key lambda를 이용한 sort: ',sort_test_1)

# ------------------------------------------------------------------------

# for cur_route in routes:
# vs
# for cur_route in range(len(routes)):
# 둘의 차이점은?