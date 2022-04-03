# 랜덤함수
from random import *

print(random())  # 0.0(이상) ~ 1.0(미만) 사이의 임의의 값 생성
print(random() * 10)  # 0.0(이상) ~ 10.0(미만) 사이의 값 생성
print(int(random() * 10))  # 0(이상) ~ 10(미만) 사이의 값 생성
print(int(random() * 10) + 1)  # 1(이상) ~ 10(이하) 사이의 값 생성

print(int(random() * 45) + 1)  # 1(이상) ~ 45(이하) 의 값 생성

print(randrange(1, 46))  # 1(이상) ~ 46(미만)

print(randint(1, 45))  # 1(이상) ~ 45(이하)
