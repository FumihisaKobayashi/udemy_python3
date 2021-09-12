
#入力された文言が特定でなければループに戻る

while True:
  word = input('Enter:')
  num = int(word)#intは型をinteggerに変える必要がある
  if word == '100':#入力された文字がokならループを抜ける(string)
    break
  print('next')
