'''
Quiz)
당신의 학교에선 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨 3명은 커피 쿠폰을 받게됩니다.
추첨 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 과 sample 을 활용

(출력예제)
 -- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
 -- 축하합니다. --
 
 (활용예제)

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))'''

from random import *
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(my_list)
chicken = sample(my_list, 1)  # 중복 불가임
coffee = sample(my_list, 3)       # 한번에 뽑아야함
print(" -- 당첨자 발표 --")
print("치킨 당첨자 :", chicken)
print("커피 당첨자 :", coffee)
print(" -- 축하합니다 --")

'''
센세답
from random import *

users = range(1,21)        1부터 20까지 숫자 생성
users = list(users)

shuffle(users)

winners = sample(users,4)

print("치킨당첨자 : {0}".format(winners[0]))
print("커피당점차 : {0}" .foramt(winers[1:]))
'''
