# weather = input('오늘 날씨는 어떻습니까? \'(ex: 화창, 흐림)\'')
#
# if weather == '화창':
#    print("오늘도 행복한 하루~")
# else:
#    print("기운내세요!")

#now_time = input('현재 시간을 입력하세요 예: 08:15) ')
#
#hour = int(now_time.split(':')[0])


# if hour < 9:
#    print('50% 할인 받으세요')
# else:
#    print('할인을 받지 못합니다.')


# numbers = int(input('숫자를 입력하세요: '))
#
# if numbers % 2 == 0:
#     print(f'{numbers}는 짝수입니다.')
# else:
#    print(f'{numbers}홀수입니다.')

sum_n = 0
for i in 1,2,3,4,5,6:
    sum_n += i
else:
    print(sum_n)

#132
# '''
# for i in range(3):
#     coffee = input('주문하세요: 아메리카노, 카페라테, 카푸치노:')

#     if coffee == '아메리카노':
#         print(f'{coffee} 주문했당')
#     elif coffee == '카페라테':
#         print(f'{coffee} 주문 완료')
#     elif coffee == '카푸치노':
#         print(f'{coffee} 주문함')
#     else:
#         print('잘못된 주문임')
# else:
#     print('3잔의 주문이 완료됨')

# '''  

# i = 0
# j = 0

# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i * j}')

favorite_food = ['카레', '김치볶음밥', '삼겹살']

while True:
    Food_1 = input('용진이가 좋아하는 음식이 뭘까요?')
    if Food_1 not in favorite_food:
        print('당신은 용진이에 대해 잘 모르시는군요')
        continue
    print(f'용진이가 좋아하는 음식은{favorite_food}가 맞아요!')
    break

print('종료'.center(5,'-')) ## 여기있는 숫자는 총 길이를 얘기함
