x = 10

#if文は上から見るようにする

if x < 0:#if のあとは４つスペーす開ける
  print('negative')
elif x == 0:
  print('zero')
elif x == 10:
  print('10')
else:
  print('positive')

a = 5
b = 10

if a > 0:
  print('a is positive')
  if b > 0:#段落ズレるとエラー出る
    print('b is positive')
#インテンドを綺麗に合わせないとエラー出る


