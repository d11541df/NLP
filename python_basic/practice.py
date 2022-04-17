a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'banana', 'orange']
e = [10, 100, ['Pen', 'banana', 'orange']]

print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2])


print(c + d)
print(str(c[0]) + 'hi')

#리스트 수정, 삭제
c[0] = 77

print(c)

c[1:2] = [100, 1000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1]
print(c)
print()
print()
print()


# 리스트 함수
y = [5,2,3,1,4]
print(y)
y.append(6)  # 맨 끝부분에 '6'추가
print(y)

y.sort()
print(y)