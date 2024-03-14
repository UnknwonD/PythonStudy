#문자열 슬라이싱
daeho = "000910-1234567"

print("성별 : " + daeho[7])
print("년도 : " + daeho[:2])
print("월 : " + daeho[2:4])
print("일 : " + daeho[4:6])

print("생년월일 : " + daeho[:6])
print("뒤 7자리 : " + daeho[7:])
print("맨 뒤에서 7번째부터 끝까지 : " + daeho[-7:])

#문자열 처리함수
a = "Python is fuckin Cool"

print(a.lower())
print(a.upper())
print(a[0].isupper())
print(len(a))
print(a.replace("Python", "Java"))

index = a.index("i")
print(index)
index = a.index("i", index+1)
print(index)
print(a.find("java"))
print(a.count("f"))

#문자열 포맷
print("나는 %d살입니다." % 20)
print("나는 %s과 %s를 좋아합니다." % ("돈", "명예"))

print("나는 {}살입니다.".format(20))
print("나는 {}과 {}를 좋아합니다.".format("돈", "명예"))
print("나는 {1}과 {0}를 좋아합니다.".format("돈", "명예"))

print("나는 {age}살입니다.".format(age = 20))

age = 20
color = "blue"
print(f"나는 {age}살이며 {color}색을 좋아합니다.")