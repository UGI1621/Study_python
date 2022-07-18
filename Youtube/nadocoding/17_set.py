# 집합
# 중복 x 순서 x

my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java n python)
print(java & python)
print(java.intersection(python))

# 합집합 (java u python)
print(java | python)
print(java.union(python))

# 차집합 (java 에서 python 뺌)
print(java-python)
print(java.difference(python))

# python 에 추가
python.add("김태호")
print(python)

# java 에서 삭제
java.remove("김태호")
print(java)
