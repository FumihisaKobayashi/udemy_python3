#{}で辞書
d = {'x': 10, 'y': 20}
print(d)
print(type(d))#type = 辞書

print(d['x'])
print(d['y'])

d['x'] = 100 #xに代入
d['x'] = 'XXXXXXX' #文字列も入る
print(d['x'])

#辞書の追加
d['z'] = 200 #文字 追加
print(d)

d[1] = 10000 #数字 追加
print(d)

#メソッドで追加する
dict(a=10, b=20)
print(dict(a=10, b=20))

#リストで追加する
w = dict([('a', 10), ('b', 20)])
print(w)