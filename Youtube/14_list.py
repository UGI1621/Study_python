# 리스트 []

# Ex)지하철 칸별로 10명, 20명, 30명 있음
subway1 = 10
subway2 = 20
subway3 = 30
#          0,  1,  2   번째
subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)


# 조세호가 몇 번째 칸에 있음?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨가 (0)유재석 / (1)조세호 사이에 탑승함
subway.insert(1, "정형돈")
print(subway)

# 지하철 끝부터 한명씩 하차함
print(subway.pop())  # 누가 내렸음
print(subway)  # 누가 남았음

# 같은 이름의 사람이 몇명 있니

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 리버스 가능
num_list.reverse()
print(num_list)

# 다 내려라
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
