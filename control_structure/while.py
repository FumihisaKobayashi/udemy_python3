"""
count = 0

while count < 5:#count が５よりも小さいときループする
  print(count)
  count += 1#countに1を足す　これがないとむげんループ
"""

count = 0
while True:
  if count >= 5: #countが５よりも大きいときはループから抜ける(break)
    break#if判定で合致したらループを抜けるという手法
  print(count)
  count += 1


count = 0
while True:
  if count >= 5: 
    break

  if count == 2:
    count += 1
    continue#次の分に行かずにスキップして次のループに行く
  print(count)
  count += 1
