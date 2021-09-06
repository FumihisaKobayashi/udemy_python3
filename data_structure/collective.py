a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
#{}重複は省略される
print(type(a))

b = {2, 3, 3, 6, 7}
print(b)

#集合
print(a - b)#aからbを取り除く
print(b - a)#bからaを取り除く

print(a & b) #aにもb二もある

print(a | b)#全ての数字が出る
print(a ^ b)# どちらかaかbにあるが重複していない
