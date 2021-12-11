# Q) 댓글이벤트를 열었음, 1명은 치킨, 3명은 커피 
# 편의상 댓글을 20명이 작성하였음 아이디는 1~20
# random 모듈과 shuffle, sample을 활용

from random import *

users = []

for i in range(20) :
    users.append(i+1)
print(users)

#리스트를 섞어줌
shuffle(users)
print(users)

#리스트에서 4개의 요소를 뽑아냄
winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")

