# 문자열 처리 함수

python = "Python is Amazing"

print(python.lower())  # 소문자로 리턴
print(python.upper())  # 대문자로 리턴
print(python[0].isupper())  # 첫번째 문자가 대문자인지 T/F
print(len(python))  # 문자열의 길이 알려줌 (공백포함)
print(python.replace("Python", "Java"))  # "Python" 을 찾아서 "Java"로 바꾼후 리턴

index = python.index("n")  # n 이 몇번째에 있는지 리턴
print(index)

index = python.index("n", index + 1)  # n 이 있는곳에서 두번째 n 을 리턴
print(index)

print(python.find("n"))  # n 이 몇번째에 있는지 리턴
print(python.find("Java"))  # 없어서 -1 리턴 index 로하면 에러나서 멈춤

print(python.count("n"))  # n 이 몇개 있는지 리턴
