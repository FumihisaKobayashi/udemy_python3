some_list = [1, 2, 3, 4, 5]

"""
i = 0
while i < len(some_list): #中身を順に出力
  print(some_list[i])#some_listのi番目
  i += 1
"""
"""
for i in some_list: #some_listから（反復処理）inで入れていき、イテレーターをinでいれていく
  print(i)
#自分で１ずつ足していく必要がない

for s in 'abcde':#文字abcdeから順に取り出す
  print(s)
"""

for word in ['my', 'name', 'is', 'Mike']:
  if word == 'name':
      continue #break ループを抜ける #スキップしてループ続ける
  print(word)
