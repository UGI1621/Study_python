id = "hong"
password = "1234"

input_id = input("아이디를 입력하세요 : ")
input_pass = input("비밀번호를 입력하세요 : ")

print("로그인 여부 : ", input_id == id and input_pass == password)
