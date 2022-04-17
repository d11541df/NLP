# # 섹션 05-2
# # 파이썬 흐름제어 반복문

# # 코딩의 핵심 >>> 조건 해결 중요

# # 기본 반복문: for, while

# from concurrent.futures import ThreadPoolExecutor


# v1 = 1

# # while v1 < 11:
# #     print("v1 is :", v1)
# #     v1 += 1

# # for v2 in range(1,100):
# #     print('v2 is :', v2)

# # sum1 = 0
# # cnt1 = 1

# # while cnt1 < 101:
# #     sum1 += cnt1
# #     cnt1 += 1
# #     print("총합은:",sum1)

# # 시퀀스( 순서가 있는) 자료형 반복
# # 문자열, 리스트, 튜플, 집합, 사전 === 반복 가능
# # iterable 리턴 함수: range, reversed, enumerate, filter, zip

# names = ['kim', 'park', 'jung', 'lee','cho']

# for name in names:
#     print("You are :", name)

# word = 'dreams'

# for s in word:
#     print("Word: ", s)


# my_info = {
#     "name": "kim", 
#     "age" : 33,
#     "city" : "Seoul"
# }

# for key in my_info:
#     print("my info :", key)

# for key in my_info.values():
#     print("my info :", key)

# print()

# for k, v in my_info.items():
#     print("my info :", k, v)

# name = "KennRY"

# for n in name:
#     if n.isupper():
#         print(n.lower())
#     else:
#         print(n.upper())

# # break

# numbers= [1, 4, 15, 75, 14, 66, 41, 2, 64, 78]

# for i in numbers:
#     if i == 14:
#         print('찾았다: 14')
#         break
#     else:
#         print("not found: 33!") 

# # for ~ else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# for i in numbers:
#     if i == 14:
#         print("found : 14")
#     else:
#         print("not found: 14") 
# else:
#     print("Not Found 14........")
# # Continue

# lt = ['1', 2, 5, True, complex(4.3),(4,3,5), {5:54}]

# for i in lt:
#     if type(i) is bool:
#         continue
#     print("타입:", type(i))

q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for i in q1.keys():
    if i == "가을":
        print(q1[i])