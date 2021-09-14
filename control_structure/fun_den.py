#からのリスト、辞書はデフォルト引数で使わない

#作りたい時は、自分でからになるようにする
def test_func(x, l =None):#からのデフォルト引数Noneにしておく
  if l is None:#もしlがNoneであれば
    l = []#からのリストを用意して渡す
  l.append(x)
  return l
"""
y = [1, 2,3]
r = test_func(100, y)
print(r)

y = [1, 2,3]
r = test_func(200, y)
print(r)
"""
#100２つ入るバグに繋がる、リストはデフォルト引数で与えるべきではない
r = test_func(100)
print(r)
r = test_func(100)#う一番上のプログラムさしたまま
print(r)

#参照渡しをデフォルトに置くとバグに繋がる

