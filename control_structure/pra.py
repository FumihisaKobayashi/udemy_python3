some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list): 
  print(some_list[i])
  i += 1

for fruit in ['apple', 'orange', 'banana']:
  if fruit == 'orange':
    print('stop eating!')
    break #ループから抜ける
  print(fruit)
else:#全てのループ終了出力
  print('I ate all!')