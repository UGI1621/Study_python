'''
Quiz) 
당신은 최근에 코딩 스터티 모임을 새로 만듬.
월 4회 스터디하는데 3번은 온라인 1번은 오프라인
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램

조건 1: 랜덤으로 날짜를 뽑음
조건 2: 월별 날짜는 다름을 감안해서 28일 이내
조건 3: 매월 1~3일은 스터디 준비로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x일로 선정됨.'''


from random import *

on_list = []
for i in range(3):
    a = randint(4, 28)
    on_list.append(a)
print("온라인 스터디 모임 날짜는 매월 " + str(on_list) + " 일로 선정됨.")

off_list = []
for i in range(1):
    b = randint(4, 28)
    off_list.append(b)
print("오프라인 스터디 모임 날짜는 매월 " + str(off_list) + " 일로 선정됨.")


'''센세 답 

from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정됨.")
'''
