#사전 
# 중괄호로 선언함, 내부의 요소는 {키 값 : 요소} 로 구성되어있음
cabinet = {3:"유재석", 4:"이대호"}

#호출할 때는 키 값을 넣어서 불러오면 됨
#값이 없으면 오류가 나면서 팅김
print(cabinet[4])

#get method 를 이용해서 불러올 수도 있음
print(cabinet.get(3))
#값이 없으면, None을 출력함
print(cabinet.get(5))
#키 값 뒤에 문자열을 넣을 시, none 대신 문자열 출력
print(cabinet.get(5, "사용 가능"))

# 3번 키 값이 할당 돼있는지 확인
print(3 in cabinet) #True
print(5 in cabinet) #False

#키 값에 문자열을 넣을 수도 있음
cabinet = {"3-a":"유재석", "4-a":"이대호"}
print(cabinet)

#값을 추가하거나 업데이트 할 떄,
cabinet["5-a"] = "장원영"
cabinet["3-a"] = "아이유"
cabinet["6-a"] = "조세호"
print(cabinet)

#del 함수를 이용해서 요소를 제거할 수 있음
del cabinet["6-a"]
print(cabinet, "조세호 탈락")

#key들만 출력
print(cabinet.keys())

#value 값만 출력
print(cabinet.values())

#모두 함께 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)