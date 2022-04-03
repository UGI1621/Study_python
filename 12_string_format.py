# 문자열 포맷

print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 25)  # %d(정수) 위치에 %x 값을 넣음
print("나는 %s를 좋아해요." % "파이썬")  # %s(문자열) 위치에 %"x" 값을 넣음
print("Apple 은 %c로 시작해요." % 'A')  # %c(문자) 위치에 %'A' 값을 넣음

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 여러개는 %(x,y) 로 넣음

# 방법 2
print("나는 {}살 입니다." .format(20))  # {}에 format(x) x값을 넣음
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))  # 여러개 넣을때 .format("x","y")

# {} 에 숫자넣으면 .format(1,2...)의 자리에 값을 넣음
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3 (format 안에서 변수선언 가능)
print("나는 {age}살이며, {color}색을 좋아해요." .format(
    age=20, color="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요." .format(
    age=20, color="빨간"))

# 방법 4 (3.6v 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
