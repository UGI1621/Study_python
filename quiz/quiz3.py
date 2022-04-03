'''
Quiz) 사이트별 password 생성 프로그램

예) http://naver.com

규칙 1: http:// 부분은 제외 => naver.com
규칙 2: 처음 만나는 점(.) 이후 부분은 제외 =>naver
규칙 3: 남은 글자 중 처음 세자리 + 글자 수 + 글자 내 'e' 갯수 + '!' 로 구성
                (nav)             (5)           (1)             (!)
                slicing           len          count
예) 생성된 비밀 번호 : nav51!
'''

site = "http://instagram.com"

first = site[7:10]
second = len(site[7:site.index(".")])
third = site.count("e")
forth = "!"
print(f"{site}에서 생성된 password : {first}{second}{third}{forth}")

'''
센세 답

url = "http://naver.com"

my_str = url.replace("http://", "") => (never.com) 규칙1
my_str = my_str[:my_str.index(".")] => my_str[0:5] (naver) 규칙2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다." .format(url, password))
'''
