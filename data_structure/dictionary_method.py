d  = {'x': 10, 'y': 20}
print(d)

print(d.keys()) #keyを指定する
print(d.values()) #values指定

d2 = {'x': 1000, 'j':500}
print(d2)
#dのxを1000を入れて jを付け加える
d.update(d2)#dをd2に上書きする
print(d)

#dに対して中身みる
print(d['x'])
print(d.get('x'))#.get(メソッド)

#print(d['z']) ないものはエラーになる

#取り出す(dから取り除く)には.pop
d.pop('x')
print(d)

#delでも辞書から削除
del d['y'] #変数del d で実行するとdの辞書自体全て消える
print(d)

#辞書の中身だけを消すとき、d.clear()で消す
d.clear()
print(d)

d  = {'x': 10, 'y': 20}

#中身確認
'a' in d #'a'はdに入っているか  TRUE or FALSE
