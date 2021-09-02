i = [1, 2, 3, 4, 5]
j = i #上と同じ
j[0] = 100
print('j =', j) #別で出力, list dictionary参照渡し
print('i =', i)

#両方に100が入る

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100 #メソッドで yのみに書き込み
print('y =', y)# 数値など 値わたし 
print('x =', x)

x = 20
y = x
y = 5

print(id(y)) #別に格納されてる
print(id(x))
print(y)
print(x)

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(y)) #同じ格納先のデータが参照される
print(id(x))
print(y)
print(x)
