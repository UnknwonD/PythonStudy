#집합 (set)
#중복 안됨, 순서 없음

#중복된 수가 들어가면 없애버림
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
#python을 set함수를 통해 집합으로 만듦
python = set(["유재석", "박명수"])

#교집합 (java 와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 
print(java - python)
print(java.difference(python))

#집합에 요소를 추가
python.add("김태호")
print(python)

#집합에서 요소를 제외
java.remove("김태호")
print(java)