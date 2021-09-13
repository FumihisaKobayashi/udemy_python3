for fruit in ['apple', 'orange', 'banana']:
  if fruit == 'orange':
    print('stop eating!')
    break #ループから抜けるため、elseは実行されない
  print(fruit)
else:#全てのループ終えたら出力
  print('I ate all!')
