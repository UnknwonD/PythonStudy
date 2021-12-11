print(abs(-5))  # 절댓값 반환   
print(pow(4, 2)) #4의 2제곱을 반환
print(max(5, 12)) #최댓값 반환
print(min(5, 12)) #최솟값 반환
print(round(3.13)) #반올림한 숫자를 반환함

from math import *

print(floor(4.99)) #내림값을 반환
print(ceil(3.14)) #올림값을 반환
print(sqrt(16)) # 제곱근을 반환함

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성함
print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값을 생성 소수점 숫자를 없앰 
print(randrange(1, 46)) # 1~45 까지의, 46 미만의 숫자를 생성함 
print(randint(1, 45)) # 양 끝을 모두 포함한 범위 내의 숫자를 생성 ( 1~ 45 )
