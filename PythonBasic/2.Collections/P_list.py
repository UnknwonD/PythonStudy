#리스트 생성
subway = ['유재석', '조세호', '박명수']
print(subway)

# 조세호는 몇 번째에 있는가
print(subway.index("조세호"))

#리스트의 마지막에 이대호를 추가
subway.append("이대호")
print(subway)

#리스트의 1번째 자리에 하하를 추가함
subway.insert(1, "하하")
print(subway)

#리스트에서 한명씩 뒤에서 꺼냄 -> 리스트에서 사라짐
for i in range(3) :
    print(subway.pop())
    print(subway)

#같은 이름이 몇 개있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

#리스트 내부의 정렬
num_list = [4,3,2,1,5]
num_list.sort()
print(num_list)

#역순으로 조정
num_list.reverse()
print(num_list)

#내부 요소 모두 삭제
num_list.clear()
print(num_list)

#리스트는 내부에서 다양한 자료형을 함께 사용할 수 있음
mix_list = ["이대호", 3, 2.4, False]
print(mix_list)

#하나의 리스트로 합치기
num_list = [4,3,2,1,5]
num_list.extend(mix_list)
print(num_list)

#리스트의 요소로 리스트를 넣을 수도 있음
num_list = [4,3,2,1,5]
num_list.append(mix_list)
print(num_list)
