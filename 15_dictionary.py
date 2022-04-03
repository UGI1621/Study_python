# 사전

# key에 대한 중복 허락 x
cabinet = {3: "유재석", 100: "김태호"}    # key:value
print(cabinet[3])
print(cabinet[100])

# print(cabinet[5]) -> 오류나고 종료됨

print(cabinet.get(3))  # 방법 1
print(cabinet.get(5))  # None 리턴
print(cabinet.get(5, "사용 가능"))  # 값 없으면 '사용 가능' 리턴

# 값 있는지 확인
print(3 in cabinet)  # boolean 으로 리턴

# key 에 문자도 가능
Ecabinet = {"A-3": "유재석", "B-100": "김태호"}
print(Ecabinet["A-3"])
print(Ecabinet["B-100"])

# 새 손님 옴
print(Ecabinet)
Ecabinet["C-20"] = "조세호"  # key C-20 value 에다가 조세호 대입
Ecabinet["A-3"] = "김종국"
print(Ecabinet)

# 손님 감

del Ecabinet["A-3"]
print(Ecabinet)

# key 만 출력
print(Ecabinet.keys())

# value 만 출력
print(Ecabinet.values())

# 둘다출력
print(Ecabinet.items())

# 목욕탕 문닫음 다 나가라
Ecabinet.clear()
print(Ecabinet)
