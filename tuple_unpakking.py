num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple #xとyに数字が入る 10 20
print(x, y)
#↓と同じ
x, y = (10, 20)#()なしでも同じ
print(x, y)
#tupleで展開されてる xに１０が入る yに２０が入る

#長いと読みにくくなると読みづらい ２〜３位
min, max = 0, 100
print(min, max)

#置き換える 
i = 10
j = 20

#置き換えに３行かかる
tmp = i
i = j
j = tmp
print(i, j)

#tupleアンパッキングで置き換えを行う
a = 100
b = 200
print(a, b)
a, b = b, a # aにb入れる bにaを入れる
print(a, b)
