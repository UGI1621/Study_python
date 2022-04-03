# 변수

# 예) 애완동물을 소개 해주세요
animal = "고양이"
name = "해피"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + " 이름은 " + name + " 입니다.")

hobby = "공놀이"
# 콤마 (,) 는 형변형 필요없음. 한칸씩 띄움
print(name, "은", age, "살이고", hobby, "을 좋아함")
# 형 변형
print(name + "은 어른인가요? " + str(is_adult))
